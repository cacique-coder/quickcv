# Jobs-to-be-Done Analysis: Cover Letter Generation
**Feature**: Cover Letter Generation for QuillCV
**Date**: 2026-03-15
**Technique**: Jobs-to-be-Done (JTBD)

---

## Context

QuillCV users have already completed their tailored CV. They are in "application assembly" mode — gathering and polishing the documents needed for a specific job application. The cover letter is the final piece.

---

## Primary Job

> **When** I have a job I want to apply for and have already generated my tailored CV,
> **I want to** produce a matching, personalised cover letter in minutes,
> **So I can** submit a complete, professional application package without losing momentum or burning time on the hardest document to write.

---

## Related Jobs

### Functional Jobs

| Job | JTBD Statement | Priority |
|-----|---------------|----------|
| Efficiency | When applying to multiple roles in a week, I want to generate a quality cover letter in under 5 minutes, so I can maintain application volume without sacrificing quality. | Critical |
| Consistency | When submitting an application, I want my cover letter to use the same language and emphasis as my CV, so the recruiter sees a coherent, intentional candidate. | High |
| ATS compliance | When applying through an online portal, I want my cover letter to include the right keywords from the job description, so it passes initial ATS filtering. | High |
| Regional appropriateness | When applying in a specific country, I want my cover letter to match local conventions (formality, length, salutation), so I don't come across as ignorant of local norms. | High |
| Plain text export | When filling in a job application form online, I want to copy a clean plain-text version of my letter, so I can paste it directly into the portal's text field without formatting issues. | High |
| Persuasive narrative | When I have a non-obvious fit for a role (career pivot, seniority jump), I want the cover letter to bridge the gap and explain why I'm the right candidate despite the unusual profile, so recruiters look past the surface CV mismatch. | Medium |
| Tone control | When applying to different types of organisations (startup vs. bank), I want to adjust the formality and energy of my cover letter, so it resonates with that company's culture. | Medium |

### Emotional Jobs

| Job | JTBD Statement | Priority |
|-----|---------------|----------|
| Confidence | When I submit an application, I want to feel confident the cover letter is genuinely good — not just passable — so I don't second-guess myself after hitting send. | Critical |
| Relief from blank-page anxiety | When I sit down to write a cover letter, I want to avoid the paralysis of the blank page, so I can focus on reviewing and improving rather than originating. | High |
| Pride in output | When I apply for a role I really want, I want to submit a cover letter that represents me well, so I feel I gave it my best shot regardless of outcome. | Medium |
| Reduced guilt | When I'm applying to many jobs and cutting corners on letters, I want a way to produce something good quickly, so I don't feel like I'm doing myself a disservice. | Medium |

### Social Jobs

| Job | JTBD Statement | Priority |
|-----|---------------|----------|
| Professional appearance | When a recruiter reads my application, I want to appear organised, literate, and intentional, so I make a strong first impression before any human reads my CV. | High |
| Seriousness of intent | When applying to a competitive role, I want my letter to signal that I researched the company and tailored my application, so the recruiter believes I actually want this specific job. | High |
| Parity with professional applicants | When I'm competing against candidates with career advisors or expensive coaches, I want to produce a letter of equivalent quality, so I'm not disadvantaged by lack of access to support. | Medium |

---

## Job Map

### Step 1: Define — What triggers the need?

- The user has just generated a tailored CV for a specific role in QuillCV
- OR the user is midway through a job application and realises they need a cover letter
- The trigger is the gap between "I have a great CV" and "I need a complete application"

**Desired outcomes at this step:**
- Immediately understand that cover letter generation is available in the same session
- Zero additional setup — the system already has what it needs

**Current satisfaction level (without this feature)**: Very low. The user exits QuillCV and opens a separate tool (ChatGPT, Google Docs template, or a dedicated cover letter site). Context-switching kills momentum.

---

### Step 2: Locate — Find what is needed

- User needs: their parsed CV content, the job description, company name, hiring manager name, their motivation
- Without QuillCV: user must manually re-assemble this from multiple tabs and documents
- With QuillCV: CV content and JD are already in memory; only the optional context fields need to be filled

**Desired outcomes:**
- Company name and manager name pre-filled where detectable from the JD
- Country already pre-set from the CV generation context
- One screen with a short form for optional extras

---

### Step 3: Prepare — Set up the environment/inputs

- User wants to specify tone (formal, conversational, confident) and length
- User may want to add a note about why they want this specific role
- User decides whether to generate cover letter alone or bundle with CV

**Desired outcomes:**
- Sensible defaults mean the user can skip this step entirely (region-appropriate tone pre-selected)
- Optional fields clearly marked as optional — no required fields that block generation
- Bundle option visible but not pushy

---

### Step 4: Confirm — Verify readiness

- User sees a summary: "Generating a [Formal] cover letter for [Company Name], [Role Title], [Country]. Cost: 1 credit."
- User confirms before credits are deducted
- Clear indication of credit balance remaining after generation

**Desired outcomes:**
- No surprise credit deductions
- Easy to go back and change tone/length without losing other inputs

---

### Step 5: Execute — Perform the core activity

- System sends structured prompt to Claude API
- System streams or returns the generated cover letter
- Puppeteer renders PDF version in the background

**Desired outcomes:**
- Generation completes in under 10 seconds
- The letter is immediately readable — no "loading" purgatory
- Letter is substantively tailored, not generic filler with name swapped in

---

### Step 6: Monitor — Track progress

- For short generation: spinner with estimated time
- For longer sessions (rare): progress indicator
- User can see credit balance update in real time

**Desired outcomes:**
- Never uncertain whether the system is working
- Credit deduction happens at generation start, not on download (so regeneration costs are transparent)

---

### Step 7: Modify — Make adjustments

- User reads the draft and may want to:
  - Edit specific phrases inline
  - Regenerate (with or without changed settings)
  - Adjust tone or length and regenerate
  - Add/remove a specific paragraph focus

**Desired outcomes:**
- Inline editing is low-friction (direct text editing in the preview)
- Regeneration is possible but with a friction bump (confirm dialog, credit cost shown)
- First regeneration within the same session costs a credit (same as generation)

---

### Step 8: Conclude — Finish the job

- User downloads PDF and/or copies plain text
- User feels ready to submit their application
- The application package (CV + CL) is coherent and complete

**Desired outcomes:**
- Both PDF and plain text available without extra steps
- PDF looks professional and visually consistent with the CV template
- User feels confident the job is done well — not just done

---

## Underserved Outcomes (Opportunity Areas)

| Outcome | Importance | Current Satisfaction | Opportunity Score |
|---------|-----------|---------------------|-------------------|
| Generate CL and CV as a matched package in one session | 5 | 1 (no tool does this) | 5 + (5-1) = **9** |
| Have the CL automatically use the same tone/keywords as the tailored CV | 5 | 1 (not possible today) | **9** |
| Produce a regionally appropriate CL with no manual effort | 4 | 2 (must know conventions yourself) | 4 + (4-2) = **6** |
| Copy plain text immediately for job portal pasting | 4 | 2 (existing tools export PDF only or require formatting cleanup) | **6** |
| Get a confident, non-generic first draft in under 5 minutes | 5 | 2 (ChatGPT can do this but requires manual context setup) | **7** |
| Feel proud of the output (not just relieved it's done) | 4 | 2 (most AI drafts need significant editing) | **6** |

*Opportunity Score = Importance + (Importance - Satisfaction). Score > 8 = high opportunity.*

---

## Current Alternatives and Their Failures

| Alternative | What Users Do | Why It Falls Short |
|-------------|--------------|-------------------|
| ChatGPT / Claude.ai | Manually paste CV + JD + instructions | No context memory; repeated friction per application; output quality depends on how well the user prompts |
| Dedicated cover letter sites (Zety, Resume.io, etc.) | Use a template wizard | Generic output; no real JD parsing; not ATS-aware; separate tool with separate account |
| Google Docs / Word template | Edit a saved template | Copy-paste effort; tone and content diverge from tailored CV; blank-page anxiety if rewriting |
| Career advisor / coach | Pay for human-written letter | High quality but expensive ($50-200/letter); not scalable for volume applications |
| Skip the cover letter | Don't submit one | Losing a signal of intent; some applications require it; some hiring managers do read them |

---

## Switch Trigger

> "After using QuillCV to generate my tailored CV in 2 minutes, I opened ChatGPT to write the cover letter and spent 40 minutes going back and forth to get something decent. I kept thinking — why can't the thing that knows my CV and the job description just write this too?"

This is the canonical switch moment. The feature exists to eliminate that 40-minute journey.

---

## Key Design Principles from JTBD

1. **The job is "complete the package", not "write a letter".** Design language should reinforce this: "Your application package is ready" not "Your cover letter has been generated."

2. **Defaults must be excellent.** Emotional jobs around confidence and pride in output require that the zero-configuration path produces a genuinely good letter. Tone and length defaults must be carefully calibrated by region.

3. **Plain text is a first-class citizen.** The social job of "filling in the portal text box" is how most applications actually happen. PDF is for email applications. Both must be equally prominent in the export UI.

4. **ATS keyword integration earns trust.** The functional job of ATS compliance is why users are here. If the generated letter reads like a human wrote it AND passes ATS, that is the product's unfair advantage vs. generic AI tools.

5. **Speed is part of the value proposition.** The efficiency JTBD is critical-priority. Under 5 minutes from "I have a CV" to "I have a complete application" is the target. Generation speed and UX flow must be optimised together.
