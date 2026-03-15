# Impact vs Effort Matrix: Cover Letter Generation
**Feature**: Cover Letter Generation for QuillCV
**Date**: 2026-03-15

---

## Components Inventory

All components extracted from User Story Mapping, JTBD analysis, and Event Storming:

1. Cover letter context form (company, manager name, motivation fields)
2. Tone selector (Formal / Conversational / Confident)
3. Length selector (Concise / Standard / Detailed)
4. Region-specific defaults (auto-apply conventions per country)
5. Claude API integration for cover letter generation
6. Keyword integration from job description into generated letter
7. CV-output consistency (mirror language from the tailored CV, not just raw CV)
8. Credit deduction and balance check at generation time
9. Credit refund on generation failure (API error / timeout)
10. Cover letter preview pane (rendered HTML in-browser)
11. Inline editing of generated cover letter
12. Regeneration with confirmation dialog and credit cost shown
13. PDF export via Puppeteer (matching CV template style)
14. Plain text export / copy to clipboard
15. "Generate Cover Letter" button on CV results page
16. Bundle option: CV + CL together for 2 credits
17. Cover letter generation from main form (before CV generation)
18. Save cover letter to user account / history
19. Re-download past cover letters from history
20. DOCX export
21. Combined PDF (CV + CL in one document)
22. Keyword highlight overlay in preview
23. Partial section regeneration (just opening / just closing)
24. Multi-variation generation (2-3 versions to choose from)
25. AI-assisted editing (natural language change requests)
26. ATS score for the cover letter itself
27. Auto-extract company name from JD text
28. Email delivery from QuillCV
29. Job board integration / pre-fill
30. Standalone CL (no CV required)

---

## Scoring

### Impact Scoring (1-5)
- 5: Revenue-generating, user-blocking, or competitive necessity
- 4: Significant user value, measurable improvement
- 3: Noticeable improvement, affects subset of users
- 2: Minor improvement or cosmetic enhancement
- 1: No measurable business impact

### Effort Scoring (1-5)
- 5: Multiple sprints, new infrastructure, high uncertainty
- 4: Full sprint, moderate complexity, some unknowns
- 3: Several days, known patterns, low risk
- 2: 1-2 days, straightforward
- 1: Hours, trivial, well-understood

---

## Scored Components

| # | Component | Impact | Effort | Quadrant | Justification |
|---|-----------|--------|--------|----------|---------------|
| 1 | Context form (company, manager, motivation) | 4 | 1 | Quick Win | 3 optional text inputs. Directly personalises the output. Trivial to build. |
| 2 | Tone selector | 4 | 1 | Quick Win | Radio buttons. Claude prompt already parameterised. High user-perceived quality impact. |
| 3 | Length selector | 3 | 1 | Filler | Marginal quality improvement. Simple Claude prompt parameter. |
| 4 | Region-specific defaults | 5 | 2 | Quick Win | Auto-apply per country already set in session. Map of defaults is config, not code. Huge quality impact for international users. |
| 5 | Claude API integration for CL generation | 5 | 3 | Strategic | Core capability. Heavy prompt engineering required. Reuses existing API client but needs new prompt design + post-processing. |
| 6 | Keyword integration from JD | 5 | 2 | Quick Win | JD keywords already parsed. Injecting into prompt is configuration. Critical for ATS-aware users — core differentiator. |
| 7 | CV-output consistency (mirror tailored CV language) | 5 | 2 | Quick Win | Pass generated CV text as context in the CL prompt. Significant quality differentiator vs. generic AI tools. |
| 8 | Credit deduction + balance check | 5 | 2 | Quick Win | Credit system already exists for CV generation. Reuse same CreditService. Non-negotiable for monetisation. |
| 9 | Credit refund on failure | 4 | 2 | Quick Win | Builds trust. Existing credit service likely has refund pathway. Low effort, high trust impact. |
| 10 | Cover letter preview pane | 5 | 2 | Quick Win | HTMX partial rendering, same pattern as CV preview. Users must see output before downloading. |
| 11 | Inline editing | 4 | 2 | Quick Win | Contenteditable div or simple textarea. Directly serves the "modify" JTBD step. Users will always want to tweak. |
| 12 | Regeneration with confirmation + credit cost | 4 | 2 | Quick Win | Modal dialog + API call. Clear credit cost shown. High user satisfaction impact, avoids surprise charges. |
| 13 | PDF export via Puppeteer | 5 | 2 | Quick Win | Puppeteer already used for CV PDF. New HTML template for CL. Critical export path for email applications. |
| 14 | Plain text export / copy to clipboard | 5 | 1 | Quick Win | JavaScript clipboard API. Zero server involvement. Most online applications use text boxes — this is equally critical as PDF. |
| 15 | "Generate Cover Letter" button on results page | 5 | 1 | Quick Win | Single HTMX link/button. Entry point for the entire feature. |
| 16 | Bundle option (CV + CL, 2 credits) | 4 | 3 | Strategic | Parallel API calls, atomic credit deduction, partial-failure handling. Good conversion driver but has edge cases. |
| 17 | CL from main form (before CV generation) | 3 | 3 | Money Pit | Complicates the form flow. Most users will want CV first. Low marginal value vs. post-CV flow. |
| 18 | Save CL to user account / history | 3 | 3 | Strategic | Requires user account system. If accounts exist, this is medium effort; if not, this depends on a larger prerequisite. |
| 19 | Re-download past CLs | 3 | 2 | Filler | Low urgency. Nice to have once history exists. |
| 20 | DOCX export | 3 | 3 | Money Pit | python-docx library available but cover letter DOCX formatting is non-trivial. Low demand (PDF + plain text covers 95% of use cases). |
| 21 | Combined PDF (CV + CL in one doc) | 3 | 3 | Money Pit | Puppeteer multi-page composition. Edge cases with page layout. Low incremental value over downloading separately. |
| 22 | Keyword highlight overlay | 3 | 3 | Money Pit | Requires NLP post-processing to map keywords to positions in text. Moderate effort for a cosmetic feature. |
| 23 | Partial section regeneration | 3 | 4 | Money Pit | Complex prompt engineering (regenerate only paragraph 1 while preserving rest). High uncertainty. |
| 24 | Multi-variation generation (2-3 versions) | 3 | 4 | Money Pit | 2-3x Claude API cost per generation. Complex UX for choosing between versions. Low incremental value. |
| 25 | AI-assisted editing (natural language) | 4 | 5 | Strategic | High UX impact but multi-turn Claude interactions, complex state management, significant prompt engineering. V2 feature. |
| 26 | ATS score for cover letter | 3 | 4 | Money Pit | Significant additional analysis. Cover letter ATS scoring is less standardised than CV scoring. Uncertain value. |
| 27 | Auto-extract company name from JD | 3 | 2 | Filler | Nice UX improvement. Claude or simple regex can extract company name from JD. Not blocking. |
| 28 | Email delivery from QuillCV | 2 | 4 | Money Pit | Low demand. Adds email infrastructure complexity. Users have their own email. |
| 29 | Job board integration / pre-fill | 2 | 5 | Money Pit | Browser extension or API partnerships required. Massive scope. Minimal near-term value. |
| 30 | Standalone CL (no CV required) | 3 | 4 | Money Pit | Requires different input flow, different prompt design. Cannibalises core CV+CL proposition. |

---

## Matrix Summary

### Quick Wins (High Impact >= 4, Low Effort <= 2) — Do First

| Component | Impact | Effort | Notes |
|-----------|--------|--------|-------|
| "Generate Cover Letter" button on results page | 5/5 | 1/5 | Entry point — must exist |
| Plain text export / copy to clipboard | 5/5 | 1/5 | Critical for job portals |
| Context form (company, manager, motivation) | 4/5 | 1/5 | Direct personalisation |
| Tone selector | 4/5 | 1/5 | User control, high quality signal |
| Region-specific defaults | 5/5 | 2/5 | International differentiator |
| Keyword integration from JD | 5/5 | 2/5 | Core ATS value proposition |
| CV-output consistency (mirror tailored CV) | 5/5 | 2/5 | Unique differentiator vs. ChatGPT |
| Credit deduction + balance check | 5/5 | 2/5 | Monetisation gate |
| Credit refund on failure | 4/5 | 2/5 | Trust and reliability |
| Cover letter preview pane | 5/5 | 2/5 | Core UX — must see before downloading |
| Inline editing | 4/5 | 2/5 | Modify step in JTBD — users will always tweak |
| Regeneration with confirmation + credit cost | 4/5 | 2/5 | Safe iteration path |
| PDF export via Puppeteer | 5/5 | 2/5 | Critical export for email applications |

**Total Quick Wins: 13 components** — these form the complete V1 feature.

---

### Strategic Projects (High Impact >= 4, High Effort >= 3) — Plan Carefully

| Component | Impact | Effort | Phase | Notes |
|-----------|--------|--------|-------|-------|
| Claude API integration for CL generation | 5/5 | 3/5 | V1 (foundation) | Core engine — everything else depends on this. The "effort" is in prompt engineering quality, not infrastructure. |
| Bundle option (CV + CL, 2 credits) | 4/5 | 3/5 | V2 | Good conversion driver. Needs careful credit atomicity and partial-failure handling. |
| Save CL to user account / history | 3/5 | 3/5 | V2 | Depends on whether user accounts exist. Medium effort if auth already present. |
| AI-assisted editing (natural language) | 4/5 | 5/5 | V3 | Compelling V3 capability. Multi-turn conversation model, significant prompt engineering. |

---

### Fillers (Low Impact <= 3, Low Effort <= 2) — Fill Spare Capacity

| Component | Impact | Effort | Notes |
|-----------|--------|--------|-------|
| Length selector | 3/5 | 1/5 | Bundle with tone selector — add at no extra cost |
| Re-download past CLs | 3/5 | 2/5 | Once history exists, trivial to add |
| Auto-extract company name from JD | 3/5 | 2/5 | Nice UX polish. Add opportunistically. |

---

### Money Pits (Low Impact <= 3 or high effort with poor ROI) — Avoid or Defer

| Component | Impact | Effort | Rationale | Alternative |
|-----------|--------|--------|-----------|-------------|
| CL from main form (before CV generation) | 3/5 | 3/5 | Complicates the primary user flow. Post-CV flow is the natural moment. | Keep CL post-CV only for V1 |
| DOCX export | 3/5 | 3/5 | PDF + plain text covers 95% of use cases. DOCX formatting is finicky. | If demand exists, add in V2 |
| Combined PDF (CV + CL) | 3/5 | 3/5 | Marginal value over separate downloads. Layout complexity. | Two separate downloads is fine |
| Keyword highlight overlay | 3/5 | 3/5 | Cosmetic. Moderate effort for unclear conversion impact. | Add in V2 as engagement feature |
| Partial section regeneration | 3/5 | 4/5 | Complex prompt engineering for marginal quality gain. | Inline editing + full regeneration is sufficient |
| Multi-variation generation | 3/5 | 4/5 | 2-3x API cost. Complex UX. Users pick the first decent one. | One good generation > three mediocre ones |
| ATS score for cover letter | 3/5 | 4/5 | Cover letter ATS scoring less standardised. Better to nail the keyword integration first. | Implicit via keyword integration in generation |
| Email delivery | 2/5 | 4/5 | Users have email. Nobody needs this. | Don't build |
| Job board integration | 2/5 | 5/5 | Enormous scope. Extension / partnerships required. Years away. | Don't build |
| Standalone CL (no CV) | 3/5 | 4/5 | Different product proposition. Dilutes the "complete package" positioning. | Future standalone product if demand warrants |

---

## Priority Roadmap

### Sprint 1 — V1: Core Cover Letter Generation (All Quick Wins + Strategic Foundation)

**Goal**: Users can generate a tailored, ATS-aware, region-appropriate cover letter after generating their CV. Download as PDF or copy plain text.

Components:
1. Claude API integration with cover letter prompt (Strategic, but V1 foundation)
2. "Generate Cover Letter" entry point on results page
3. Context form (company, manager, motivation)
4. Tone selector + length selector
5. Region-specific defaults
6. Keyword integration from JD + CV-output consistency
7. Credit deduction + balance check + refund on failure
8. Preview pane
9. Inline editing
10. Regeneration (with confirmation dialog)
11. PDF export via Puppeteer
12. Plain text copy to clipboard

**Estimated effort**: 1.5–2 sprints given Claude prompt engineering investment

---

### Sprint 2 — V2: Bundle + History

**Goal**: Users can generate CV + CL as a package in one action. Past cover letters are saved and re-downloadable.

Components:
1. Bundle option (2 credits, atomic deduction, parallel generation)
2. Save CL to user account / history
3. Re-download past CLs from history
4. Auto-extract company name from JD (opportunistic filler)
5. DOCX export (if usage data from V1 shows demand)

---

### Sprint 3 — V3: AI-Assisted Editing + Engagement Features

**Goal**: Users can refine their cover letter with natural language instructions. Keyword visibility added.

Components:
1. AI-assisted editing (natural language change requests)
2. Keyword highlight overlay
3. Length selector enhancements (if not bundled in V1)

---

### Rejected / Indefinitely Deferred

- Email delivery from QuillCV — no user demand
- Job board integration — out of scope for 12-24 months
- Standalone CL without CV — possible future product, not an extension
- Combined PDF — marginal value, skip indefinitely
- Multi-variation generation — cost and UX complexity outweigh benefits
- Partial section regeneration — inline edit + full regen is sufficient
