"""Landing page and public routes."""

from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.auth.dependencies import get_current_user
from app.database import async_session
from app.services.credit_service import get_balance
from app.services.user_service import count_alpha_users

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


@router.get("/")
async def landing(request: Request):
    user = await get_current_user(request)
    if user:
        # Logged in users go to the app
        return templates.TemplateResponse("index.html", {
            "request": request,
            "user": user,
        })

    async with async_session() as db:
        alpha_count = await count_alpha_users(db)
    spots_remaining = max(0, 100 - alpha_count)

    return templates.TemplateResponse("landing.html", {
        "request": request,
        "spots_remaining": spots_remaining,
        "page_description": "Build ATS-optimized CVs tailored to job descriptions. 12 country formats, keyword matching, and AI-powered quality review. Alpha pricing: $29 for 50 generations.",
    })


@router.get("/app")
async def app_page(request: Request):
    """Main app page for authenticated users."""
    user = await get_current_user(request)
    if not user:
        return templates.TemplateResponse("landing.html", {
            "request": request,
            "spots_remaining": 100,
        })

    async with async_session() as db:
        balance = await get_balance(db, user.id)

    from app.services.template_registry import list_regions, list_templates
    return templates.TemplateResponse("index.html", {
        "request": request,
        "user": user,
        "balance": balance,
        "templates": list_templates(),
        "regions": list_regions(),
    })
