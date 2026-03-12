"""SEO infrastructure routes: robots.txt and sitemap.xml."""

from datetime import date

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse, Response

from app.services.template_registry import list_regions, list_templates

router = APIRouter()

BASE_URL = "https://quillcv.com"

ROBOTS_TXT = """\
User-agent: *
Allow: /
Disallow: /app
Disallow: /wizard/
Disallow: /apply-fixes
Disallow: /download-pdf
Disallow: /checkout/
Disallow: /photos/
Sitemap: https://quillcv.com/sitemap.xml
"""


@router.get("/robots.txt", include_in_schema=False)
async def robots_txt():
    """Serve robots.txt for web crawlers."""
    return PlainTextResponse(ROBOTS_TXT)


@router.get("/sitemap.xml", include_in_schema=False)
async def sitemap_xml():
    """Dynamically generate sitemap.xml listing all public pages."""
    today = date.today().isoformat()

    urls: list[str] = []

    # Static public pages
    static_pages = [
        ("/", "1.0", "weekly"),
        ("/pricing", "0.8", "monthly"),
        ("/demo", "0.9", "weekly"),
        ("/login", "0.5", "monthly"),
        ("/signup", "0.5", "monthly"),
    ]
    for path, priority, changefreq in static_pages:
        urls.append(
            f"  <url>\n"
            f"    <loc>{BASE_URL}{path}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>{changefreq}</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            f"  </url>"
        )

    # Country pages: /demo/{country_code}
    regions = list_regions()
    for region in regions:
        path = f"/demo/{region.code.lower()}"
        urls.append(
            f"  <url>\n"
            f"    <loc>{BASE_URL}{path}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>0.7</priority>\n"
            f"  </url>"
        )

    # Template + country combos: /demo/{country_code}/{template_id}
    templates = list_templates()
    for region in regions:
        for template in templates:
            if region.code in template.regions:
                path = f"/demo/{region.code.lower()}/{template.id}"
                urls.append(
                    f"  <url>\n"
                    f"    <loc>{BASE_URL}{path}</loc>\n"
                    f"    <lastmod>{today}</lastmod>\n"
                    f"    <changefreq>monthly</changefreq>\n"
                    f"    <priority>0.6</priority>\n"
                    f"  </url>"
                )

    url_block = "\n".join(urls)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{url_block}\n"
        "</urlset>"
    )

    return Response(content=xml, media_type="application/xml")
