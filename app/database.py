"""SQLAlchemy async database setup."""

import asyncio
import logging

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config.settings import database_config

logger = logging.getLogger(__name__)

_config = database_config()

engine = create_async_engine(
    _config["url"],
    echo=_config.get("echo", False),
    pool_size=_config.get("pool_size", 5),
)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def init_db():
    """Run Alembic migrations then create_all as safety net.

    1. Alembic handles column additions and schema changes on existing tables.
    2. create_all handles any new tables not yet covered by migrations.
       It's idempotent — skips tables that already exist.
    """
    from alembic import command
    from alembic.config import Config

    # Step 1: Alembic migrations (sync, run in thread)
    def _run_upgrade():
        alembic_cfg = Config("alembic.ini")
        logger.info("Running Alembic migrations to head...")
        command.upgrade(alembic_cfg, "head")
        logger.info("Alembic migrations complete.")

    await asyncio.to_thread(_run_upgrade)

    # Step 2: create_all for any new tables not yet in a migration
    from app.models import APIRequestLog, ConsentRecord, Credit, ExpressionOfInterest, Invitation, Payment, PIIVault, SavedCV, User, WebAuthnCredential  # noqa: F401
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("create_all safety net complete.")


async def get_db() -> AsyncSession:
    """Dependency: yield a database session."""
    async with async_session() as session:
        yield session
