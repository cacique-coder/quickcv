import os

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from starlette.middleware.sessions import SessionMiddleware

from app.routers import cv, demo, photos, wizard
from app.services.template_registry import list_templates, list_regions
from app.services.llm_client import AnthropicAPIClient, ClaudeCodeClient

app = FastAPI(title="QuillCV")

# Dev mode: enabled when using the default session secret (i.e. local development)
app.state.dev_mode = os.environ.get("SESSION_SECRET", "quillcv-dev-secret-change-in-prod") == "quillcv-dev-secret-change-in-prod"

# Session middleware for attempt tracking
app.add_middleware(
    SessionMiddleware,
    secret_key=os.environ.get("SESSION_SECRET", "quillcv-dev-secret-change-in-prod"),
)

# LLM clients: primary (Sonnet) for CV generation, fast (Haiku) for lightweight tasks
if os.environ.get("ANTHROPIC_API_KEY"):
    app.state.llm = AnthropicAPIClient(model="claude-sonnet-4-20250514")
    app.state.llm_fast = AnthropicAPIClient(model="claude-haiku-4-5-20251001")
else:
    app.state.llm = ClaudeCodeClient(model="sonnet")
    app.state.llm_fast = ClaudeCodeClient(model="haiku")

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent / "static"),
    name="static",
)

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

app.include_router(wizard.router)
app.include_router(cv.router)
app.include_router(demo.router)
app.include_router(photos.router)


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "templates": list_templates(),
        "regions": list_regions(),
    })
