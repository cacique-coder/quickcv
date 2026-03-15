# User Story Map: Cover Letter Generation
**Feature**: Cover Letter Generation for QuillCV
**Date**: 2026-03-15
**Technique**: User Story Mapping

---

## Persona

**Primary**: Alex, the active job seeker
- Applies to 5-15 jobs per week
- Uses QuillCV to generate tailored CVs per role
- Currently writes cover letters manually, copy-pasting a template and editing each time
- Frustrated by the time cost; quality varies by how much energy they have that day
- Markets: AU and US primarily, but also UK, CA, NZ

**Secondary**: The career pivoter
- Changing industries or seniority levels
- Needs cover letters that bridge a narrative gap (why this role given that background)
- Relies more heavily on AI to craft a compelling story

---

## User Goal

> "When I find a job I want to apply for, I want to produce a complete, tailored application package — both a CV and a cover letter — quickly and confidently, so I can apply to more roles without sacrificing quality."

---

## Journey Backbone (Horizontal Steps)

```
[1. Arrive at CL]  [2. Provide Context]  [3. Configure Style]  [4. Generate]  [5. Review & Edit]  [6. Export]  [7. Apply]
```

---

## Full Story Map

### Step 1: Arrive at Cover Letter Entry Point

| Priority | Task / Capability |
|----------|-------------------|
| V1 | User sees "Generate Cover Letter" button on the results page after CV generation |
| V1 | User can access cover letter generation from the main landing form (alongside CV) |
| V1 | System infers: CV data already parsed, job description already parsed — no re-upload needed |
| V2 | User can generate a cover letter for a previously generated CV (from history/dashboard) |
| V3 | User can generate a standalone cover letter without a CV (just pastes JD + experience summary) |

---

### Step 2: Provide Optional Context

| Priority | Task / Capability |
|----------|-------------------|
| V1 | User can optionally enter: company name |
| V1 | User can optionally enter: hiring manager name (defaults to "Hiring Manager" if blank) |
| V1 | User can optionally enter: motivation / why this role (free-text, ~200 chars) |
| V1 | System pre-fills country from CV generation context |
| V2 | User can enter: specific achievements to emphasise |
| V2 | User can enter: salary expectations note (opt-in, some regions expect this) |
| V3 | User uploads a previous cover letter to use as style/tone reference |

---

### Step 3: Configure Cover Letter Style

| Priority | Task / Capability |
|----------|-------------------|
| V1 | User selects tone: Formal / Conversational / Confident |
| V1 | System applies region-specific defaults (AU: conversational-confident; US: confident; UK: formal) |
| V1 | User selects length preference: Concise (250 words) / Standard (400 words) / Detailed (600 words) |
| V2 | User selects emphasis: Skills-led / Experience-led / Motivation-led |
| V2 | User can toggle "Mirror job description language" (ATS keyword density control) |
| V3 | Custom instructions free-text field ("Don't mention my gap year", "Lead with the fintech angle") |

---

### Step 4: Generate Cover Letter

| Priority | Task / Capability |
|----------|-------------------|
| V1 | System deducts 1 credit from user's pool |
| V1 | System sends CV data + job description + user context to Claude API |
| V1 | Claude generates cover letter body with: opening hook, experience bridge, motivation/fit paragraph, call to action |
| V1 | System applies region-specific structural conventions (date format, address block, sign-off) |
| V1 | System integrates high-value keywords from job description naturally into the letter |
| V1 | System renders cover letter in preview pane (streaming or near-instant) |
| V2 | System offers "Bundle" option: generate CV + cover letter together for 2 credits with a single action |
| V2 | System detects if user has insufficient credits before generation; prompts purchase |
| V3 | System generates 2-3 variations for the user to choose from |

---

### Step 5: Review and Edit

| Priority | Task / Capability |
|----------|-------------------|
| V1 | User sees formatted plain-text preview of the cover letter |
| V1 | User can inline-edit the generated text directly in the preview |
| V1 | User can regenerate (costs another credit, with confirmation dialog) |
| V2 | User can see highlighted keywords drawn from the job description |
| V2 | User can click "Improve opening / closing" to regenerate just that section (uses partial credit?) |
| V3 | AI-assisted editing: user describes the change in natural language and system applies it |
| V3 | ATS score overlay: how well does this letter score against the job description? |

---

### Step 6: Export

| Priority | Task / Capability |
|----------|-------------------|
| V1 | User can download as PDF (via Puppeteer, matching CV's visual language) |
| V1 | User can copy plain text to clipboard (for job board text fields) |
| V1 | Cover letter PDF has consistent branding: same template style as the accompanying CV |
| V2 | User can download as DOCX (Word format, common in some markets) |
| V2 | User can download a combined PDF: CV + cover letter as a single document |
| V3 | User can email the package directly from QuillCV to an address they enter |

---

### Step 7: Apply

| Priority | Task / Capability |
|----------|-------------------|
| V1 | User applies with their downloaded package — QuillCV's job is done |
| V2 | System saves the generated cover letter to the user's account for reference |
| V2 | User can view/re-download past cover letters from their history |
| V3 | Integration with job boards: pre-fill cover letter text into application form |

---

## V1 Release Line (Walking Skeleton)

The following items form the minimum viable Cover Letter feature — a user can complete their task end-to-end:

```
[Arrive]              [Context]            [Style]             [Generate]           [Review]            [Export]
  |                     |                    |                    |                    |                    |
  See "Gen CL" btn      Enter company name   Select tone         Deduct 1 credit      Inline edit         Download PDF
  on results page       Enter mgr name       Select length       Send to Claude       Regenerate          Copy plain text
  CV+JD already         Enter motivation     Apply region        Apply region         (confirm dialog)
  available             pre-fill country     defaults            conventions
                                                                 Preview rendered
```

A user can: arrive on the CL step → add optional context → pick tone + length → click Generate → read and lightly edit → download PDF or copy text. That is a complete, shippable V1.

---

## Out of Scope (V3+)

- Standalone cover letter without a CV
- Multi-variation generation
- AI-assisted editing with natural language instructions
- ATS score overlay for the cover letter
- Email delivery from QuillCV
- Job board integrations
- Previous cover letter as style reference

---

## Key Insights from Mapping

1. **Context re-use is a superpower.** QuillCV already has the CV and JD parsed. The cover letter step is almost zero friction on the input side — the only new inputs are small optional fields. This makes the V1 trivially easy to scope.

2. **Region defaults reduce cognitive load.** Rather than forcing users to understand regional conventions, the system should silently apply them. AU users get a conversational tone by default; UK users get formal. This mirrors how the CV templates already work.

3. **Plain text export is equally important as PDF.** Most modern job applications use text boxes on company portals — the PDF is for email applications. Both formats are V1 requirements.

4. **The credit model is a decision point.** Bundling CV + CL for 2 credits is logical (same as 2 separate generations) but a "bundle discount" (1.5 credits) could be a conversion driver. Flagged for business model discussion.

5. **Regeneration UX needs care.** Users will iterate. A credit-per-regeneration model could feel punitive. Consider a first regeneration free (same session) or a "light regeneration" (adjust tone/length only, no new credit).
