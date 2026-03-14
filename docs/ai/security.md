# Security Architecture — QuillCV

**Last updated**: 14 March 2026
**Audience**: Backend developer, infrastructure engineer, security reviewer
**Scope**: PII protection, encryption layers, data flow, admin visibility

---

## Overview

QuillCV stores sensitive user data — CV content, identity fields, uploaded files. The
architecture uses two independent encryption layers to limit the blast radius of any
credential or infrastructure compromise.

```
User Data
    │
    ├── Identity fields (name, email, address, phone)
    │       └── Layer 1: PII Vault (password-derived key)
    │
    ├── Uploaded files (CV PDFs, photos)
    │       └── Layer 2: File encryption at rest (server key, Cloudflare R2)
    │
    └── Generated CV output (stored documents)
            └── Layer 2: File encryption at rest (server key)
```

---

## Layer 1 — PII Vault (Zero-Knowledge Identity Fields)

### Purpose

Identity fields are the most sensitive personal data. Layer 1 ensures that even if an
attacker gains full database access, they cannot read raw identity values without the
user's password.

### How it works

```
User password
    │
    ▼
PBKDF2-SHA256 (100,000 iterations, unique salt per user)
    │
    ▼
Derived encryption key (256-bit)
    │
    ▼
AES-256-GCM encrypt(plaintext_pii_value)
    │
    ▼
Stored in DB: { ciphertext, iv, salt }
```

### Covered fields

| Field         | Stored as         |
|---------------|-------------------|
| Full name     | Encrypted blob    |
| Email address | Encrypted blob    |
| Phone number  | Encrypted blob    |
| Address       | Encrypted blob    |
| LinkedIn URL  | Encrypted blob    |

Email is also stored as a salted hash for login lookup (separate from the encrypted blob).

### Implications

- **Admin cannot read** raw identity fields. Database queries return ciphertext only.
- **Password reset** requires re-encryption: after a password change, all PII vault fields
  are decrypted with the old key and re-encrypted with the new key during the same request.
- **Account recovery** is limited. If a user loses their password and cannot reset it via
  email, their PII vault contents are irrecoverable. This is a deliberate privacy trade-off.

---

## Layer 2 — File Encryption at Rest

### Purpose

Uploaded and generated files are stored on Cloudflare R2. Layer 2 ensures files are
encrypted at rest independent of R2's own default encryption.

### How it works

```
File bytes (PDF, DOCX, photo, generated HTML)
    │
    ▼
AES-256-GCM encrypt(file_bytes, server_master_key)
    │
    ▼
Stored on Cloudflare R2
```

The `server_master_key` is a 256-bit key stored in environment variables (never in source
code or the database). In production this is injected via the deployment secrets manager.

### Covered objects

| Object type           | Storage location       |
|-----------------------|------------------------|
| Uploaded source CV    | R2 (encrypted)         |
| Uploaded photo        | R2 (encrypted)         |
| Generated CV (HTML)   | R2 (encrypted)         |
| Generated CV (PDF)    | R2 (encrypted, temp)   |

---

## Placeholder System — PII Isolation from AI Providers

### Purpose

CV content is sent to AI providers (Google Gemini, Anthropic Claude) for generation.
Raw PII must never leave the application boundary in plain text.

### Data flow

```
User submits CV generation request
    │
    ▼
PII Extractor
  - Decrypts Layer 1 fields using user's session key
  - Builds a placeholder map:
      { "[NAME]": "Jane Smith", "[EMAIL]": "jane@example.com", ... }
    │
    ▼
Sanitized payload (PII replaced with tokens)
    │
    ▼
AI Provider API (Gemini / Claude)
  ← Receives: "[NAME] is applying for a Senior Engineer role at Acme..."
  → Returns: CV draft with [NAME], [EMAIL] tokens preserved
    │
    ▼
Rehydrator
  - Replaces placeholder tokens with real values
  - Real values never leave the application server
    │
    ▼
Final CV output rendered / stored
```

### Placeholder token set

| Token          | Maps to              |
|----------------|----------------------|
| `[NAME]`       | Full name            |
| `[EMAIL]`      | Email address        |
| `[PHONE]`      | Phone number         |
| `[ADDRESS]`    | Full address         |
| `[LINKEDIN]`   | LinkedIn URL         |
| `[CITY]`       | City (if separate)   |

Tokens are deterministic so AI models can use them naturally in prose.

---

## Data Retention and Cleanup

| Data type                  | TTL / retention policy                          |
|----------------------------|-------------------------------------------------|
| Temporary upload (session) | Auto-deleted after 7 days                      |
| Generated PDF (download)   | Auto-deleted after 24 hours                    |
| Stored CVs (account)       | Retained until user deletes or closes account   |
| Profile / PII vault        | Retained until user closes account              |
| Analytics (Google)         | Governed by Google Analytics data retention     |
| Stripe payment records     | Governed by Stripe (financial compliance)       |

A background job (`cleanup_expired_files`) runs daily and deletes R2 objects past TTL.

---

## What Admins Can and Cannot See

| Data type                        | Admin visibility          |
|----------------------------------|---------------------------|
| User email (for support)         | Hashed only — no plaintext|
| User name                        | Not visible (encrypted)   |
| User phone / address             | Not visible (encrypted)   |
| Credit balance                   | Visible                   |
| Generation count                 | Visible                   |
| CV content sent to AI            | Not stored; tokenized only|
| Payment status                   | Visible via Stripe dashboard|
| Uploaded file bytes              | Encrypted blob; not readable|

Admins can look up users by searching on the email hash. Raw PII is never displayed in
the admin panel.

---

## Threat Model Summary

| Threat                              | Mitigation                                          |
|-------------------------------------|-----------------------------------------------------|
| Database breach                     | PII vault encrypted; identity fields unreadable     |
| R2 storage breach                   | Files encrypted at rest with server key             |
| AI provider data leak               | Placeholder system; raw PII never sent              |
| Insider threat (admin access)       | Admin panel exposes no raw PII                      |
| Password compromise                 | PBKDF2 key derivation; salted hashes for login      |
| Session hijack                      | HTTPS enforced; secure, HttpOnly session cookies    |
| Brute-force / credential stuffing   | Rate limiting on login endpoint                     |

---

## Environment Variables (Production)

```
# AI Providers
ANTHROPIC_API_KEY=...       # Fallback AI provider
GEMINI_API_KEY=...          # Primary AI provider

# File Storage
R2_ENDPOINT_URL=...
R2_ACCESS_KEY_ID=...
R2_SECRET_ACCESS_KEY=...
R2_BUCKET=...

# Encryption
SERVER_MASTER_KEY=...       # 256-bit hex key for Layer 2 file encryption
                             # Never commit to source control

# Database
DATABASE_URL=...
```

`SERVER_MASTER_KEY` should be generated with:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

---

## Related Documentation

- `app/services/storage.py` — R2 upload/download with encryption wrapper
- `docs/ai/architecture/data-model.md` — Database schema and field types
- `app/templates/privacy.html` — User-facing encryption disclosures (sections 6 and 9)
- `app/templates/terms.html` — User-facing data protection commitment (section 8)
