"""
Server-side storage for CV generation attempts.

Each attempt stores all wizard state: region, personal details, uploaded documents,
parsed text, AI results (template recommendations), etc. Keyed by attempt_id,
stored as JSON on disk. This avoids re-uploading files and re-calling the AI
when the user navigates back and forth in the wizard.
"""

import json
import time
import uuid
from pathlib import Path
from typing import Any

ATTEMPTS_DIR = Path(__file__).parent.parent / "uploads" / "attempts"


def create_attempt() -> str:
    """Create a new empty attempt and return its ID."""
    attempt_id = uuid.uuid4().hex[:16]
    _save(attempt_id, {
        "id": attempt_id,
        "created_at": time.time(),
        "step": 1,
    })
    return attempt_id


def get_attempt(attempt_id: str) -> dict | None:
    """Load attempt data by ID. Returns None if not found."""
    path = _path(attempt_id)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def update_attempt(attempt_id: str, **fields: Any) -> dict:
    """Update specific fields on an attempt. Returns the updated attempt."""
    data = get_attempt(attempt_id)
    if data is None:
        data = {"id": attempt_id, "created_at": time.time()}
    data.update(fields)
    data["updated_at"] = time.time()
    _save(attempt_id, data)
    return data


def save_document(attempt_id: str, doc_key: str, filename: str, file_bytes: bytes) -> str:
    """Save an uploaded document to disk and record it in the attempt.

    doc_key: "cv_file" or "extra_doc_0", "extra_doc_1"
    Returns the path relative to the attempt directory.
    """
    attempt_dir = _ensure_dir(attempt_id) / "docs"
    attempt_dir.mkdir(exist_ok=True)

    # Use a stable name based on doc_key so re-uploads overwrite
    ext = Path(filename).suffix.lower()
    safe_name = f"{doc_key}{ext}"
    file_path = attempt_dir / safe_name
    file_path.write_bytes(file_bytes)

    # Record in attempt metadata
    data = get_attempt(attempt_id) or {}
    docs = data.get("documents", {})
    docs[doc_key] = {
        "filename": filename,
        "stored_as": safe_name,
        "size": len(file_bytes),
    }
    update_attempt(attempt_id, documents=docs)

    return str(file_path)


def get_document_bytes(attempt_id: str, doc_key: str) -> bytes | None:
    """Read a previously stored document's bytes."""
    data = get_attempt(attempt_id)
    if not data:
        return None
    docs = data.get("documents", {})
    doc_info = docs.get(doc_key)
    if not doc_info:
        return None

    file_path = _ensure_dir(attempt_id) / "docs" / doc_info["stored_as"]
    if file_path.exists():
        return file_path.read_bytes()
    return None


def get_document_filename(attempt_id: str, doc_key: str) -> str | None:
    """Get the original filename of a stored document."""
    data = get_attempt(attempt_id)
    if not data:
        return None
    docs = data.get("documents", {})
    doc_info = docs.get(doc_key)
    return doc_info["filename"] if doc_info else None


def _path(attempt_id: str) -> Path:
    return _ensure_dir(attempt_id) / "attempt.json"


def _ensure_dir(attempt_id: str) -> Path:
    # Sanitize attempt_id to prevent directory traversal
    safe_id = "".join(c for c in attempt_id if c.isalnum())
    d = ATTEMPTS_DIR / safe_id
    d.mkdir(parents=True, exist_ok=True)
    return d


def _save(attempt_id: str, data: dict) -> None:
    path = _path(attempt_id)
    path.write_text(json.dumps(data, default=str))
