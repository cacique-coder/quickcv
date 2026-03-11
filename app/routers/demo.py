from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.services.template_registry import (
    get_template, get_region, list_templates, list_regions,
)
from app.services.demo_data import get_demo_data, list_roles, get_role

router = APIRouter(prefix="/demo")
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")
cv_templates = Jinja2Templates(
    directory=Path(__file__).parent.parent / "templates"
)


@router.get("/")
async def demo_index(request: Request):
    """Browse all available templates by region."""
    return templates.TemplateResponse("demo_index.html", {
        "request": request,
        "regions": list_regions(),
        "templates": list_templates(),
        "roles": list_roles(),
    })


@router.get("/{country_code}")
async def demo_country(request: Request, country_code: str):
    """Show all templates available for a specific country."""
    country_code = country_code.upper()
    region = get_region(country_code)
    if not region:
        return HTMLResponse(f"Unknown country code: {country_code}", status_code=404)

    country_templates = list_templates(region=country_code)
    return templates.TemplateResponse("demo_country.html", {
        "request": request,
        "region": region,
        "templates": country_templates,
        "roles": list_roles(),
    })


@router.get("/{country_code}/{template_id}")
async def demo_preview(
    request: Request,
    country_code: str,
    template_id: str,
    role: str = "software-engineer",
):
    """Render a full CV demo for a specific country + template + role."""
    country_code = country_code.upper()
    region = get_region(country_code)
    template = get_template(template_id)
    selected_role = get_role(role)

    if not region:
        return HTMLResponse(f"Unknown country code: {country_code}", status_code=404)
    if not template:
        return HTMLResponse(f"Unknown template: {template_id}", status_code=404)
    if country_code not in template.regions:
        return HTMLResponse(
            f"Template '{template_id}' is not available for {region.name}",
            status_code=404,
        )

    demo_data = get_demo_data(country_code, role)

    return templates.TemplateResponse("demo_preview.html", {
        "request": request,
        "region": region,
        "template": template,
        "demo": demo_data,
        "roles": list_roles(),
        "current_role": selected_role or get_role("software-engineer"),
    })


@router.get("/{country_code}/{template_id}/raw")
async def demo_raw(
    request: Request,
    country_code: str,
    template_id: str,
    role: str = "software-engineer",
):
    """Render just the CV template (no wrapper) — for PDF generation or iframe."""
    country_code = country_code.upper()
    region = get_region(country_code)
    template = get_template(template_id)

    if not region or not template:
        return HTMLResponse("Not found", status_code=404)

    demo_data = get_demo_data(country_code, role)

    return cv_templates.TemplateResponse(f"cv_templates/{template_id}.html", {
        "request": request,
        **demo_data,
    })
