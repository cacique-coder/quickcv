"""My CVs — list and manage saved CVs."""

import json
import logging
from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates

from app.database import async_session
from app.services.cv_store import get_saved_cv, list_saved_cvs
from app.services.docx_generator import generate_docx
from app.services.pdf_generator import generate_pdf

logger = logging.getLogger(__name__)

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


@router.get("/my-cvs")
async def my_cvs_page(request: Request):
    """List all saved CVs for the current user/session."""
    user = request.state.user if hasattr(request.state, "user") else None
    user_id = user.id if user else None

    # Also check for anonymous CVs tied to builder/wizard sessions
    attempt_ids = []
    if builder_id := request.state.session.get("builder_id"):
        attempt_ids.append(builder_id)
    if wizard_id := request.state.session.get("attempt_id"):
        attempt_ids.append(wizard_id)

    async with async_session() as db:
        cvs = []
        if user_id:
            cvs = await list_saved_cvs(db, user_id=user_id)
        # Also fetch session-based CVs (anonymous users)
        for aid in attempt_ids:
            session_cvs = await list_saved_cvs(db, attempt_id=aid)
            existing_ids = {c.id for c in cvs}
            for cv in session_cvs:
                if cv.id not in existing_ids:
                    cvs.append(cv)

        # Sort by created_at descending
        cvs.sort(key=lambda c: c.created_at, reverse=True)

    return templates.TemplateResponse("my_cvs.html", {
        "request": request,
        "saved_cvs": cvs,
    })


@router.get("/my-cvs/{cv_id}/preview")
async def my_cv_preview(request: Request, cv_id: str):
    """Return rendered CV HTML for preview."""
    async with async_session() as db:
        saved = await get_saved_cv(db, cv_id)

    if not saved:
        return Response("CV not found", status_code=404)

    cv_data = json.loads(saved.cv_data_json)
    rendered = templates.get_template(
        f"cv_templates/{saved.template_id}.html"
    ).render(**cv_data)

    return Response(rendered, media_type="text/html")


@router.get("/my-cvs/{cv_id}/download")
async def my_cv_download(request: Request, cv_id: str):
    """Download a saved CV as PDF."""
    async with async_session() as db:
        saved = await get_saved_cv(db, cv_id)

    if not saved:
        return Response("CV not found", status_code=404)

    cv_data = json.loads(saved.cv_data_json)
    rendered = templates.get_template(
        f"cv_templates/{saved.template_id}.html"
    ).render(**cv_data)

    cv_name = cv_data.get("name", "CV") or "CV"
    safe_name = "".join(c for c in cv_name if c.isalnum() or c in " -_").strip() or "CV"
    label_part = f" - {saved.label}" if saved.label else ""

    pdf_bytes = await generate_pdf(rendered)
    if pdf_bytes is None:
        return Response("PDF generation failed", status_code=500)

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="{safe_name}{label_part} - QuillCV.pdf"',
        },
    )


@router.get("/my-cvs/{cv_id}/download-docx")
async def my_cv_download_docx(request: Request, cv_id: str):
    """Download a saved CV as DOCX."""
    async with async_session() as db:
        saved = await get_saved_cv(db, cv_id)

    if not saved:
        return Response("CV not found", status_code=404)

    cv_data = json.loads(saved.cv_data_json)
    region_code = saved.region or "AU"
    template_id = saved.template_id or "classic"
    cv_name = cv_data.get("name", "CV") or "CV"
    safe_name = "".join(c for c in cv_name if c.isalnum() or c in " -_").strip() or "CV"
    label_part = f" - {saved.label}" if saved.label else ""

    try:
        docx_bytes = generate_docx(cv_data, region_code=region_code, template_id=template_id)
    except Exception:
        logger.exception("DOCX generation failed for cv_id=%s", cv_id)
        return Response("DOCX generation failed", status_code=500)

    return Response(
        content=docx_bytes,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": f'attachment; filename="{safe_name}{label_part} - QuillCV.docx"',
        },
    )
