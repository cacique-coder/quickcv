from dataclasses import dataclass, field


@dataclass
class CVTemplate:
    id: str
    name: str
    description: str
    best_for: str
    regions: list[str]


@dataclass
class RegionConfig:
    code: str
    name: str
    flag: str
    language: str
    date_format: str
    page_length: str
    include_photo: str  # "required", "common", "optional", "no"
    include_references: bool
    include_dob: bool
    include_nationality: bool
    include_visa_status: bool
    include_marital_status: bool
    paper_size: str  # "A4" or "Letter"
    spelling: str  # "British", "American", "Canadian", etc.
    notes: list[str] = field(default_factory=list)
    sources: list[dict] = field(default_factory=list)  # [{title, url}]


TEMPLATES: dict[str, CVTemplate] = {
    "classic": CVTemplate(
        id="classic",
        name="Classic",
        description="Traditional single-column with serif fonts. Conservative and universally accepted.",
        best_for="Corporate, government, finance, legal",
        regions=["AU", "US", "UK", "CA", "NZ", "DE", "FR", "NL", "IN", "BR", "AE", "JP"],
    ),
    "modern": CVTemplate(
        id="modern",
        name="Modern",
        description="Clean sans-serif with blue accent color. Professional yet contemporary.",
        best_for="Marketing, consulting, general professional roles",
        regions=["AU", "US", "UK", "CA", "NZ", "DE", "FR", "NL", "IN", "BR", "AE", "JP"],
    ),
    "minimal": CVTemplate(
        id="minimal",
        name="Minimal",
        description="Ultra-clean Harvard-style. Maximum whitespace, no color, pure content focus.",
        best_for="Academia, research, any role where content > design",
        regions=["AU", "US", "UK", "CA", "NZ", "DE", "FR", "NL", "IN", "BR", "AE", "JP"],
    ),
    "executive": CVTemplate(
        id="executive",
        name="Executive",
        description="Dark header, authoritative layout with key achievements section.",
        best_for="Senior/C-level roles, director positions, management",
        regions=["AU", "US", "UK", "CA", "NZ", "DE", "FR", "NL", "IN", "BR", "AE", "JP"],
    ),
    "tech": CVTemplate(
        id="tech",
        name="Tech",
        description="Skills-forward layout with tech tags, project sections, and stack listings.",
        best_for="Software engineering, DevOps, IT, data science",
        regions=["AU", "US", "UK", "CA", "NZ", "DE", "FR", "NL", "IN", "BR", "AE", "JP"],
    ),
    "compact": CVTemplate(
        id="compact",
        name="Compact",
        description="Dense layout maximizing content per page. Great for extensive experience.",
        best_for="Experienced professionals, career changers with lots of history",
        regions=["AU", "US", "UK", "CA", "NZ", "DE", "FR", "NL", "IN", "BR", "AE", "JP"],
    ),
}


REGIONS: dict[str, RegionConfig] = {
    "AU": RegionConfig(
        code="AU",
        name="Australia",
        flag="🇦🇺",
        language="Australian English",
        date_format="DD/MM/YYYY",
        page_length="2–3 pages",
        include_photo="no",
        include_references=True,
        include_dob=False,
        include_nationality=False,
        include_visa_status=True,
        include_marital_status=False,
        paper_size="A4",
        spelling="British",
        notes=[
            "Include 2–3 professional references with full contact details",
            "May include visa/work rights status (e.g., 'Full working rights')",
            "Use Australian English spelling (organised, programme, colour)",
            "Do NOT include photo, age, date of birth, or marital status",
            "Typical length: 2–3 pages; up to 5 for senior/executive",
            "Reverse chronological is the most accepted format",
            "Go back 10–15 years of experience unless highly relevant",
        ],
        sources=[
            {"title": "Novorésumé – Australian Resume Guide", "url": "https://novoresume.com/career-blog/australian-resume"},
            {"title": "VisualCV – Australia CV Guide", "url": "https://www.visualcv.com/international/australia-cv/"},
            {"title": "DreamShift – AU CV Format 2025", "url": "https://dreamshift.net/blog/2025/09/03/australia-cv-format-2025-a-guide-by-dreamshift/"},
        ],
    ),
    "US": RegionConfig(
        code="US",
        name="United States",
        flag="🇺🇸",
        language="American English",
        date_format="MM/YYYY",
        page_length="1–2 pages",
        include_photo="no",
        include_references=False,
        include_dob=False,
        include_nationality=False,
        include_visa_status=False,
        include_marital_status=False,
        paper_size="Letter",
        spelling="American",
        notes=[
            "Strict 1–2 page limit; 1 page preferred for < 10 years experience",
            "Do NOT include photo, age, DOB, marital status, or nationality",
            "'References available upon request' is outdated — omit entirely",
            "Use American English spelling (organized, program, color)",
            "Use standard section headings: Summary, Experience, Skills, Education",
            "Include both acronym and full form for technical terms (e.g., 'CI/CD')",
            "Letter size paper (8.5 × 11 in), not A4",
        ],
        sources=[
            {"title": "Indeed – ATS Resume Template", "url": "https://www.indeed.com/career-advice/resumes-cover-letters/ats-resume-template"},
            {"title": "Jobscan – ATS-Friendly Resume 2026", "url": "https://www.jobscan.co/blog/20-ats-friendly-resume-templates/"},
            {"title": "ResumeWorded – ATS Templates", "url": "https://resumeworded.com/resume-templates"},
        ],
    ),
    "UK": RegionConfig(
        code="UK",
        name="United Kingdom",
        flag="🇬🇧",
        language="British English",
        date_format="DD/MM/YYYY",
        page_length="1–2 pages",
        include_photo="no",
        include_references=False,
        include_dob=False,
        include_nationality=False,
        include_visa_status=False,
        include_marital_status=False,
        paper_size="A4",
        spelling="British",
        notes=[
            "1–2 pages is the norm; 2 pages max for experienced professionals",
            "Do NOT include photo, age, gender, marital status, or nationality",
            "Include a concise Personal Profile / Summary (3–4 lines)",
            "'References available on request' is optional — can omit entirely",
            "Use British English spelling (organised, behaviour, colour)",
            "Achievement-focused bullets with quantified results",
            "Use 2.5 cm margins, Arial/Calibri/Verdana 11–12pt",
        ],
        sources=[
            {"title": "Novorésumé – UK Resume Guide", "url": "https://novoresume.com/career-blog/uk-resume-guide"},
            {"title": "VisualCV – UK CV Guide", "url": "https://www.visualcv.com/international/uk-cv/"},
            {"title": "Brendan Hope – UK CV Format", "url": "https://brendanhope.com/blog/how-to-write-uk-cv-2025/"},
        ],
    ),
    "CA": RegionConfig(
        code="CA",
        name="Canada",
        flag="🇨🇦",
        language="Canadian English / French",
        date_format="YYYY-MM-DD",
        page_length="1–2 pages",
        include_photo="no",
        include_references=False,
        include_dob=False,
        include_nationality=False,
        include_visa_status=False,
        include_marital_status=False,
        paper_size="Letter",
        spelling="Canadian",
        notes=[
            "1–2 pages; slightly more detail acceptable than US resumes",
            "Do NOT include photo, DOB, marital status, or religion",
            "Use Canadian English spelling (behaviour, colour, but program not programme)",
            "Highlight language proficiency — English and French especially",
            "Use metric units (kilometres, kilograms)",
            "Date format: YYYY-MM-DD (ISO standard)",
            "Results-oriented with numbers and clear outcomes",
            "In bilingual regions (Quebec), consider a French version",
        ],
        sources=[
            {"title": "Novorésumé – Canadian Resume Format", "url": "https://novoresume.com/career-blog/canada-resume-format"},
            {"title": "Resumemate – Canada vs US Resume", "url": "https://www.resumemate.io/blog/canada-resume-format-differences-from-us-templates/"},
            {"title": "Indeed – Canadian Format Resume", "url": "https://www.indeed.com/career-advice/resumes-cover-letters/resume-in-canadian-format"},
        ],
    ),
    "NZ": RegionConfig(
        code="NZ",
        name="New Zealand",
        flag="🇳🇿",
        language="New Zealand English",
        date_format="DD/MM/YYYY",
        page_length="2–3 pages",
        include_photo="no",
        include_references=True,
        include_dob=False,
        include_nationality=False,
        include_visa_status=True,
        include_marital_status=False,
        paper_size="A4",
        spelling="British",
        notes=[
            "2–3 pages is typical; focus on relevance and impact",
            "Do NOT include age, DOB, marital status, health, nationality, or photo",
            "CV and resume are used interchangeably in NZ",
            "May include visa/work rights status",
            "Include references (2–3 professional referees)",
            "Use Calibri or Arial, 11–12pt, with 2.5 cm margins",
            "Always save and send as PDF",
        ],
        sources=[
            {"title": "VisualCV – NZ Resume Guide", "url": "https://www.visualcv.com/international/new-zealand/"},
            {"title": "Careers.govt.nz – NZ CV Tips", "url": "https://www.careers.govt.nz/job-hunting/new-to-new-zealand/tips-for-creating-a-nz-style-cv/"},
            {"title": "CV App NZ – Best CV Formats", "url": "https://cvapp.nz/blog/cv-format"},
        ],
    ),
    "DE": RegionConfig(
        code="DE",
        name="Germany",
        flag="🇩🇪",
        language="German",
        date_format="DD.MM.YYYY",
        page_length="1–2 pages",
        include_photo="common",
        include_references=False,
        include_dob=True,
        include_nationality=True,
        include_visa_status=False,
        include_marital_status=False,
        paper_size="A4",
        spelling="German",
        notes=[
            "Use tabular (tabellarisch) format — structured, scannable layout",
            "Professional photo is common (not legally required but expected in many industries)",
            "Include date of birth and nationality in personal details",
            "Reverse chronological order, 1–2 pages",
            "Employers may expect certificates (Zeugnisse) as attachments",
            "Optional: place, date, and signature at the bottom",
            "Use simple font: Times New Roman or Roboto, 11pt body, 14–16pt headers",
            "Cover letter (Anschreiben) is typically required alongside the CV",
        ],
        sources=[
            {"title": "Expatrio – German CV Guide", "url": "https://www.expatrio.com/about-germany/how-draft-perfect-german-cv-format-and-template"},
            {"title": "CV Creator – German CV Format", "url": "https://cv-creator.co.uk/cv-advice/german-cv/"},
            {"title": "Fintiba – German CV Structure", "url": "https://www.fintiba.com/germany/working/german-cv"},
        ],
    ),
    "FR": RegionConfig(
        code="FR",
        name="France",
        flag="🇫🇷",
        language="French",
        date_format="DD/MM/YYYY",
        page_length="1–2 pages",
        include_photo="common",
        include_references=False,
        include_dob=False,
        include_nationality=False,
        include_visa_status=False,
        include_marital_status=False,
        paper_size="A4",
        spelling="French",
        notes=[
            "1 page for junior, 2 pages for experienced professionals",
            "Photo is common but not mandatory (expected for client-facing roles)",
            "Strong emphasis on education (formations) — list before experience for juniors",
            "Do NOT include full address, marital status, religion, or ID numbers",
            "Date format: DD/MM/YYYY (e.g., 12/05/2023 = 12 May 2023)",
            "Language skills are very important — include proficiency levels",
            "Cover letter (lettre de motivation) is always expected",
            "Use A4 paper, clean modern design",
        ],
        sources=[
            {"title": "Novorésumé – French Resume Guide", "url": "https://novoresume.com/career-blog/french-resume"},
            {"title": "VisualCV – France CV Guide", "url": "https://www.visualcv.com/international/france-cv/"},
            {"title": "Enhancv – French Resume", "url": "https://enhancv.com/blog/french-resume/"},
        ],
    ),
    "NL": RegionConfig(
        code="NL",
        name="Netherlands",
        flag="🇳🇱",
        language="Dutch / English",
        date_format="DD-MM-YYYY",
        page_length="1–2 pages",
        include_photo="optional",
        include_references=True,
        include_dob=True,
        include_nationality=False,
        include_visa_status=False,
        include_marital_status=False,
        paper_size="A4",
        spelling="British",
        notes=[
            "1–2 pages; 1 page if < 5 years experience",
            "Photo inclusion varies — becoming less common but still seen",
            "Date of birth and address are commonly included",
            "Direct, factual tone — avoid exaggeration or overly promotional language",
            "Cover letter (motivatiebrief) is expected alongside CV",
            "Many roles accept English-language CVs (especially international companies)",
            "Use simple professional font: Arial or Times New Roman",
            "References section is common",
        ],
        sources=[
            {"title": "I Am Expat – Dutch CV Guide", "url": "https://www.iamexpat.nl/career/employment-guides-tools/cv-guide-netherlands"},
            {"title": "Undutchables – Preparing a Good CV", "url": "https://undutchables.nl/get-ready/preparing-a-good-cv"},
            {"title": "WorkInHolland – Dutch CV Tips", "url": "https://www.workinholland.com/about-workinholland/inspiration/blogs/this-is-how-you-write-the-perfect-dutch-cv"},
        ],
    ),
    "IN": RegionConfig(
        code="IN",
        name="India",
        flag="🇮🇳",
        language="English / Hindi",
        date_format="DD/MM/YYYY",
        page_length="2–3 pages",
        include_photo="common",
        include_references=True,
        include_dob=True,
        include_nationality=True,
        include_visa_status=False,
        include_marital_status=True,
        paper_size="A4",
        spelling="British",
        notes=[
            "2–3 pages is acceptable; 1–2 pages for tech roles at MNCs",
            "Photo is commonly expected by many employers",
            "Personal details (DOB, gender, marital status) often included — MNCs may discourage this",
            "Strong emphasis on educational qualifications with grades and ranks",
            "Technical skills and certifications are highlighted prominently",
            "Languages section is nearly always present (multilingual professionals)",
            "Objective statement is expected (not summary) for traditional companies",
            "Key projects and internships are important, especially for freshers",
        ],
        sources=[
            {"title": "VisualCV – India CV Guide", "url": "https://www.visualcv.com/international/india-cv/"},
            {"title": "ResumeGenius – Indian Resume Format", "url": "https://resumegenius.com/blog/resume-help/indian-resume"},
            {"title": "Kickresume – Indian Resume Format Guide", "url": "https://www.kickresume.com/en/blog/indian-resume-format-guide/"},
        ],
    ),
    "BR": RegionConfig(
        code="BR",
        name="Brazil",
        flag="🇧🇷",
        language="Portuguese",
        date_format="DD/MM/YYYY",
        page_length="1–2 pages",
        include_photo="optional",
        include_references=False,
        include_dob=True,
        include_nationality=True,
        include_visa_status=False,
        include_marital_status=True,
        paper_size="A4",
        spelling="Portuguese",
        notes=[
            "1–2 pages maximum; concise and professional",
            "Personal details (DOB, marital status, nationality) are standard",
            "Photo is optional — becoming less common, but still seen",
            "Write in Portuguese for local companies; English for MNCs",
            "Lying on a CV is a prosecutable offense in Brazil",
            "Reverse chronological order for both education and experience",
            "Use Calibri or Verdana, 1-inch margins, A4 paper",
            "Cover letter is commonly expected",
        ],
        sources=[
            {"title": "Resume Example – Brazilian CV Guide", "url": "https://resume-example.com/cv/portuguese-brazil-language"},
            {"title": "ResumeFlex – Brazil Job Market CV", "url": "https://resumeflex.com/how-to-write-a-professional-cv-for-brazil-job-market/"},
            {"title": "ProResumes – Brazilian Resume Standards", "url": "https://proresumes.io/international-standards-for-brazilian-resumes/"},
        ],
    ),
    "AE": RegionConfig(
        code="AE",
        name="UAE / Dubai",
        flag="🇦🇪",
        language="English / Arabic",
        date_format="DD/MM/YYYY",
        page_length="2–3 pages",
        include_photo="common",
        include_references=True,
        include_dob=True,
        include_nationality=True,
        include_visa_status=True,
        include_marital_status=True,
        paper_size="A4",
        spelling="British",
        notes=[
            "2–3 pages; more detailed than Western CVs",
            "Photo is expected, especially for customer-facing roles",
            "Include nationality, visa status, DOB, and marital status",
            "Highlight UAE/GCC work experience prominently",
            "English is standard unless the role specifically requires Arabic",
            "Dubai favors modern international format; Abu Dhabi prefers formal structure",
            "Use STAR method for describing achievements",
            "Do NOT use scanned/JPG CVs — use Word or text-based PDF",
            "Include availability and notice period if possible",
        ],
        sources=[
            {"title": "VisualCV – UAE Resume Guide", "url": "https://www.visualcv.com/international/uae-resume/"},
            {"title": "GulfTalent – Dubai CV Format", "url": "https://www.gulftalent.com/resources/dubai-jobs-guide/building-your-profile"},
            {"title": "Bayt – UAE CV Format 2025", "url": "https://www.bayt.com/en/blog/32302/what-is-a-good-cv-format-for-uae-jobs-in-2025/"},
        ],
    ),
    "JP": RegionConfig(
        code="JP",
        name="Japan",
        flag="🇯🇵",
        language="Japanese",
        date_format="YYYY/MM/DD",
        page_length="Standardized forms",
        include_photo="required",
        include_references=False,
        include_dob=True,
        include_nationality=True,
        include_visa_status=True,
        include_marital_status=True,
        paper_size="A4 / B5",
        spelling="Japanese",
        notes=[
            "Two-document system: Rirekisho (履歴書) + Shokumu-keirekisho (職務経歴書)",
            "Rirekisho: standardized JIS format with personal details, education, work history",
            "Shokumu-keirekisho: flexible format for detailed work experience and achievements",
            "Photo is required — passport-style professional headshot",
            "Must be written in Japanese (unless applying to English-teaching roles)",
            "Include DOB, nationality, marital status, and number of dependents",
            "Digital submission is now acceptable (handwritten used to be required)",
            "Cover letter is also typically expected",
        ],
        sources=[
            {"title": "Jobs in Japan – Two-Resume System", "url": "https://jobsinjapan.com/working-in-japan/understanding-japans-two-resume-system/"},
            {"title": "VisualCV – Japan Resume Guide", "url": "https://www.visualcv.com/international/japan-resume/"},
            {"title": "Japan Dev – Rirekisho Guide", "url": "https://japan-dev.com/blog/japanese-resume-rirekisho"},
        ],
    ),
}


# Keep backward compat alias
REGION_RULES = {
    code: {
        "include_references": r.include_references,
        "include_visa_status": r.include_visa_status,
        "date_format": r.date_format,
        "max_pages": r.page_length,
        "notes": r.notes,
    }
    for code, r in REGIONS.items()
}


def get_template(template_id: str) -> CVTemplate | None:
    return TEMPLATES.get(template_id)


def get_region(code: str) -> RegionConfig | None:
    return REGIONS.get(code)


def list_templates(region: str | None = None) -> list[CVTemplate]:
    if region:
        return [t for t in TEMPLATES.values() if region in t.regions]
    return list(TEMPLATES.values())


def list_regions() -> list[RegionConfig]:
    return list(REGIONS.values())
