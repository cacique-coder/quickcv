"""Logs each CV generation run to a JSONL file for analysis and debugging.

Each line is a self-contained JSON object with the full pipeline state:
ATS before/after, keywords gained/still missing, score breakdown, timing, etc.

Log file: app/logs/generations.jsonl
"""
import json
import time
from pathlib import Path

from app.services.ats_analyzer import ATSResult

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_FILE = LOG_DIR / "generations.jsonl"


def _score_breakdown(ats: ATSResult) -> dict:
    """Recreate the individual score components for debugging."""
    kw_pts = min(ats.keyword_match_pct * 0.4, 40)
    sections_found = sum(ats.section_checks.values())
    section_pts = (sections_found / max(len(ats.section_checks), 1)) * 30
    format_pts = max(0, 20 - len(ats.formatting_issues) * 5)
    rec_pts = max(0, 10 - len(ats.recommendations) * 2)
    return {
        "total": ats.score,
        "keywords_pts": round(kw_pts, 1),
        "sections_pts": round(section_pts, 1),
        "formatting_pts": round(format_pts, 1),
        "recommendations_pts": round(rec_pts, 1),
    }


def log_generation(
    attempt_id: str,
    region: str,
    template_id: str,
    cv_text: str,
    job_description: str,
    ats_original: ATSResult,
    ats_generated: ATSResult,
    generated_text: str,
    cv_data: dict,
    timings: dict[str, float],
):
    """Append a generation log entry."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # Keywords that were missing and got added
    gained = [kw for kw in ats_generated.matched_keywords if kw in ats_original.missing_keywords]
    still_missing = ats_generated.missing_keywords

    entry = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "attempt_id": attempt_id,
        "region": region,
        "template_id": template_id,
        "timings_sec": timings,

        # ATS comparison
        "score_original": ats_original.score,
        "score_generated": ats_generated.score,
        "score_delta": ats_generated.score - ats_original.score,
        "breakdown_original": _score_breakdown(ats_original),
        "breakdown_generated": _score_breakdown(ats_generated),

        # Keywords
        "job_keywords_total": len(ats_original.matched_keywords) + len(ats_original.missing_keywords),
        "original_keyword_match_pct": ats_original.keyword_match_pct,
        "generated_keyword_match_pct": ats_generated.keyword_match_pct,
        "keywords_gained": gained,
        "keywords_gained_count": len(gained),
        "keywords_still_missing": still_missing[:30],
        "keywords_still_missing_count": len(still_missing),

        # Sections
        "sections_original": ats_original.section_checks,
        "sections_generated": ats_generated.section_checks,

        # Formatting
        "formatting_issues_original": ats_original.formatting_issues,
        "formatting_issues_generated": ats_generated.formatting_issues,

        # Recommendations still firing on generated CV
        "recommendations_generated": ats_generated.recommendations,

        # Content stats
        "cv_input_chars": len(cv_text),
        "cv_output_chars": len(generated_text),
        "job_desc_chars": len(job_description),
        "experience_count": len(cv_data.get("experience", [])),
        "skills_count": len(cv_data.get("skills", [])),

        # LLM usage & cost
        "llm": cv_data.get("_llm_usage", {}),

        # Raw texts for manual review
        "cv_text_preview": cv_text[:1000],
        "generated_text_preview": generated_text[:1000],
        "job_desc_preview": job_description[:1000],
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
