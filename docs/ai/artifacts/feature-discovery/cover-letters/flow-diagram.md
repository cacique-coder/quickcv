# Logic Visualization: Cover Letter Generation
**Feature**: Cover Letter Generation for QuillCV
**Date**: 2026-03-15
**Technique**: Event Storming + Flowcharts + Sequence Diagrams

---

## Part 1: Event Storming

### Domain Events Timeline

```
TIMELINE (left to right — chronological)

[User]
  |
  +--[REQUEST COVER LETTER]
  |         |
  |    Cover Letter
  |    Requested
  |         |
  |         v
  |    [CONTEXT FORM]
  |    Company name entered
  |    Manager name entered
  |    Motivation entered
  |    Tone selected
  |    Length selected
  |         |
  |    Cover Letter
  |    Configuration Set
  |         |
  |         v
  |    [GENERATION COMMAND]
  |         |
  |    Credit Deduction
  |    Triggered
  |         |
  |    [Credit] ----------> Credit Deducted
  |                              |
  |    Cover Letter              v
  |    Generation           [CLAUDE API]
  |    Started                   |
  |         |              CL Draft Generated
  |         |                   |
  |         +<------------------+
  |         |
  |    Cover Letter
  |    Draft Available
  |         |
  |         v
  |    [USER REVIEW]
  |    Inline edit applied?  -----> Cover Letter Edited
  |    Regenerate requested? -----> [Credit Deduction] --> [CLAUDE API] --> CL Draft Generated
  |         |
  |    Cover Letter
  |    Approved
  |         |
  |         v
  |    [EXPORT]
  |    PDF Download Requested -----> [Puppeteer] --> PDF Rendered --> PDF Downloaded
  |    Plain Text Copied      -----> Plain Text Copied to Clipboard
  |         |
  |    Cover Letter
  |    Exported
```

### Aggregates

| Aggregate | Owns | Key Events |
|-----------|------|------------|
| CoverLetterRequest | Configuration, context, tone, length | CL Requested, Configuration Set |
| Generation | Claude API interaction, prompt construction | Generation Started, Draft Available |
| Credit | Balance, deduction | Credit Deducted |
| Export | PDF rendering, plain text formatting | PDF Rendered, Plain Text Copied |

### Policies (Automated Reactions)

| Trigger Event | Policy | Resulting Command |
|---------------|--------|-------------------|
| Cover Letter Requested | If CreditBalance < 1, show purchase prompt | Block Generation |
| Generation Started | Deduct 1 credit immediately | Update CreditBalance |
| Regenerate Requested | Show confirmation dialog with credit cost | If confirmed: Deduct + Generate |
| PDF Download Requested | Render cover letter through Puppeteer | Return PDF binary |

### Hotspots (Uncertainties / Questions)

- **HOTSPOT 1**: Should credit be deducted at generation start or at successful completion? (Risk: user pays for a failed generation)
- **HOTSPOT 2**: Should regeneration always cost a credit, or is the first regeneration in a session free?
- **HOTSPOT 3**: How does the system handle a Claude API timeout mid-generation? Refund credit automatically?
- **HOTSPOT 4**: When generating CV + CL as a bundle, does credit deduction happen atomically, or can CV succeed and CL fail (leaving a half-charged state)?
- **HOTSPOT 5**: Should company name be extracted automatically from the job description (via NLP/Claude), or always require manual entry?

---

## Part 2: User-Facing Flowchart

### Main Generation Flow

```mermaid
flowchart TD
    Start([User has generated CV]) --> ResultsPage[Results page shown\nCV preview + download buttons]
    ResultsPage --> CLButton[User clicks\n'Generate Cover Letter']
    CLButton --> CheckCredits{Credits\navailable?}

    CheckCredits -->|No| PurchasePrompt[Show purchase prompt\nwith credit options]
    PurchasePrompt --> PurchaseComplete([Purchase flow\nout of scope])

    CheckCredits -->|Yes| ContextForm[Show Cover Letter\nContext Form]
    ContextForm --> FormInputs[/Optional inputs:\nCompany name\nHiring manager name\nMotivation note\nTone selection\nLength preference/]
    FormInputs --> RegionDefaults[Apply region defaults\nTone + formality\nbased on CV country]
    RegionDefaults --> UserReady{User clicks\nGenerate?}

    UserReady -->|Adjusts settings| FormInputs
    UserReady -->|Confirms| DeductCredit[Deduct 1 credit\nfrom pool]
    DeductCredit --> GenerateAPI[Send to Claude API:\nCV data + JD + context\n+ region conventions]

    GenerateAPI --> APITimeout{API responds\nwithin timeout?}
    APITimeout -->|No| RefundCredit[Refund credit\nShow error message]
    RefundCredit --> RetryOption([User can retry])

    APITimeout -->|Yes| RenderPreview[Render CL in\npreview pane]
    RenderPreview --> UserReviews[User reads\ngenerated letter]

    UserReviews --> EditChoice{User action?}
    EditChoice -->|Inline edit| InlineEdit[User edits text\ndirectly in preview]
    InlineEdit --> UserReviews

    EditChoice -->|Regenerate| RegenConfirm{Confirm dialog:\nCosts 1 credit.\nProceed?}
    RegenConfirm -->|Cancel| UserReviews
    RegenConfirm -->|Confirm| DeductCredit

    EditChoice -->|Happy with result| ExportOptions[Show export options]
    ExportOptions --> ExportChoice{Export type?}

    ExportChoice -->|Download PDF| RenderPDF[Puppeteer renders\nCL as PDF\nmatching CV template]
    RenderPDF --> PDFDownloaded([PDF downloaded\nto user device])

    ExportChoice -->|Copy plain text| CopyText[Strip formatting\nCopy to clipboard]
    CopyText --> TextCopied([Plain text copied\nUser can paste into portals])

    ExportChoice -->|Both| BothExports[Render PDF +\nPrepare plain text]
    BothExports --> PDFDownloaded
    BothExports --> TextCopied
```

---

### Bundle Flow (CV + Cover Letter Together)

```mermaid
flowchart TD
    MainForm([User on main\nQuillCV form]) --> BundleToggle{User toggles\n'Generate CV + Cover Letter'?}
    BundleToggle -->|No toggle\nCV only| StandardCVFlow([Standard CV\ngeneration flow])
    BundleToggle -->|Bundle selected| ExtraFields[Show additional\noptional fields:\nCompany name\nTone preference]
    ExtraFields --> CreditCheck{Credit balance\n>= 2?}
    CreditCheck -->|No| PurchasePrompt([Show purchase prompt])
    CreditCheck -->|Yes| DeductTwo[Deduct 2 credits\natomically]
    DeductTwo --> ParallelGen[Generate CV and CL\nin parallel API calls]
    ParallelGen --> CVResult[CV generated]
    ParallelGen --> CLResult[CL generated]
    CVResult --> BothReady{Both\ncomplete?}
    CLResult --> BothReady
    BothReady -->|Both succeeded| ShowBoth[Show CV preview\n+ CL preview\nside by side]
    BothReady -->|CV failed| RefundTwo[Refund 2 credits\nShow error]
    BothReady -->|CL failed| RefundOne[Refund 1 credit\nShow CV only\nOffer CL retry]
    ShowBoth --> ExportBoth[Download options:\nCV PDF + CL PDF\n+ Plain text CL\n+ Combined PDF]
```

---

## Part 3: System Sequence Diagram

### Cover Letter Generation — Detailed System Interactions

```mermaid
sequenceDiagram
    actor User
    participant UI as HTMX Frontend
    participant API as FastAPI Backend
    participant CreditSvc as Credit Service
    participant CLSvc as CoverLetter Service
    participant Claude as Claude API
    participant Puppeteer as PDF Generator

    User->>UI: Click "Generate Cover Letter"
    UI->>API: GET /cover-letter/form?session_id={id}

    API->>API: Load CV data + JD from session
    API-->>UI: Render CL context form\n(pre-filled: country, role title)

    User->>UI: Fill optional fields\n(company, manager, motivation, tone, length)
    User->>UI: Click "Generate (1 credit)"

    UI->>API: POST /cover-letter/generate\n{session_id, company, manager, motivation, tone, length}

    API->>CreditSvc: check_balance(user_id)
    CreditSvc-->>API: balance: N

    alt Insufficient credits
        API-->>UI: 402 Payment Required\n{redirect: /credits/purchase}
        UI-->>User: Show purchase prompt
    else Sufficient credits
        API->>CreditSvc: deduct(user_id, amount=1, reason="cover_letter")
        CreditSvc-->>API: OK, remaining: N-1

        API->>CLSvc: generate(cv_data, job_description, options)
        CLSvc->>CLSvc: Build structured prompt\n(region conventions + tone + keywords)
        CLSvc->>Claude: POST /messages\n(prompt with CV + JD + context)

        alt Claude timeout / error
            Claude-->>CLSvc: Error / timeout
            CLSvc->>CreditSvc: refund(user_id, amount=1, reason="generation_failure")
            CLSvc-->>API: GenerationError
            API-->>UI: 500 with error message
            UI-->>User: "Generation failed. Your credit has been refunded."
        else Success
            Claude-->>CLSvc: Cover letter text
            CLSvc->>CLSvc: Post-process:\n- Inject keyword density check\n- Apply region-specific formatting\n- Add address block / date / sign-off
            CLSvc-->>API: {cover_letter_text, word_count, keywords_used}
            API-->>UI: 200 {cover_letter_html, plain_text, metadata}
            UI-->>User: Display CL preview\n(streaming if available)
        end
    end

    Note over User,UI: User reviews and optionally edits inline

    User->>UI: Click "Download PDF"
    UI->>API: POST /cover-letter/export/pdf\n{session_id, cover_letter_text}
    API->>Puppeteer: render_pdf(cover_letter_html, template_style)
    Puppeteer-->>API: PDF binary
    API-->>UI: 200 application/pdf
    UI-->>User: File download triggered

    User->>UI: Click "Copy plain text"
    UI->>UI: Copy plain_text to clipboard\n(no server call needed)
    UI-->>User: "Copied to clipboard" toast
```

---

### Credit Deduction State Diagram

```mermaid
stateDiagram-v2
    [*] --> Idle: Session opened

    Idle --> CheckingBalance: User clicks Generate
    CheckingBalance --> InsufficientFunds: balance < cost
    CheckingBalance --> Deducting: balance >= cost

    InsufficientFunds --> [*]: Show purchase prompt

    Deducting --> Generating: Deduct successful
    Generating --> Generated: Claude returns success
    Generating --> Failed: Timeout or API error
    Failed --> Refunding: Trigger refund
    Refunding --> Idle: Credit restored, show error

    Generated --> Reviewing: Preview shown to user
    Reviewing --> Regenerating: User requests regeneration
    Regenerating --> CheckingBalance: Check balance again

    Reviewing --> Exported: User downloads/copies
    Exported --> [*]: Session complete
```

---

## Part 4: Data Flow Overview

### Inputs to Cover Letter Generation

```
┌─────────────────────────────────────────────────────┐
│                SESSION DATA (already held)          │
│                                                     │
│  parsed_cv: {                                       │
│    name, contact, summary                           │
│    experience: [{title, company, dates, bullets}]   │
│    skills: [...]                                    │
│    education: [...]                                 │
│    generated_cv_text: "..." (the tailored CV output)│
│  }                                                  │
│                                                     │
│  parsed_jd: {                                       │
│    role_title, company_name (if found)              │
│    required_skills: [...]                           │
│    nice_to_have: [...]                              │
│    keywords: [...]                                  │
│    seniority_level                                  │
│    industry                                         │
│  }                                                  │
│                                                     │
│  session_meta: {                                    │
│    country_code, template_id, generated_at          │
│  }                                                  │
└─────────────────────────────────────────────────────┘
          |
          | + user-provided optional context:
          |   company_name (override), manager_name,
          |   motivation_note, tone, length_preference
          v
┌─────────────────────────────────────────────────────┐
│              CLAUDE PROMPT (structured)             │
│                                                     │
│  System: You are an expert cover letter writer...   │
│          Regional conventions for {country}...      │
│          Tone: {formal|conversational|confident}... │
│          Length target: {250|400|600} words...      │
│                                                     │
│  User:   Write a cover letter for:                  │
│          - Candidate: {cv_summary}                  │
│          - Role: {role_title} at {company_name}     │
│          - Key JD requirements: {top_keywords}      │
│          - Candidate motivation: {motivation_note}  │
│          - Reference these CV achievements: ...     │
│          - Mirror this language from the CV: ...    │
└─────────────────────────────────────────────────────┘
          |
          v
┌─────────────────────────────────────────────────────┐
│                     OUTPUTS                         │
│                                                     │
│  cover_letter_html  →  Puppeteer  →  PDF download   │
│  cover_letter_text  →  clipboard  →  Portal paste   │
│                                                     │
│  metadata: {                                        │
│    word_count, keywords_used, tone_applied          │
│    region_conventions_applied: [...]                │
│  }                                                  │
└─────────────────────────────────────────────────────┘
```

---

## Part 5: Region Convention Map

```
Country     Formality    Salutation Default        Sign-off Default     Address Block   Length Norm
─────────   ─────────    ─────────────────────     ────────────────     ─────────────   ───────────
AU          Conversational  Dear [Name] / Hi [Name] Kind regards         Optional         300-400 words
US          Confident    Dear Hiring Manager      Sincerely             Standard         250-400 words
UK          Formal       Dear Mr/Ms [Name]        Yours sincerely       Required         300-400 words
CA          Conversational  Dear [Name]           Best regards          Optional         300-400 words
NZ          Conversational  Hi [Name] / Kia ora   Ngā mihi / Kind regards Optional      250-350 words
DE          Very formal  Sehr geehrte/r [Name]    Mit freundlichen Grüßen Required      400-600 words
FR          Formal       Madame, Monsieur          Veuillez agréer...   Required        400-500 words
NL          Semi-formal  Geachte [Name]           Met vriendelijke groet Required       350-450 words
IN          Formal       Dear Mr/Ms [Name]        Regards / Warm regards Standard       300-400 words
BR          Semi-formal  Prezado/a [Name]         Atenciosamente        Standard        300-400 words
AE          Formal       Dear [Name]              Regards               Standard        300-400 words
JP          Very formal  拝啓 [formal opener]       敬具                   Required        400-600 words
```
