# PRD: Cover Letter Generation

**Version**: 1.0
**Date**: 2026-03-15
**Author**: Feature Discovery (Autonomous — QuillCV context)
**Status**: Draft

---

## 1. Executive Summary

QuillCV users currently generate a tailored, ATS-optimized CV in under two minutes — but then leave the product to spend 30–90 minutes writing a cover letter manually, often using a generic template or a separate AI tool with no access to the CV data already held in session. This creates a product experience gap immediately after the feature users love most.

Cover Letter Generation closes this gap by completing the application package. Using the CV data and job description already parsed in the user's session, the system generates an ATS-aware, regionally appropriate, tonally consistent cover letter matched to the same role. Users control tone (Formal / Conversational / Confident), length (Concise / Standard / Detailed), and can add optional personalisation (company name, hiring manager, motivation note). Generation costs one credit from the existing pool. Output is available as a PDF (via Puppeteer, visually consistent with the CV template) and as plain text for direct pasting into job portal text fields.

This feature is a natural extension that reuses every major infrastructure component already built: the Claude API integration, the Puppeteer PDF renderer, the credit system, the country/region configuration, and the JD keyword extraction. The primary implementation investment is in prompt engineering quality and the cover letter HTML template. The business impact is an immediate increase in session value — users who complete both CV and CL in a single session have a materially better application outcome and a stronger reason to use their remaining credits quickly.

---

## 2. Problem Statement

### The Problem

After generating a tailored CV, users must switch to a separate tool to write a cover letter. This creates friction at the highest-intent moment of the user journey. The tools available — ChatGPT, Google Docs templates, dedicated cover letter sites — all require the user to manually re-provide context (CV data, job description, company name) that QuillCV already holds. The result is inconsistency between the CV and the cover letter, a poor ATS keyword density in the letter, and significant time spent on a document that should be the easy companion to the CV.

### Who Is Affected

- **Primary**: Active job seekers in AU and US markets applying to 5–15 roles per week. High frequency, time-sensitive, value efficiency above all.
- **Secondary**: Career pivoters and those making seniority jumps who need the cover letter to bridge a narrative gap their CV alone cannot close.
- **All QuillCV users**: Anyone who generates a CV and then encounters the "what do I do about the cover letter?" question.

### Root Cause

*(From 5 Whys analysis)*

Three compounding root causes:
1. **Data gap**: The inputs needed for a great cover letter (CV content + tailored CV language + JD keywords) are already co-located in QuillCV after CV generation — but unused for the companion document.
2. **Market gap**: No tool currently produces CV and cover letter as a unified, ATS-coherent application package from the same parsed inputs.
3. **Experience gap**: QuillCV's fast CV flow creates a contrast effect. The ease of CV generation makes the subsequent manual cover letter step feel disproportionately painful — a regression to the old way of doing things.

### Cost of Inaction

- Users complete their CV and leave QuillCV for another tool. The session ends at exactly the wrong moment — when user intent is at its peak.
- Competitors (Resume.io, Zety, Enhancv) offer cover letter features, even if lower quality. QuillCV risks appearing incomplete.
- Users who leave to write cover letters in ChatGPT may start generating CVs there too, eroding retention.
- Credits go unused because the application workflow is not fully serviced in-product.

---

## 3. Goals and Success Metrics

### Primary Goal

Enable users to generate a tailored, ATS-aware, regionally appropriate cover letter in the same session as their CV, without leaving QuillCV.

### Secondary Goals

- Increase average credits consumed per session (cover letter = additional credit use)
- Improve application package quality: coherent language between CV and cover letter
- Reduce user-reported "after-QuillCV" workflow steps
- Expand value proposition for international users through region-specific CL conventions

### Success Metrics

| Metric | Baseline | Target (30 days post-launch) | Measurement |
|--------|----------|------------------------------|-------------|
| CL generation rate (% of CV sessions that also generate a CL) | 0% | 30%+ | Event tracking on /cover-letter/generate |
| Credits per session (average) | ~1 (CV only) | 1.8+ | Credit deduction logs |
| Time-to-complete application (CV + CL) | 35-95 min (CV: 2min + CL: 30-90min manual) | < 7 minutes | Session duration analytics |
| User satisfaction score for CL output | N/A | 4.0+ / 5.0 | In-app thumbs up/down after preview |
| Regeneration rate (% of CLs that are regenerated) | N/A | < 25% (lower = first draft quality higher) | Regeneration event tracking |
| PDF download rate | N/A | 60%+ of generated CLs | Download event tracking |
| Plain text copy rate | N/A | 50%+ of generated CLs | Clipboard event tracking |

---

## 4. User Personas and Jobs-to-be-Done

### Primary Persona: Alex — The Active Job Seeker

- **Role**: Mid-level professional (3-8 years experience), applying actively to 5-15 roles per week
- **Context**: Uses QuillCV as part of a job search toolkit. Generates a tailored CV per role. Has experienced the before/after contrast of manual vs. AI-assisted CV writing.
- **Pain Points**: Time spent writing cover letters from scratch; inconsistency between CV and cover letter tone; frustration using generic AI tools that require re-providing context
- **Markets**: AU (primary), US (primary), UK, CA, NZ

### Secondary Persona: Jordan — The Career Pivoter

- **Role**: Professional changing industries or seniority level. CV alone doesn't tell the right story.
- **Context**: Uses QuillCV because the tailored CV helps address skill gaps. Needs the cover letter to explain "why this role despite the pivot" — a narrative job the CV can't do alone.
- **Pain Points**: Generic cover letters don't address the pivot narrative; AI-generated letters often miss the nuance without detailed prompting; doesn't know regional conventions for the target market
- **Markets**: All 12 countries; particularly common in DE, IN, US

### Jobs-to-be-Done

| Job | Type | Priority | JTBD Statement |
|-----|------|----------|----------------|
| Complete the application package | Functional | Critical | When I have a generated CV, I want to create a matching cover letter immediately, so I can submit a complete application without switching tools |
| Apply efficiently at volume | Functional | Critical | When applying to 5+ roles per week, I want cover letter generation to take under 5 minutes, so I can maintain quality without burning time |
| Maintain ATS compliance | Functional | High | When submitting through an online portal, I want my cover letter to include the right JD keywords, so it passes ATS filtering |
| Match regional conventions | Functional | High | When applying in a specific country, I want the letter to automatically match local formality and structure expectations, so I don't signal unfamiliarity with local norms |
| Paste into job portals | Functional | High | When filling an online application form, I want clean plain text ready to paste, so I can complete the portal form without reformatting |
| Feel confident in quality | Emotional | Critical | When I submit an application I care about, I want to feel proud of my cover letter, not just relieved it's done |
| Avoid blank-page paralysis | Emotional | High | When I sit down to write, I want a strong first draft already written, so I can edit and improve rather than originate |
| Appear serious and tailored | Social | High | When a recruiter reads my application, I want to appear to have genuinely researched and tailored my application to this specific role |

---

## 5. Functional Requirements

### Core Features — V1

| ID | Requirement | Priority | Source |
|----|-------------|----------|--------|
| FR-001 | System must display a "Generate Cover Letter" button on the CV results page immediately after CV generation | Must Have | USM Step 1, JTBD |
| FR-002 | System must present an optional context form with fields: Company Name, Hiring Manager Name, Motivation Note (all optional) | Must Have | USM Step 2 |
| FR-003 | System must offer Tone selection: Formal, Conversational, Confident | Must Have | USM Step 3, JTBD |
| FR-004 | System must offer Length selection: Concise (~250 words), Standard (~400 words), Detailed (~600 words) | Must Have | USM Step 3 |
| FR-005 | System must auto-apply region-specific defaults for tone, salutation, sign-off, and address block conventions based on the country set during CV generation | Must Have | USM Step 3, JTBD, Region Map |
| FR-006 | System must check credit balance before generation and block generation (with purchase prompt) if insufficient | Must Have | USM Step 4, Credit Policy |
| FR-007 | System must deduct 1 credit from the user's pool at the start of generation (before Claude API call) | Must Have | USM Step 4, Credit Policy |
| FR-008 | System must send a structured prompt to Claude API containing: parsed CV data, generated CV text (for language consistency), parsed JD keywords, user-provided context, region conventions, tone, and length target | Must Have | FR-006, Sequence Diagram |
| FR-009 | The Claude prompt must instruct the model to integrate high-value JD keywords naturally into the cover letter body | Must Have | JTBD ATS compliance, 5 Whys RC1 |
| FR-010 | The Claude prompt must instruct the model to mirror the language and emphasis used in the generated CV output (not just raw CV data) | Must Have | 5 Whys RC1, JTBD consistency |
| FR-011 | System must refund 1 credit automatically if the Claude API call fails (timeout or error) | Must Have | Credit trust, Event Storming Hotspot 1 |
| FR-012 | System must render the generated cover letter in a preview pane immediately on success | Must Have | USM Step 5 |
| FR-013 | System must allow the user to edit the generated cover letter text inline in the preview | Must Have | USM Step 5, JTBD Modify step |
| FR-014 | System must allow the user to regenerate the cover letter, with a confirmation dialog that clearly states the credit cost | Must Have | USM Step 5 |
| FR-015 | System must allow the user to download the cover letter as a PDF, rendered via Puppeteer with styling consistent with the CV template | Must Have | USM Step 6, JTBD |
| FR-016 | System must allow the user to copy the cover letter as plain text to the clipboard | Must Have | USM Step 6, JTBD plain text job |
| FR-017 | Region-specific structure must be applied to the generated output: appropriate address block, date format, salutation, and sign-off per the Region Convention Map | Must Have | Region Map |

### Business Rules

| ID | Rule | Condition |
|----|------|-----------|
| BR-001 | 1 credit = 1 cover letter generation | Always |
| BR-002 | Credit deducted at generation start, not on download | Always |
| BR-003 | Credit refunded automatically on API failure | On Claude error or timeout |
| BR-004 | Regeneration costs 1 credit; user must confirm before credit is deducted | On regeneration request |
| BR-005 | If credit balance is 0, generation is blocked and purchase prompt is shown | At generation attempt |
| BR-006 | Country defaults for tone/salutation/sign-off are pre-applied but user-overridable | On form load |
| BR-007 | Company name field defaults to "Hiring Manager" salutation if no manager name provided; uses company name in opener if provided | On generation |

### User Stories (V1)

**Story 1: Generate a cover letter after CV generation**
As an active job seeker who has just generated my tailored CV,
I want to generate a matching cover letter in the same session,
So that I can complete my application package without switching tools.

Acceptance Criteria:
- [ ] "Generate Cover Letter" button visible on CV results page
- [ ] Clicking the button navigates to or expands the CL context form
- [ ] CV data and JD are pre-loaded (no re-upload required)
- [ ] Country is pre-set from CV generation session
- [ ] All context fields are optional (form can be submitted empty)
- [ ] Selecting a tone and length and clicking Generate triggers generation

**Story 2: Generate a region-appropriate cover letter for an Australian role**
As a job seeker applying to a role in Australia,
I want the cover letter to automatically use Australian conventions (conversational tone, "Kind regards", no address block required),
So that my letter feels locally appropriate without requiring me to know the conventions.

Acceptance Criteria:
- [ ] Country = AU → default tone = Conversational
- [ ] Country = AU → default sign-off = "Kind regards"
- [ ] Country = AU → address block is optional (not required in output)
- [ ] User can override the tone default
- [ ] Generated letter reflects the applied defaults

**Story 3: Copy plain text for a job portal**
As a job seeker filling in an online application form with a cover letter text box,
I want to copy the generated cover letter as clean plain text,
So that I can paste it directly without formatting issues.

Acceptance Criteria:
- [ ] "Copy plain text" button visible in export options
- [ ] Clicking copies plain text to clipboard (no HTML tags, no markdown)
- [ ] Confirmation toast shown: "Copied to clipboard"
- [ ] Plain text preserves paragraph breaks but strips all formatting

**Story 4: Regenerate after reviewing the first draft**
As a user who has reviewed the generated cover letter and wants a different approach,
I want to regenerate with different settings,
So that I can find the version that best represents me.

Acceptance Criteria:
- [ ] "Regenerate" button visible in the preview
- [ ] Clicking shows a confirmation dialog: "This will use 1 credit. Proceed?"
- [ ] Confirmation required before any credit is deducted
- [ ] User can change tone/length before regenerating
- [ ] New letter replaces the current preview on success
- [ ] Credit balance updates visibly after deduction

**Story 5: Download PDF consistent with my CV**
As a user applying by email,
I want to download my cover letter as a PDF with professional formatting,
So that the letter looks polished and visually matches my CV when submitted together.

Acceptance Criteria:
- [ ] "Download PDF" button visible in export options
- [ ] PDF renders via Puppeteer using a cover letter template
- [ ] PDF uses typography and colour consistent with the CV template used
- [ ] PDF includes the region-appropriate address block and date
- [ ] File name is descriptive: `cover-letter-{company}-{role}.pdf`

---

## 6. Non-Functional Requirements

### Performance
- Cover letter generation (Claude API call + post-processing) must complete in under 10 seconds for Standard length
- PDF rendering via Puppeteer must complete in under 5 seconds
- Plain text copy must be instantaneous (client-side only)
- Preview pane must render within 500ms of API response received

### Security
- No cover letter content stored server-side beyond the active session unless the user has an account (V2 feature)
- Credit deduction operations must be idempotent — retry-safe via a generation request ID to prevent double deduction
- Claude API prompts must not expose other users' CV or JD data
- Session data cleared on session expiry (existing session security model applies)

### Reliability
- Credit refund must be guaranteed on API failure — use a transactional or compensating pattern
- Generation failure must produce a clear, actionable error message
- System must handle Claude API rate limits gracefully (queue or immediate retry with backoff)

### Accessibility
- Form controls (tone, length selectors) must be keyboard-navigable and screen-reader labelled
- Preview pane must have sufficient colour contrast
- Copy to clipboard action must announce success to screen readers via aria-live region
- Download confirmation must be accessible

### Scalability
- Cover letter generation uses the same Claude API client as CV generation — no additional infrastructure required
- PDF rendering uses the existing Puppeteer instance — cover letter adds a new template, not a new renderer
- Credit service must handle concurrent deductions safely (no double-spend race condition)

---

## 7. User Experience

### User Flows

Refer to: `flow-diagram.md` — Part 2: User-Facing Flowchart

Key UX principles from JTBD analysis:
1. **The entry point must be on the results page**, immediately after CV generation. The momentum from "your CV is ready" carries directly into "and here's your cover letter."
2. **All fields optional**: The form must feel light. A user in a hurry should be able to click Generate with zero input changes and get a good result.
3. **Region defaults are invisible**: Tone and sign-off are pre-selected based on country. The user sees the pre-selection and can change it, but does not need to understand why it was chosen.
4. **Plain text and PDF are equally prominent**: The export UI must not imply PDF is the "real" download. Many applications need plain text.
5. **Credit cost is always visible**: Before any action that costs credits (Generate, Regenerate), the cost must be shown inline. No surprise deductions.

### Key Interactions

| Interaction | Expected Behaviour | Error State |
|-------------|-------------------|-------------|
| Click "Generate Cover Letter" | Opens context form; CV and JD are already loaded | If session expired: prompt to re-generate CV |
| Click "Generate" | Shows spinner; deducts credit; calls Claude API | If no credits: show purchase prompt. If API error: show error + refund message. |
| Generated letter appears | Preview pane updates with formatted letter | If generation is empty/garbled: show "Try regenerating" with no credit deduction |
| Inline edit | Text in preview is directly editable | Changes are in-memory only; lost if user refreshes without downloading |
| Regenerate | Confirmation dialog → credit deducted → new letter | Same failure handling as initial generation |
| Download PDF | Puppeteer call → file download triggered | If Puppeteer fails: show retry option; do not charge additional credits |
| Copy plain text | Clipboard write → toast "Copied" | If clipboard blocked by browser: show text in a modal for manual copy |

### Wireframe Notes (for implementation reference)

The cover letter UI should follow this layout pattern on the results page:

```
┌─────────────────────────────────────────────────┐
│  Your CV is ready.          [Download CV PDF]   │
│  [Generate Cover Letter ▼]                      │
└─────────────────────────────────────────────────┘

On expand / navigate to CL step:

┌──────────────────────┐  ┌──────────────────────────────────┐
│ COVER LETTER SETUP   │  │ PREVIEW                          │
│                      │  │                                  │
│ Company name:        │  │ [Rendered cover letter text]     │
│ [_________________]  │  │                                  │
│ Hiring manager:      │  │ [Inline editable]                │
│ [_________________]  │  │                                  │
│ Why this role:       │  │ Word count: 387                  │
│ [_____________    ]  │  │ Keywords: 8/10 matched           │
│                      │  └──────────────────────────────────┘
│ Tone:                │
│ (•) Conversational   │  ┌──────────────────────────────────┐
│ ( ) Formal           │  │ EXPORT                           │
│ ( ) Confident        │  │ [Download PDF]  [Copy plain text]│
│                      │  │ [Regenerate (1 credit)]          │
│ Length:              │  └──────────────────────────────────┘
│ ( ) Concise          │
│ (•) Standard         │
│ ( ) Detailed         │
│                      │
│ Credits remaining: 4 │
│ [Generate (1 credit)]│
└──────────────────────┘
```

---

## 8. System Architecture

### Domain Events

*(From Event Storming — refer to `flow-diagram.md` Part 1)*

Key domain events:
- `CoverLetterRequested` — user initiates from results page
- `CoverLetterConfigurationSet` — form submitted with options
- `CreditDeducted` — credit removed from pool at generation start
- `CoverLetterGenerationStarted` — Claude API call initiated
- `CoverLetterDraftAvailable` — Claude returned successfully
- `CoverLetterEdited` — user made inline changes
- `RegenerationRequested` — user confirmed regeneration dialog
- `CoverLetterExported` — PDF downloaded or text copied
- `CreditRefunded` — generation failure, credit restored

### System Interactions

Refer to: `flow-diagram.md` — Part 3: Sequence Diagrams

### Integration Points

| System | Type | Protocol | Notes |
|--------|------|----------|-------|
| Claude API (Anthropic) | External | HTTPS / Anthropic SDK | Reuses existing client from CV generation. New prompt template. |
| Puppeteer | Internal | Node.js subprocess / IPC | Reuses existing PDF renderer. New HTML template for CL. |
| Credit Service | Internal | Python function call | Reuses CreditService from CV generation. New reason code: "cover_letter". |
| Session Store | Internal | In-memory / Redis | CV data + JD already held in session. No new storage required for V1. |

### Data Model

No new database tables required for V1 (if no user account persistence).

For V2 (account-based history):

```sql
cover_letters (
  id              UUID PRIMARY KEY,
  user_id         UUID REFERENCES users(id),
  cv_generation_id UUID REFERENCES cv_generations(id),  -- parent CV
  role_title      TEXT,
  company_name    TEXT,
  country_code    CHAR(2),
  tone            TEXT,  -- 'formal' | 'conversational' | 'confident'
  length_pref     TEXT,  -- 'concise' | 'standard' | 'detailed'
  generated_text  TEXT,
  word_count      INTEGER,
  keywords_used   TEXT[],
  created_at      TIMESTAMPTZ DEFAULT now()
)
```

### New Code Components Required

| Component | Type | Location (suggested) | Notes |
|-----------|------|----------------------|-------|
| CoverLetterService | Python service | `app/services/cover_letter_service.py` | Prompt building, Claude call, post-processing |
| CoverLetterRouter | FastAPI router | `app/routers/cover_letter.py` | `/cover-letter/form`, `/cover-letter/generate`, `/cover-letter/export/pdf` |
| cover_letter_prompt.py | Prompt template | `app/services/prompts/cover_letter_prompt.py` | Structured prompt with region + tone + context |
| region_conventions.py | Config/data | `app/services/region_conventions.py` | Defaults per country code (tone, salutation, sign-off, address block) |
| cover_letter.html | Jinja2 template | `app/templates/cover_letter.html` | Main CL template with region-variable sections |
| cover_letter_pdf.html | Puppeteer template | `app/templates/cover_letter_pdf.html` | PDF-optimised version |
| CL form partial | HTMX partial | `app/templates/partials/cover_letter_form.html` | Context form + preview pane |

---

## 9. Scope and Boundaries

### In Scope — V1

- Cover letter generation using existing CV + JD session data
- Optional context inputs: company name, hiring manager, motivation note
- Tone selection (Formal / Conversational / Confident)
- Length selection (Concise / Standard / Detailed)
- Region-specific defaults for all 12 supported countries
- ATS keyword integration from parsed JD
- CV language consistency (using generated CV text as context)
- Credit deduction (1 credit) with balance check and refund on failure
- Cover letter preview pane with inline editing
- Regeneration with confirmation dialog
- PDF export via Puppeteer
- Plain text copy to clipboard

### Out of Scope — V1

- Bundle option (CV + CL in one action) — V2
- Cover letter history / save to account — V2
- DOCX export — V2 (only if user demand demonstrated)
- AI-assisted editing (natural language) — V3
- Keyword highlight overlay — V2
- Multi-variation generation — Rejected
- Standalone cover letter (no CV) — Not planned
- Combined PDF (CV + CL) — Not planned
- Email delivery — Not planned
- Job board integration — Not planned

### Assumptions

- The existing session model already holds parsed CV data and parsed JD for the duration of the session
- Puppeteer is already running as a service (used for CV PDF generation) — no additional infrastructure needed
- The Claude API client is already configured and operational
- The Credit Service (deduct/refund) supports a `reason` field for auditing — or can be extended trivially
- Country code is already set in the session from CV generation
- User authentication is not required for V1 (same session-based model as CV generation)

### Constraints

- Must not require users to re-upload their CV or re-paste the job description
- Must stay within existing credit model pricing ($7.99 / 20 credits — CL = 1 credit = same as CV)
- Must work for all 12 supported countries, not just AU/US
- PDF output must be visually consistent with the CV template used (not a generic document style)
- Generation must not feel slower than CV generation (target: under 10 seconds)

---

## 10. Priority Matrix

*(Full detail in `impact-effort-matrix.md`)*

### Quick Wins — Sprint 1

| Component | Impact | Effort |
|-----------|--------|--------|
| "Generate Cover Letter" entry point | 5/5 | 1/5 |
| Plain text copy to clipboard | 5/5 | 1/5 |
| Context form | 4/5 | 1/5 |
| Tone selector | 4/5 | 1/5 |
| Region-specific defaults | 5/5 | 2/5 |
| Keyword integration from JD | 5/5 | 2/5 |
| CV-output consistency | 5/5 | 2/5 |
| Credit deduction + balance check + refund | 5/5 + 4/5 | 2/5 |
| Preview pane | 5/5 | 2/5 |
| Inline editing | 4/5 | 2/5 |
| Regeneration with confirmation | 4/5 | 2/5 |
| PDF export via Puppeteer | 5/5 | 2/5 |

### Strategic Projects

| Component | Impact | Effort | Phase |
|-----------|--------|--------|-------|
| Claude API integration + prompt engineering | 5/5 | 3/5 | V1 foundation |
| Bundle option (CV + CL) | 4/5 | 3/5 | V2 |
| Account history + re-download | 3/5 | 3/5 | V2 |
| AI-assisted editing | 4/5 | 5/5 | V3 |

### Deferred / Rejected

| Component | Reason |
|-----------|--------|
| Multi-variation generation | 2-3x API cost; UX complexity outweighs benefit |
| Standalone CL (no CV) | Different product proposition; dilutes packaging story |
| DOCX export | PDF + plain text covers 95% of use cases; validate demand first |
| Combined PDF | Marginal; layout complexity; low demand signal |
| Job board integration | Multiple sprints + partnerships; 18+ months away |
| ATS score for CL | Less standardised than CV scoring; keyword integration is the better approach |

---

## 11. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Claude prompt produces generic, unconvincing letters | Medium | High | Invest significant prompt engineering effort in V1. Create a test suite of 5-10 real CV+JD pairs across multiple countries and tones. Human evaluation of output quality before launch. |
| Credit double-deduction (race condition or retry) | Low | High | Implement idempotent generation requests with a unique `request_id`. CreditService checks for duplicate `request_id` before deducting. |
| Credit refund not triggered on silent API failure | Low | Medium | Wrap all Claude API calls in try/finally with explicit refund call. Add monitoring for orphaned "generation started" events with no "draft available" outcome. |
| PDF layout breaks for long cover letters (Detailed mode, DE/JP markets) | Medium | Low | Test Puppeteer template with 600-word letters in German and Japanese. Set max-width and overflow constraints. |
| Region convention map is inaccurate for some markets | Medium | Medium | Research and validate conventions for all 12 markets. Mark lower-confidence markets (BR, AE, JP) for native reviewer sign-off before launch in those markets. |
| Users treat CL generation as a reason to apply to more roles (volume abuse) | Low | Low | Credit model already controls this; each CL costs 1 credit. |
| Claude API rate limits under concurrent generation load | Low | Medium | Implement request queuing with backoff. Monitor rate limit headers. Current CV load pattern will inform expected CL load. |

### Open Questions

- [ ] **Q1**: Should the first regeneration in a session be free, to reduce friction on the "get to a good version" workflow? (Credit model decision)
- [ ] **Q2**: Can the JD parser reliably extract company name in most cases? If yes, should this be auto-filled in the form? (UX decision — reduces form friction)
- [ ] **Q3**: Should the cover letter template share visual elements with all 6 CV templates, or only the template the user selected? (Design decision)
- [ ] **Q4**: For V2 bundle option: should the price be 2 credits (same as separate) or 1.5 credits (bundle incentive)? (Pricing / conversion decision)
- [ ] **Q5**: Are there any countries in the 12 where cover letters are not expected or are culturally unusual? (JP: cover letters exist but follow a rigid formal structure — may need a special template path)

---

## 12. Timeline and Milestones

| Milestone | Target | Dependencies |
|-----------|--------|--------------|
| Prompt engineering: first draft + test suite | Week 1 | Access to test CV+JD pairs for all 12 regions |
| Backend: CoverLetterService + Router | Week 1-2 | Prompt engineering complete |
| Region conventions config | Week 1 | Research for 12 markets |
| Cover letter HTML/PDF templates | Week 2 | Design brief: typography + layout |
| Credit integration (deduct, refund) | Week 2 | Existing CreditService audit |
| HTMX frontend: form + preview + export | Week 2-3 | Backend endpoints complete |
| Inline editing + regeneration flow | Week 3 | Preview pane complete |
| QA: all 12 countries × 3 tones × 3 lengths | Week 3-4 | Feature complete |
| Prompt quality review (human eval) | Week 4 | QA complete |
| Launch V1 | Week 4-5 | All QA sign-off |
| V2 bundle option | Sprint 2 | V1 usage data available |

**Estimated total effort (V1)**: 3-4 developer-weeks. Primary investment in prompt engineering, region convention research, and HTMX frontend. Infrastructure reuse is high.

---

## Appendices

### A. Discovery Session Artifacts

| Artifact | Location |
|----------|----------|
| User Story Map | `docs/ai/artifacts/feature-discovery/cover-letters/user-story-map.md` |
| 5 Whys Analysis | `docs/ai/artifacts/feature-discovery/cover-letters/five-whys.md` |
| JTBD Analysis | `docs/ai/artifacts/feature-discovery/cover-letters/jtbd.md` |
| Flow Diagrams (Event Storming, Flowcharts, Sequence Diagrams) | `docs/ai/artifacts/feature-discovery/cover-letters/flow-diagram.md` |
| Impact vs Effort Matrix | `docs/ai/artifacts/feature-discovery/cover-letters/impact-effort-matrix.md` |

### B. Glossary

| Term | Definition |
|------|------------|
| ATS | Applicant Tracking System — software used by employers to filter and rank CVs and cover letters by keyword matching before human review |
| CL | Cover Letter — abbreviation used throughout this document |
| Credit | A unit of QuillCV currency. 1 credit = 1 CV generation OR 1 cover letter generation. Purchased in packs. |
| Bundle | A planned V2 feature where CV + CL are generated in one action for 2 credits |
| Region conventions | Country-specific norms for cover letter formatting: formality level, salutation style, sign-off style, address block presence, date format, expected length |
| Tone | The register of the generated letter: Formal (restrained, traditional language), Conversational (warm, direct), Confident (assertive, outcomes-focused) |
| Plain text export | A version of the cover letter with all HTML/CSS formatting stripped, suitable for pasting into job portal text input fields |
| Walking skeleton | In User Story Mapping: the minimum viable set of steps that allows a user to complete their end-to-end goal |
| JTBD | Jobs-to-be-Done — a product design framework that focuses on the "job" a user is hiring a product or feature to do |
