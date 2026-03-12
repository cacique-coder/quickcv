# QuillCV

ATS-optimized CV builder that tailors CVs to specific job descriptions with region-specific formatting for 12 countries.

## What it does

1. Parses your existing CV (PDF, DOCX, or plain text)
2. Analyzes the target job description for keywords and requirements
3. Searches for similar-profile CVs online as reference
4. Generates an ATS-optimized CV tailored to the role
5. Provides ATS scoring, keyword gap analysis, and recommendations

Supports region-specific formats for AU, US, UK, CA, NZ, DE, FR, NL, IN, BR, AE, and JP — each with appropriate conventions for photos, personal details, references, and page length.

## Tech stack

- **Backend**: Python, FastAPI, Jinja2
- **Frontend**: HTMX + server-rendered HTML
- **AI**: Multi-provider LLM abstraction (Anthropic, OpenAI, Gemini)
- **CV parsing**: pdfplumber (PDF), python-docx (DOCX)
- **Photo storage**: Local + Cloudflare R2
- **PDF generation**: Puppeteer
- **Database**: SQLAlchemy + aiosqlite
- **Payments**: Stripe

## Setup

### Prerequisites

- Python 3.12+
- Node.js (for PDF generation)
- [mise](https://mise.jdx.dev/) (optional, for task runner)

### Install

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node dependencies (for PDF generation)
npm install
```

### Environment variables

```bash
ANTHROPIC_API_KEY=...          # Or OPENAI_API_KEY / GOOGLE_API_KEY
LLM_PROVIDER=anthropic         # anthropic | openai | gemini
SESSION_SECRET=...             # Session encryption key

# Optional — Cloudflare R2 for photo persistence
R2_ENDPOINT_URL=...
R2_ACCESS_KEY_ID=...
R2_SECRET_ACCESS_KEY=...
R2_BUCKET=...

# Optional — Stripe for payments
STRIPE_SECRET_KEY=...
STRIPE_WEBHOOK_SECRET=...
```

In dev mode (no API key set), the app falls back to Claude Code CLI for LLM calls.

### Run

```bash
# Development
uvicorn app.main:app --reload --port 8000

# Or with mise
mise run dev

# Production
gunicorn app.main:app -c gunicorn.conf.py
```

## Quality checks

```bash
mise run lint          # Ruff linter
mise run security      # Bandit security scanner
mise run audit         # pip-audit for known CVEs
mise run test          # Pytest with coverage
mise run check         # All of the above
```

## CV templates

46 ATS-optimized HTML/CSS templates covering general-purpose designs (classic, modern, minimal, executive, tech, compact) and specialized formats (academic, federal, consulting, healthcare, legal, creative, and region-specific like europass, lebenslauf, rirekisho, curriculo).
