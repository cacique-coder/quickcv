"""Sample CV data for each role + region to power demo/preview pages."""

from dataclasses import dataclass


@dataclass
class DemoRole:
    id: str
    name: str
    description: str
    hero_template: str  # The template that best showcases this role


ROLES: dict[str, DemoRole] = {
    "software-engineer": DemoRole(
        id="software-engineer",
        name="Software Engineer",
        description="Mid-senior IC role — skills-forward, projects, tech stacks",
        hero_template="tech",
    ),
    "marketing-manager": DemoRole(
        id="marketing-manager",
        name="Marketing Manager",
        description="Metrics-driven marketer — campaigns, ROI, brand strategy",
        hero_template="modern",
    ),
    "financial-analyst": DemoRole(
        id="financial-analyst",
        name="Financial Analyst",
        description="Corporate finance — modelling, reporting, compliance",
        hero_template="classic",
    ),
    "vp-engineering": DemoRole(
        id="vp-engineering",
        name="VP of Engineering",
        description="Executive leadership — strategy, team building, P&L",
        hero_template="executive",
    ),
    "ux-designer": DemoRole(
        id="ux-designer",
        name="UX Designer",
        description="Design-focused — portfolio, research, user outcomes",
        hero_template="minimal",
    ),
    "project-manager": DemoRole(
        id="project-manager",
        name="Project Manager",
        description="Cross-functional delivery — Agile, stakeholders, budgets",
        hero_template="compact",
    ),
    "professor": DemoRole(
        id="professor",
        name="Professor",
        description="Academic role — publications, grants, teaching",
        hero_template="academic",
    ),
    "nurse": DemoRole(
        id="nurse",
        name="Registered Nurse",
        description="Healthcare — licenses, clinical rotations",
        hero_template="healthcare",
    ),
    "lawyer": DemoRole(
        id="lawyer",
        name="Lawyer",
        description="Legal — bar admissions, practice areas",
        hero_template="legal",
    ),
    "graphic-designer": DemoRole(
        id="graphic-designer",
        name="Graphic Designer",
        description="Creative — portfolio links, visual projects",
        hero_template="creative",
    ),
    "sales-executive": DemoRole(
        id="sales-executive",
        name="Sales Executive",
        description="Sales — quota data, revenue metrics",
        hero_template="sales",
    ),
    "graduate": DemoRole(
        id="graduate",
        name="Recent Graduate",
        description="Entry-level — coursework, internships, minimal experience",
        hero_template="clean-slate",
    ),
    "freelancer": DemoRole(
        id="freelancer",
        name="Freelancer",
        description="Contract — client-based project format",
        hero_template="freelance",
    ),
    "career-changer": DemoRole(
        id="career-changer",
        name="Career Changer",
        description="Transition — functional skills-first format",
        hero_template="career-change",
    ),
}


def list_roles() -> list[DemoRole]:
    return list(ROLES.values())


def get_role(role_id: str) -> DemoRole | None:
    return ROLES.get(role_id)


# ---------------------------------------------------------------------------
# Role base data
# ---------------------------------------------------------------------------

def _software_engineer() -> dict:
    return {
        "name": "Alex Morgan",
        "title": "Senior Software Engineer",
        "email": "alex.morgan@email.com",
        "phone": "+61 400 123 456",
        "linkedin": "linkedin.com/in/alexmorgan",
        "github": "github.com/alexmorgan",
        "portfolio": "",
        "summary": (
            "Results-driven software engineer with 8+ years of experience building "
            "scalable web applications and distributed systems. Proven track record "
            "of leading cross-functional teams, delivering projects on time, and "
            "reducing infrastructure costs by 40%. Passionate about clean code, "
            "mentoring junior developers, and continuous improvement."
        ),
        "experience": [
            {
                "title": "Senior Software Engineer",
                "company": "TechCorp",
                "location": "Sydney, Australia",
                "date": "Jan 2021 – Present",
                "tech": "Python, FastAPI, React, PostgreSQL, AWS, Docker, Kubernetes",
                "bullets": [
                    "Led migration of monolithic application to microservices, reducing deployment time by 75%",
                    "Designed and implemented real-time data pipeline processing 2M+ events/day",
                    "Mentored team of 5 junior developers through code reviews and pair programming",
                    "Reduced AWS infrastructure costs by 40% through architecture optimisation",
                ],
            },
            {
                "title": "Software Engineer",
                "company": "DataFlow Inc",
                "location": "Melbourne, Australia",
                "date": "Mar 2018 – Dec 2020",
                "tech": "Ruby on Rails, React, PostgreSQL, Redis, Heroku",
                "bullets": [
                    "Built customer-facing analytics dashboard serving 50K+ monthly active users",
                    "Implemented CI/CD pipeline reducing release cycle from 2 weeks to daily deploys",
                    "Optimised database queries resulting in 60% improvement in API response times",
                ],
            },
            {
                "title": "Junior Developer",
                "company": "StartupXYZ",
                "location": "Brisbane, Australia",
                "date": "Jun 2016 – Feb 2018",
                "tech": "Python, Django, JavaScript, MySQL",
                "bullets": [
                    "Developed RESTful APIs for mobile application with 10K+ downloads",
                    "Wrote comprehensive test suites achieving 90%+ code coverage",
                    "Collaborated with UX team to implement responsive design across 3 products",
                ],
            },
        ],
        "skills": [
            "Python", "Ruby", "JavaScript", "TypeScript", "Go",
            "FastAPI", "Django", "Rails", "React", "Next.js",
            "PostgreSQL", "Redis", "MongoDB",
            "AWS", "Docker", "Kubernetes", "Terraform",
            "CI/CD", "Git", "Agile/Scrum",
        ],
        "skills_grouped": [
            {"category": "Languages", "items": ["Python", "Ruby", "JavaScript", "TypeScript", "Go"]},
            {"category": "Frameworks", "items": ["FastAPI", "Django", "Rails", "React", "Next.js"]},
            {"category": "Databases", "items": ["PostgreSQL", "Redis", "MongoDB"]},
            {"category": "Infrastructure", "items": ["AWS", "Docker", "Kubernetes", "Terraform", "CI/CD"]},
        ],
        "education": [
            {"degree": "Bachelor of Computer Science", "institution": "University of Queensland", "date": "2012 – 2016"},
        ],
        "certifications": [
            "AWS Solutions Architect – Associate (2023)",
            "Certified Kubernetes Administrator (2022)",
        ],
        "key_achievements": [
            "Reduced infrastructure costs by $250K/year through cloud architecture redesign",
            "Led team of 8 engineers delivering a greenfield product in 6 months",
            "Achieved 99.99% uptime for critical payment processing system",
        ],
        "projects": [
            {
                "name": "OpenMetrics Dashboard",
                "url": "github.com/alexmorgan/openmetrics",
                "description": "Open-source real-time metrics visualisation tool for Kubernetes clusters",
                "tech": ["Python", "FastAPI", "React", "Prometheus", "Grafana"],
            },
        ],
    }


def _marketing_manager() -> dict:
    return {
        "name": "Sarah Chen",
        "title": "Marketing Manager",
        "email": "sarah.chen@email.com",
        "phone": "+61 412 345 678",
        "linkedin": "linkedin.com/in/sarahchen",
        "github": "",
        "portfolio": "",
        "summary": (
            "Strategic marketing manager with 7+ years driving brand growth, "
            "digital campaigns, and customer acquisition across B2B SaaS. "
            "Increased marketing-qualified leads by 180% and reduced CAC by 35% "
            "through data-driven campaign optimisation. Skilled in cross-functional "
            "leadership, content strategy, and marketing automation."
        ),
        "experience": [
            {
                "title": "Marketing Manager",
                "company": "CloudScale",
                "location": "Sydney, Australia",
                "date": "Feb 2022 – Present",
                "tech": "",
                "bullets": [
                    "Manage $1.2M annual marketing budget across paid, organic, and event channels",
                    "Increased marketing-qualified leads by 180% YoY through ABM strategy",
                    "Led rebranding initiative resulting in 45% increase in brand recognition scores",
                    "Built and managed team of 4 marketers, 2 designers, and 3 agency partners",
                    "Reduced customer acquisition cost by 35% through funnel optimisation",
                ],
            },
            {
                "title": "Digital Marketing Specialist",
                "company": "GrowthHub",
                "location": "Melbourne, Australia",
                "date": "Jun 2019 – Jan 2022",
                "tech": "",
                "bullets": [
                    "Managed Google Ads and LinkedIn campaigns with $500K+ annual spend",
                    "Achieved 4.2x ROAS across paid channels, exceeding 3x target",
                    "Created content strategy generating 120K+ monthly organic visits",
                    "Implemented HubSpot marketing automation reducing manual workflows by 60%",
                ],
            },
            {
                "title": "Marketing Coordinator",
                "company": "BrandFirst Agency",
                "location": "Brisbane, Australia",
                "date": "Jan 2017 – May 2019",
                "tech": "",
                "bullets": [
                    "Coordinated multi-channel campaigns for 12+ B2B clients simultaneously",
                    "Produced monthly analytics reports tracking KPIs across all client accounts",
                    "Managed social media presence growing combined follower base by 200%",
                ],
            },
        ],
        "skills": [
            "Digital Marketing", "SEO/SEM", "Content Strategy", "Brand Management",
            "Marketing Automation", "HubSpot", "Salesforce", "Google Analytics",
            "Google Ads", "LinkedIn Ads", "Meta Ads", "A/B Testing",
            "CRM Management", "Email Marketing", "Copywriting",
            "Budget Management", "Team Leadership", "Agile Marketing",
        ],
        "skills_grouped": [
            {"category": "Channels", "items": ["SEO/SEM", "Google Ads", "LinkedIn Ads", "Meta Ads", "Email Marketing"]},
            {"category": "Tools", "items": ["HubSpot", "Salesforce", "Google Analytics", "Hotjar", "Figma"]},
            {"category": "Strategy", "items": ["Content Strategy", "ABM", "Brand Management", "A/B Testing"]},
            {"category": "Leadership", "items": ["Team Management", "Budget Management", "Agency Management", "Agile Marketing"]},
        ],
        "education": [
            {"degree": "Bachelor of Business (Marketing)", "institution": "University of Melbourne", "date": "2013 – 2016"},
        ],
        "certifications": [
            "Google Ads Certified (2024)",
            "HubSpot Inbound Marketing Certification (2023)",
            "Meta Certified Marketing Science Professional (2023)",
        ],
        "key_achievements": [
            "Grew pipeline contribution from marketing from 30% to 55% of total revenue",
            "Launched product positioning that won 'Best B2B Campaign' at Australian Marketing Awards",
            "Built marketing ops function from scratch, reducing lead-to-SQL time by 40%",
        ],
        "projects": [],
    }


def _financial_analyst() -> dict:
    return {
        "name": "James Richardson",
        "title": "Senior Financial Analyst",
        "email": "james.richardson@email.com",
        "phone": "+61 403 567 890",
        "linkedin": "linkedin.com/in/jamesrichardson",
        "github": "",
        "portfolio": "",
        "summary": (
            "Detail-oriented financial analyst with 6+ years of experience in "
            "financial modelling, forecasting, and strategic analysis for ASX-listed "
            "companies. Track record of delivering insights that drove $15M+ in cost "
            "savings. CFA charterholder with expertise in valuation, budgeting, and "
            "regulatory compliance."
        ),
        "experience": [
            {
                "title": "Senior Financial Analyst",
                "company": "Westfield Corporation",
                "location": "Sydney, Australia",
                "date": "Mar 2021 – Present",
                "tech": "",
                "bullets": [
                    "Lead financial planning and analysis for $2.4B property portfolio across APAC",
                    "Built 3-year forecasting model reducing budget variance from 12% to 3%",
                    "Identified $8.5M in operational cost savings through variance analysis",
                    "Present quarterly financial reviews to C-suite and board of directors",
                    "Manage SOX compliance reporting across 4 business units",
                ],
            },
            {
                "title": "Financial Analyst",
                "company": "Deloitte",
                "location": "Melbourne, Australia",
                "date": "Jul 2018 – Feb 2021",
                "tech": "",
                "bullets": [
                    "Conducted due diligence for M&A transactions valued at $50M–$500M",
                    "Built DCF and comparable company valuation models for 20+ engagements",
                    "Prepared financial reports and presentations for client executive teams",
                    "Trained and supervised 3 junior analysts on modelling best practices",
                ],
            },
            {
                "title": "Graduate Analyst",
                "company": "Commonwealth Bank",
                "location": "Sydney, Australia",
                "date": "Jan 2017 – Jun 2018",
                "tech": "",
                "bullets": [
                    "Supported monthly management reporting for retail banking division ($12B revenue)",
                    "Automated recurring Excel reports saving 15 hours/month of manual work",
                    "Assisted in annual budgeting process across 6 cost centres",
                ],
            },
        ],
        "skills": [
            "Financial Modelling", "DCF Valuation", "Forecasting", "Budgeting",
            "Variance Analysis", "M&A Due Diligence", "Regulatory Compliance",
            "SOX Compliance", "Excel (Advanced)", "Power BI", "SAP",
            "SQL", "Python (pandas)", "IFRS/GAAP",
            "Board Reporting", "Stakeholder Management",
        ],
        "skills_grouped": [
            {"category": "Analysis", "items": ["Financial Modelling", "DCF Valuation", "Forecasting", "Budgeting", "Variance Analysis"]},
            {"category": "Compliance", "items": ["SOX", "IFRS/GAAP", "Regulatory Reporting", "Audit Support"]},
            {"category": "Tools", "items": ["Excel (Advanced)", "Power BI", "SAP", "SQL", "Python (pandas)"]},
            {"category": "Soft Skills", "items": ["Board Reporting", "Stakeholder Management", "Team Supervision"]},
        ],
        "education": [
            {"degree": "Master of Applied Finance", "institution": "Macquarie University", "date": "2019 – 2020"},
            {"degree": "Bachelor of Commerce (Accounting & Finance)", "institution": "University of Sydney", "date": "2013 – 2016"},
        ],
        "certifications": [
            "CFA Charterholder (2022)",
            "CPA Australia (2020)",
            "Advanced Excel & Financial Modelling — Wall Street Prep (2019)",
        ],
        "key_achievements": [
            "Delivered $15M+ in identified cost savings across two fiscal years",
            "Built forecasting model adopted as standard template across APAC division",
            "Promoted to Senior Analyst 6 months ahead of typical progression timeline",
        ],
        "projects": [],
    }


def _vp_engineering() -> dict:
    return {
        "name": "David Nakamura",
        "title": "Vice President of Engineering",
        "email": "david.nakamura@email.com",
        "phone": "+61 401 234 567",
        "linkedin": "linkedin.com/in/davidnakamura",
        "github": "",
        "portfolio": "",
        "summary": (
            "Engineering executive with 15+ years of experience scaling technology "
            "organisations from 20 to 200+ engineers. Led platform modernisation "
            "initiatives generating $40M+ in annual revenue. Proven ability to align "
            "engineering strategy with business objectives, build high-performing teams, "
            "and drive operational excellence across distributed organisations."
        ),
        "experience": [
            {
                "title": "VP of Engineering",
                "company": "Nexus Technologies",
                "location": "Sydney, Australia",
                "date": "Jan 2020 – Present",
                "tech": "",
                "bullets": [
                    "Lead 120+ engineers across 14 squads delivering core platform serving 5M+ users",
                    "Grew engineering org from 45 to 120 while maintaining 92% retention rate",
                    "Drove platform migration from legacy monolith to cloud-native architecture (AWS/K8s)",
                    "Reduced time-to-market by 60% through DevOps transformation and CI/CD maturity",
                    "Managed $18M annual engineering budget with full P&L accountability",
                    "Established engineering career ladder and promoted 15 engineers to senior/staff level",
                ],
            },
            {
                "title": "Director of Engineering",
                "company": "PayRight",
                "location": "Melbourne, Australia",
                "date": "Mar 2016 – Dec 2019",
                "tech": "",
                "bullets": [
                    "Built and led 6 engineering teams (55 engineers) for fintech payment platform",
                    "Delivered PCI-DSS Level 1 compliance enabling $2B+ in annual transaction volume",
                    "Launched mobile payments product contributing $12M ARR within first year",
                    "Implemented OKR framework aligning engineering output to business goals",
                    "Reduced critical incident response time from 4 hours to 15 minutes",
                ],
            },
            {
                "title": "Engineering Manager",
                "company": "Atlassian",
                "location": "Sydney, Australia",
                "date": "Jun 2012 – Feb 2016",
                "tech": "",
                "bullets": [
                    "Managed 3 teams (18 engineers) on Jira Cloud infrastructure",
                    "Led migration to microservices architecture reducing deployment failures by 80%",
                    "Shipped 4 major features contributing to 25% growth in enterprise accounts",
                    "Established on-call rotation and incident management process for 99.95% SLA",
                ],
            },
            {
                "title": "Senior Software Engineer",
                "company": "ThoughtWorks",
                "location": "Melbourne, Australia",
                "date": "Jan 2009 – May 2012",
                "tech": "",
                "bullets": [
                    "Led technical delivery for 3 enterprise consulting engagements ($5M+ combined)",
                    "Championed agile practices and TDD across client organisations",
                ],
            },
        ],
        "skills": [
            "Engineering Leadership", "Organisational Design", "Strategic Planning",
            "P&L Management", "Talent Acquisition", "Team Building",
            "Cloud Architecture", "Platform Engineering", "DevOps",
            "Agile/SAFe", "OKRs", "Stakeholder Management",
            "M&A Technical Due Diligence", "Vendor Management",
        ],
        "skills_grouped": [
            {"category": "Leadership", "items": ["Org Design", "P&L Management", "Talent Acquisition", "Mentoring", "OKRs"]},
            {"category": "Strategy", "items": ["Technical Roadmapping", "M&A Due Diligence", "Vendor Management", "Budget Planning"]},
            {"category": "Technical", "items": ["Cloud Architecture", "Platform Engineering", "DevOps", "Security/Compliance"]},
        ],
        "education": [
            {"degree": "MBA (Technology Management)", "institution": "Melbourne Business School", "date": "2014 – 2016"},
            {"degree": "Bachelor of Software Engineering", "institution": "University of Melbourne", "date": "2005 – 2008"},
        ],
        "certifications": [
            "AWS Certified Solutions Architect – Professional (2021)",
            "SAFe Program Consultant (SPC) (2020)",
        ],
        "key_achievements": [
            "Scaled engineering org from 45 to 120 engineers with 92% retention",
            "Platform modernisation drove $40M+ annual revenue and 60% faster delivery",
            "Built engineering brand attracting top talent — 4.5/5 Glassdoor engineering rating",
        ],
        "projects": [],
    }


def _ux_designer() -> dict:
    return {
        "name": "Mia Torres",
        "title": "Senior UX Designer",
        "email": "mia.torres@email.com",
        "phone": "+61 422 345 678",
        "linkedin": "linkedin.com/in/miatorres",
        "github": "",
        "portfolio": "miatorres.design",
        "summary": (
            "User-centred designer with 6+ years crafting intuitive digital experiences "
            "for web and mobile products. Specialising in research-driven design, "
            "design systems, and accessibility. Increased user task completion rates "
            "by 40% and reduced support tickets by 55% through evidence-based redesigns."
        ),
        "experience": [
            {
                "title": "Senior UX Designer",
                "company": "HealthTech Co",
                "location": "Sydney, Australia",
                "date": "Apr 2022 – Present",
                "tech": "",
                "bullets": [
                    "Lead UX for patient-facing health platform with 800K+ active users",
                    "Conducted 60+ user interviews and usability tests informing product roadmap",
                    "Redesigned onboarding flow increasing completion rate from 45% to 82%",
                    "Built and maintained design system (120+ components) used across 4 product teams",
                    "Reduced customer support tickets by 55% through UX improvements to self-service flows",
                ],
            },
            {
                "title": "UX Designer",
                "company": "FinApp Studio",
                "location": "Melbourne, Australia",
                "date": "Jan 2020 – Mar 2022",
                "tech": "",
                "bullets": [
                    "Designed end-to-end mobile banking experience for 200K+ users",
                    "Created interactive prototypes tested with 30+ participants per sprint",
                    "Improved Net Promoter Score from 32 to 58 through iterative design improvements",
                    "Collaborated with engineering to ensure WCAG 2.1 AA accessibility compliance",
                ],
            },
            {
                "title": "Junior UX Designer",
                "company": "Digital Agency Co",
                "location": "Brisbane, Australia",
                "date": "Jun 2018 – Dec 2019",
                "tech": "",
                "bullets": [
                    "Produced wireframes, user flows, and prototypes for 15+ client projects",
                    "Assisted in user research including surveys (1,000+ respondents) and card sorting",
                    "Delivered responsive designs for e-commerce platform generating $4M annual GMV",
                ],
            },
        ],
        "skills": [
            "User Research", "Usability Testing", "Interaction Design",
            "Design Systems", "Information Architecture", "Wireframing",
            "Prototyping", "Accessibility (WCAG)", "Visual Design",
            "Figma", "Sketch", "Adobe XD", "Miro", "Hotjar",
            "HTML/CSS", "Design Thinking", "Agile/Scrum",
        ],
        "skills_grouped": [
            {"category": "Research", "items": ["User Interviews", "Usability Testing", "Surveys", "Card Sorting", "Analytics"]},
            {"category": "Design", "items": ["Interaction Design", "Visual Design", "Design Systems", "Information Architecture"]},
            {"category": "Tools", "items": ["Figma", "Sketch", "Adobe XD", "Miro", "Hotjar", "HTML/CSS"]},
            {"category": "Methods", "items": ["Design Thinking", "Agile/Scrum", "Accessibility (WCAG 2.1)", "A/B Testing"]},
        ],
        "education": [
            {"degree": "Bachelor of Design (Interaction Design)", "institution": "University of Technology Sydney", "date": "2014 – 2017"},
        ],
        "certifications": [
            "Google UX Design Professional Certificate (2022)",
            "IAAP Web Accessibility Specialist (WAS) (2023)",
            "Interaction Design Foundation — UX Management (2021)",
        ],
        "key_achievements": [
            "Redesigned onboarding flow increasing completion from 45% to 82%",
            "Built design system adopted across 4 product teams (120+ components)",
            "Improved NPS from 32 to 58 through iterative user-centred design",
        ],
        "projects": [],
    }


def _project_manager() -> dict:
    return {
        "name": "Rachel Kim",
        "title": "Senior Project Manager",
        "email": "rachel.kim@email.com",
        "phone": "+61 433 456 789",
        "linkedin": "linkedin.com/in/rachelkim",
        "github": "",
        "portfolio": "",
        "summary": (
            "PMP-certified project manager with 9+ years delivering complex technology "
            "and business transformation projects. Successfully managed $50M+ in combined "
            "project portfolios across financial services, healthcare, and government sectors. "
            "Expert in Agile, hybrid, and waterfall methodologies with a track record of "
            "on-time, on-budget delivery."
        ),
        "experience": [
            {
                "title": "Senior Project Manager",
                "company": "Accenture",
                "location": "Sydney, Australia",
                "date": "May 2021 – Present",
                "tech": "",
                "bullets": [
                    "Manage portfolio of 5 concurrent projects ($12M combined budget, 60+ team members)",
                    "Delivered ERP migration for government client — $8M budget, 18-month timeline, on time",
                    "Implemented Agile transformation across 3 client organisations (200+ stakeholders)",
                    "Achieved 95% client satisfaction score across all managed engagements",
                    "Established PMO standards and templates adopted across ANZ practice",
                ],
            },
            {
                "title": "Project Manager",
                "company": "Suncorp Group",
                "location": "Brisbane, Australia",
                "date": "Feb 2018 – Apr 2021",
                "tech": "",
                "bullets": [
                    "Led digital transformation program for insurance claims platform ($6M budget)",
                    "Reduced claims processing time from 14 days to 3 days through process redesign",
                    "Managed cross-functional team of 25 across IT, operations, and business units",
                    "Delivered 12 projects over 3 years with 100% on-budget track record",
                ],
            },
            {
                "title": "Associate Project Manager",
                "company": "IBM",
                "location": "Melbourne, Australia",
                "date": "Jul 2015 – Jan 2018",
                "tech": "",
                "bullets": [
                    "Coordinated delivery of cloud migration project for banking client (500+ VMs)",
                    "Managed project schedules, risk registers, and status reporting for 4 workstreams",
                    "Facilitated weekly steering committees with client CIO and programme sponsors",
                    "Mentored 2 junior PMs through IBM's project management development programme",
                ],
            },
        ],
        "skills": [
            "Project Management", "Programme Management", "PMO",
            "Agile/Scrum", "SAFe", "Waterfall", "Hybrid Methodology",
            "Stakeholder Management", "Risk Management", "Budget Management",
            "Jira", "Confluence", "MS Project", "Smartsheet",
            "Change Management", "Vendor Management", "Resource Planning",
            "PRINCE2", "PMP",
        ],
        "skills_grouped": [
            {"category": "Methodologies", "items": ["Agile/Scrum", "SAFe", "Waterfall", "Hybrid", "PRINCE2"]},
            {"category": "Management", "items": ["Stakeholder Management", "Risk Management", "Budget Management", "Vendor Management"]},
            {"category": "Tools", "items": ["Jira", "Confluence", "MS Project", "Smartsheet", "Power BI"]},
            {"category": "Domains", "items": ["Digital Transformation", "Cloud Migration", "ERP", "Insurance", "Government"]},
        ],
        "education": [
            {"degree": "Master of Project Management", "institution": "University of Sydney", "date": "2017 – 2018"},
            {"degree": "Bachelor of Information Technology", "institution": "Queensland University of Technology", "date": "2011 – 2014"},
        ],
        "certifications": [
            "PMP — Project Management Professional (2019)",
            "PRINCE2 Practitioner (2018)",
            "Certified SAFe Agilist (SA) (2022)",
            "ITIL v4 Foundation (2020)",
        ],
        "key_achievements": [
            "Delivered $50M+ in project portfolios with 100% on-budget track record",
            "Reduced insurance claims processing from 14 days to 3 days",
            "95% client satisfaction score across all managed engagements",
        ],
        "projects": [],
    }


def _professor() -> dict:
    return {
        "name": "Dr. Sarah Williams",
        "title": "Associate Professor of Computer Science",
        "email": "s.williams@university.edu",
        "phone": "+61 402 345 678",
        "linkedin": "linkedin.com/in/sarahwilliamscs",
        "github": "github.com/swilliams-cs",
        "portfolio": "",
        "summary": (
            "Associate Professor of Computer Science with 12+ years in academia, "
            "specialising in machine learning and natural language processing. "
            "Published 35+ peer-reviewed papers (h-index 22) and secured over "
            "$2.4M in competitive research funding. Passionate about bridging "
            "industry and academia through applied research and mentoring the "
            "next generation of researchers."
        ),
        "experience": [
            {
                "title": "Associate Professor",
                "company": "University of Queensland",
                "location": "Brisbane, Australia",
                "date": "Jan 2020 – Present",
                "tech": "",
                "bullets": [
                    "Lead the NLP & Applied ML research group (8 PhD students, 3 postdocs)",
                    "Secured $1.8M ARC Discovery Grant for explainable AI research programme",
                    "Published 12 papers in top-tier venues (NeurIPS, ACL, EMNLP) since 2020",
                    "Redesigned postgraduate ML curriculum adopted by 3 partner universities",
                    "Supervised 6 PhD completions with 100% employment placement rate",
                ],
            },
            {
                "title": "Senior Lecturer",
                "company": "University of Melbourne",
                "location": "Melbourne, Australia",
                "date": "Mar 2016 – Dec 2019",
                "tech": "",
                "bullets": [
                    "Taught undergraduate and postgraduate courses (200+ students/semester)",
                    "Co-authored textbook 'Applied Machine Learning' adopted by 15+ institutions",
                    "Established industry partnership programme with 4 tech companies",
                    "Received Faculty Teaching Excellence Award (2018)",
                ],
            },
            {
                "title": "Postdoctoral Research Fellow",
                "company": "Stanford University",
                "location": "Stanford, CA, USA",
                "date": "Jun 2013 – Feb 2016",
                "tech": "",
                "bullets": [
                    "Conducted research in deep learning for biomedical text mining",
                    "Published 8 papers with 1,200+ citations",
                    "Collaborated with Stanford NLP Group on open-source toolkit development",
                ],
            },
        ],
        "skills": [
            "Machine Learning", "Natural Language Processing", "Deep Learning",
            "Research Leadership", "Grant Writing", "Python", "PyTorch",
            "TensorFlow", "Statistical Analysis", "Academic Publishing",
            "Curriculum Design", "PhD Supervision", "Peer Review",
        ],
        "skills_grouped": [
            {"category": "Research", "items": ["Machine Learning", "NLP", "Deep Learning", "Statistical Analysis"]},
            {"category": "Technical", "items": ["Python", "PyTorch", "TensorFlow", "R", "LaTeX"]},
            {"category": "Academic", "items": ["Grant Writing", "Curriculum Design", "PhD Supervision", "Peer Review"]},
        ],
        "education": [
            {"degree": "PhD in Computer Science", "institution": "University of Melbourne", "date": "2009 – 2013"},
            {"degree": "Master of Computer Science", "institution": "University of Sydney", "date": "2007 – 2008"},
            {"degree": "Bachelor of Computer Science (Honours)", "institution": "University of Queensland", "date": "2003 – 2006"},
        ],
        "certifications": [],
        "key_achievements": [
            "Secured $2.4M+ in competitive research funding across 5 grants",
            "35+ publications with h-index of 22 and 3,500+ total citations",
            "Faculty Teaching Excellence Award (2018)",
        ],
        "projects": [],
        "publications": [
            "Williams, S., Chen, L., & Park, J. (2023). 'Explainable Transformers for Biomedical Text Classification.' NeurIPS 2023.",
            "Williams, S. & Rodriguez, A. (2022). 'Cross-Lingual Transfer Learning for Low-Resource NLP.' ACL 2022, pp. 1234–1245.",
            "Park, J., Williams, S., et al. (2021). 'Attention-Based Models for Clinical Note Summarisation.' EMNLP 2021.",
            "Williams, S. (2020). 'A Survey of Pre-trained Language Models for Domain-Specific Applications.' Journal of Machine Learning Research, 21(1), pp. 1–42.",
        ],
        "grants": [
            "ARC Discovery Grant — Explainable AI for Healthcare — $1,800,000 — 2021",
            "Google Research Scholar Award — NLP for Accessibility — $80,000 — 2022",
            "University Strategic Research Fund — Cross-Lingual NLP — $520,000 — 2019",
        ],
        "teaching": [
            {"course": "COMP7505 — Advanced Machine Learning", "institution": "University of Queensland", "date": "2020"},
            {"course": "COMP4702 — Machine Learning", "institution": "University of Queensland", "date": "2021"},
            {"course": "COMP3710 — Natural Language Processing", "institution": "University of Melbourne", "date": "2017"},
        ],
        "conferences": [
            "Keynote Speaker — Australasian Language Technology Workshop (ALTA) — 2023",
            "Invited Talk — Google Research Sydney — 'Explainability in NLP' — 2022",
            "Oral Presentation — NeurIPS 2023, New Orleans, USA",
        ],
    }


def _nurse() -> dict:
    return {
        "name": "Emily Johnson",
        "title": "Registered Nurse — Intensive Care Unit",
        "email": "emily.johnson@email.com",
        "phone": "+61 411 234 567",
        "linkedin": "linkedin.com/in/emilyjohnsonrn",
        "github": "",
        "portfolio": "",
        "summary": (
            "Dedicated Registered Nurse with 6+ years of experience in critical care "
            "and intensive care settings. Skilled in ventilator management, haemodynamic "
            "monitoring, and rapid patient assessment. Committed to evidence-based practice "
            "and compassionate patient-centred care. Experienced preceptor with a track "
            "record of mentoring graduate nurses through ICU transition programmes."
        ),
        "experience": [
            {
                "title": "Registered Nurse — ICU",
                "company": "Royal Prince Alfred Hospital",
                "location": "Sydney, Australia",
                "date": "Mar 2021 – Present",
                "tech": "",
                "bullets": [
                    "Provide critical care nursing for 12-bed ICU with 1:1 and 1:2 patient ratios",
                    "Manage patients on mechanical ventilation, CRRT, and intra-aortic balloon pumps",
                    "Precept 8+ graduate nurses through 6-month ICU transition programme",
                    "Led implementation of early mobility protocol reducing ICU length of stay by 1.8 days",
                    "Participate in rapid response and code blue teams across 600-bed facility",
                ],
            },
            {
                "title": "Registered Nurse — Medical/Surgical",
                "company": "St Vincent's Hospital",
                "location": "Melbourne, Australia",
                "date": "Jan 2019 – Feb 2021",
                "tech": "",
                "bullets": [
                    "Managed care for up to 6 patients on busy 32-bed medical/surgical ward",
                    "Administered medications, IV therapy, and wound care to post-surgical patients",
                    "Coordinated discharge planning with multidisciplinary healthcare teams",
                    "Achieved 98% medication administration accuracy across 2-year tenure",
                ],
            },
        ],
        "skills": [
            "Critical Care Nursing", "Ventilator Management", "Haemodynamic Monitoring",
            "ECG Interpretation", "IV Therapy", "Wound Management",
            "Patient Assessment", "Medication Administration", "Care Planning",
            "Infection Control", "Electronic Health Records", "Team Leadership",
        ],
        "skills_grouped": [
            {"category": "Clinical", "items": ["Critical Care", "Ventilator Management", "Haemodynamic Monitoring", "ECG Interpretation"]},
            {"category": "Procedures", "items": ["IV Therapy", "Wound Management", "Medication Administration", "Blood Transfusion"]},
            {"category": "Professional", "items": ["Patient Assessment", "Care Planning", "Infection Control", "Preceptorship"]},
        ],
        "education": [
            {"degree": "Bachelor of Nursing", "institution": "University of Technology Sydney", "date": "2015 – 2018"},
        ],
        "certifications": [
            "Graduate Certificate in Critical Care Nursing — University of Sydney (2022)",
        ],
        "key_achievements": [
            "Led early mobility protocol reducing ICU length of stay by 1.8 days",
            "Precepted 8+ graduate nurses with 100% programme completion rate",
            "98% medication administration accuracy over 2-year tenure",
        ],
        "projects": [],
        "licenses": [
            "Registered Nurse — AHPRA — NMW0002345678 — Expires Dec 2026",
            "Basic Life Support (BLS) — Australian Resuscitation Council — Current",
            "Advanced Cardiovascular Life Support (ACLS) — ARC — Expires Jun 2026",
        ],
        "clinical_experience": [
            {"role": "Student Nurse — ICU Placement", "facility": "Westmead Hospital", "date": "Jul 2017 – Oct 2017", "description": "120-hour clinical placement in 20-bed ICU, assisted with ventilated patient care and haemodynamic monitoring"},
            {"role": "Student Nurse — Emergency Dept Placement", "facility": "Royal North Shore Hospital", "date": "Feb 2017 – May 2017", "description": "100-hour placement in Level 1 trauma centre, triaged patients and assisted in resuscitation bays"},
            {"role": "Student Nurse — Aged Care Placement", "facility": "HammondCare", "date": "Aug 2016 – Nov 2016", "description": "80-hour placement providing holistic care for elderly residents including medication rounds and wound care"},
        ],
    }


def _lawyer() -> dict:
    return {
        "name": "Michael Chen",
        "title": "Senior Associate — Corporate & Commercial Law",
        "email": "michael.chen@email.com",
        "phone": "+61 404 567 890",
        "linkedin": "linkedin.com/in/michaelchenlaw",
        "github": "",
        "portfolio": "",
        "summary": (
            "Senior Associate with 8+ years of experience in corporate and commercial "
            "law, specialising in mergers & acquisitions, private equity, and cross-border "
            "transactions. Advised on deals valued at over $3B collectively. Recognised "
            "by Chambers Asia-Pacific as an 'Associate to Watch' and committed to "
            "delivering commercially pragmatic legal solutions."
        ),
        "experience": [
            {
                "title": "Senior Associate — Corporate & M&A",
                "company": "King & Wood Mallesons",
                "location": "Sydney, Australia",
                "date": "Feb 2021 – Present",
                "tech": "",
                "bullets": [
                    "Lead deal teams on M&A and private equity transactions valued at $50M–$1.2B",
                    "Advised ASX-listed clients on takeovers, schemes of arrangement, and capital raisings",
                    "Drafted and negotiated share purchase agreements, shareholders agreements, and joint ventures",
                    "Managed due diligence processes across 15+ transactions coordinating teams of 8–12 lawyers",
                    "Mentored 4 junior lawyers and supervised 6 summer clerks across 3 intakes",
                ],
            },
            {
                "title": "Associate — Corporate",
                "company": "Herbert Smith Freehills",
                "location": "Melbourne, Australia",
                "date": "Mar 2018 – Jan 2021",
                "tech": "",
                "bullets": [
                    "Acted on cross-border M&A transactions across Australia, Southeast Asia, and Europe",
                    "Advised private equity funds on portfolio acquisitions and exit strategies",
                    "Prepared ASIC and ASX regulatory filings and disclosure documents",
                    "Recognised in Chambers Asia-Pacific 2020 as 'Associate to Watch — Corporate/M&A'",
                ],
            },
            {
                "title": "Graduate Lawyer",
                "company": "Herbert Smith Freehills",
                "location": "Melbourne, Australia",
                "date": "Feb 2017 – Feb 2018",
                "tech": "",
                "bullets": [
                    "Rotated through Corporate, Disputes, and Employment practice groups",
                    "Conducted legal research and drafted client memoranda on regulatory matters",
                    "Assisted on pro bono matters including refugee visa applications",
                ],
            },
        ],
        "skills": [
            "Mergers & Acquisitions", "Private Equity", "Corporate Advisory",
            "Due Diligence", "Contract Negotiation", "Capital Markets",
            "Regulatory Compliance", "Cross-Border Transactions",
            "Stakeholder Management", "Legal Research", "Client Advisory",
        ],
        "skills_grouped": [
            {"category": "Transactional", "items": ["M&A", "Private Equity", "Capital Markets", "Joint Ventures"]},
            {"category": "Advisory", "items": ["Corporate Governance", "Regulatory Compliance", "ASIC/ASX Filings"]},
            {"category": "Drafting", "items": ["SPAs", "Shareholders Agreements", "Due Diligence Reports", "Board Resolutions"]},
        ],
        "education": [
            {"degree": "Juris Doctor", "institution": "University of Melbourne", "date": "2014 – 2016"},
            {"degree": "Bachelor of Commerce (Finance)", "institution": "University of Sydney", "date": "2010 – 2013"},
        ],
        "certifications": [
            "Admitted to Supreme Court of New South Wales (2017)",
            "Admitted to High Court of Australia (2017)",
            "Graduate Diploma of Legal Practice — College of Law (2016)",
        ],
        "key_achievements": [
            "Advised on transactions valued at $3B+ collectively",
            "Chambers Asia-Pacific 'Associate to Watch' — Corporate/M&A (2020)",
            "Led due diligence for largest deal in firm's APAC PE practice (FY2023)",
        ],
        "projects": [],
        "bar_admissions": [
            "Supreme Court of New South Wales — 2017",
            "High Court of Australia — 2017",
        ],
        "practice_areas": [
            "Mergers & Acquisitions",
            "Private Equity",
            "Capital Markets",
            "Corporate Governance",
            "Cross-Border Transactions",
        ],
        "case_highlights": [
            {"case_type": "Public M&A — Scheme of Arrangement", "outcome": "Successful $1.2B acquisition completed", "description": "Advised ASX-listed target on contested scheme of arrangement involving competing proposals from two international bidders"},
            {"case_type": "Private Equity Buyout", "outcome": "Deal closed — $380M enterprise value", "description": "Led transaction for PE fund acquiring majority stake in Australian healthcare group, including complex vendor due diligence"},
            {"case_type": "Cross-Border Joint Venture", "outcome": "JV operational within 6 months", "description": "Structured and documented 50/50 JV between Australian mining company and Singapore-based investor for Indonesian operations"},
        ],
    }


def _graphic_designer() -> dict:
    return {
        "name": "Luna Patel",
        "title": "Senior Graphic Designer",
        "email": "luna.patel@email.com",
        "phone": "+61 421 567 890",
        "linkedin": "linkedin.com/in/lunapatel",
        "github": "",
        "portfolio": "lunapatel.design",
        "summary": (
            "Creative and detail-oriented Senior Graphic Designer with 5+ years of "
            "experience delivering compelling visual identities, marketing materials, "
            "and digital assets for brands ranging from startups to ASX-listed corporations. "
            "Skilled in brand strategy, print and digital design, and motion graphics. "
            "Passionate about translating complex ideas into beautiful, functional design."
        ),
        "experience": [
            {
                "title": "Senior Graphic Designer",
                "company": "BrandWorks Studio",
                "location": "Sydney, Australia",
                "date": "Jun 2022 – Present",
                "tech": "",
                "bullets": [
                    "Lead visual design for 8+ client accounts generating $2M+ annual revenue",
                    "Created complete brand identities (logo, typography, colour systems) for 15+ brands",
                    "Designed marketing collateral driving 35% increase in client engagement metrics",
                    "Mentored 2 junior designers through portfolio development and skill building",
                    "Produced motion graphics and social media content with 2M+ combined impressions",
                ],
            },
            {
                "title": "Graphic Designer",
                "company": "Creative Pulse Agency",
                "location": "Melbourne, Australia",
                "date": "Jan 2020 – May 2022",
                "tech": "",
                "bullets": [
                    "Designed print and digital campaigns for clients in tech, hospitality, and retail",
                    "Produced packaging designs for FMCG brand achieving 20% sales uplift post-redesign",
                    "Collaborated with copywriters and strategists on integrated marketing campaigns",
                    "Managed production pipeline for 30+ concurrent projects using Asana",
                ],
            },
            {
                "title": "Junior Graphic Designer",
                "company": "PixelCraft",
                "location": "Brisbane, Australia",
                "date": "Mar 2019 – Dec 2019",
                "tech": "",
                "bullets": [
                    "Created social media graphics, email templates, and web banners for 10+ clients",
                    "Assisted senior designers with large-scale branding and print projects",
                    "Maintained brand consistency across all deliverables and client touchpoints",
                ],
            },
        ],
        "skills": [
            "Brand Identity", "Visual Design", "Typography", "Colour Theory",
            "Print Design", "Digital Design", "Motion Graphics", "Packaging Design",
            "Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "Adobe After Effects",
            "Figma", "Sketch", "Canva", "Art Direction",
        ],
        "skills_grouped": [
            {"category": "Design", "items": ["Brand Identity", "Typography", "Colour Theory", "Layout", "Art Direction"]},
            {"category": "Adobe Suite", "items": ["Photoshop", "Illustrator", "InDesign", "After Effects", "Premiere Pro"]},
            {"category": "Digital", "items": ["Figma", "Sketch", "Canva", "Motion Graphics", "Social Media Design"]},
            {"category": "Print", "items": ["Packaging Design", "Large Format", "Offset Printing", "Pre-press"]},
        ],
        "education": [
            {"degree": "Bachelor of Design (Visual Communication)", "institution": "RMIT University", "date": "2015 – 2018"},
        ],
        "certifications": [
            "Adobe Certified Professional — Illustrator (2023)",
            "Google UX Design Certificate (2022)",
        ],
        "key_achievements": [
            "Brand identity work contributed to client winning 'Best New Brand' at Australian Design Awards",
            "Packaging redesign drove 20% sales uplift for FMCG client within 3 months",
            "2M+ social media impressions on motion graphics content produced in 2023",
        ],
        "projects": [],
        "portfolio_links": [
            {"title": "Nova Coffee — Brand Identity", "url": "https://lunapatel.design/nova-coffee", "description": "Complete brand identity including logo, packaging, and store signage for specialty coffee chain"},
            {"title": "TechStart Conference — Event Branding", "url": "https://lunapatel.design/techstart", "description": "Event branding, stage design, and digital assets for 2,000-attendee tech conference"},
            {"title": "GreenLeaf Organics — Packaging", "url": "https://lunapatel.design/greenleaf", "description": "Sustainable packaging design for organic food brand achieving 20% sales uplift"},
            {"title": "MindWell App — UI Design", "url": "https://lunapatel.design/mindwell", "description": "UI design and illustration for mental health app with 50K+ downloads"},
        ],
        "brand_statement": (
            "I believe design is a conversation between brand and audience. My work "
            "bridges strategic thinking with visual craft, creating identities that "
            "resonate emotionally while driving measurable business outcomes."
        ),
    }


def _sales_executive() -> dict:
    return {
        "name": "Tom Bradley",
        "title": "Regional Sales Director — APAC",
        "email": "tom.bradley@email.com",
        "phone": "+61 408 901 234",
        "linkedin": "linkedin.com/in/tombradleysales",
        "github": "",
        "portfolio": "",
        "summary": (
            "High-performing Regional Sales Director with 10+ years of experience "
            "driving revenue growth across enterprise SaaS and technology markets in "
            "APAC. Consistently exceeded quota by 120%+, generating $45M+ in cumulative "
            "revenue. Proven ability to build and scale sales teams, develop strategic "
            "partnerships, and close complex enterprise deals with C-suite stakeholders."
        ),
        "experience": [
            {
                "title": "Regional Sales Director — APAC",
                "company": "CloudPlatform Inc",
                "location": "Sydney, Australia",
                "date": "Jan 2021 – Present",
                "tech": "",
                "bullets": [
                    "Lead 12-person sales team across AU, NZ, and SEA generating $18M ARR",
                    "Exceeded annual quota by 135% in FY2024, earning President's Club recognition",
                    "Closed largest deal in APAC history — $4.2M 3-year enterprise agreement",
                    "Grew APAC revenue from $8M to $18M (125% growth) over 3 years",
                    "Implemented MEDDIC sales methodology increasing win rates from 22% to 38%",
                ],
            },
            {
                "title": "Senior Account Executive",
                "company": "SalesForceOne",
                "location": "Melbourne, Australia",
                "date": "Mar 2017 – Dec 2020",
                "tech": "",
                "bullets": [
                    "Managed portfolio of 40+ enterprise accounts ($6M+ annual quota)",
                    "Achieved 128% quota attainment averaged across 4 years",
                    "Developed strategic account plans resulting in 3 seven-figure expansions",
                    "Built relationships with C-suite executives at ASX 100 companies",
                ],
            },
            {
                "title": "Account Executive",
                "company": "TechVentures",
                "location": "Brisbane, Australia",
                "date": "Jun 2014 – Feb 2017",
                "tech": "",
                "bullets": [
                    "Exceeded first-year quota by 115%, promoted to Senior AE within 18 months",
                    "Built pipeline of $4M+ through outbound prospecting and networking events",
                    "Closed 60+ mid-market deals with average contract value of $85K",
                ],
            },
        ],
        "skills": [
            "Enterprise Sales", "Strategic Account Management", "Revenue Growth",
            "MEDDIC", "Consultative Selling", "Pipeline Management",
            "C-Suite Engagement", "Contract Negotiation", "Team Leadership",
            "Salesforce", "Gong", "Sales Navigator", "Clari",
            "Forecasting", "Partner Channel Development",
        ],
        "skills_grouped": [
            {"category": "Sales", "items": ["Enterprise Sales", "MEDDIC", "Consultative Selling", "Negotiation"]},
            {"category": "Leadership", "items": ["Team Management", "Coaching", "Revenue Planning", "Forecasting"]},
            {"category": "Tools", "items": ["Salesforce", "Gong", "Clari", "Sales Navigator", "Outreach"]},
        ],
        "education": [
            {"degree": "Bachelor of Business (Marketing)", "institution": "Queensland University of Technology", "date": "2010 – 2013"},
        ],
        "certifications": [
            "MEDDIC Certified Sales Professional (2021)",
            "Sandler Sales Certification (2019)",
            "Salesforce Certified Administrator (2020)",
        ],
        "key_achievements": [
            "Grew APAC revenue from $8M to $18M (125% growth) in 3 years",
            "President's Club winner 3 consecutive years (FY2022–FY2024)",
            "Closed largest APAC deal in company history — $4.2M enterprise agreement",
        ],
        "projects": [],
        "quota_metrics": [
            {"period": "FY2024", "target": "$14M", "achieved": "$18.9M", "percentage": "135%"},
            {"period": "FY2023", "target": "$12M", "achieved": "$15.6M", "percentage": "130%"},
            {"period": "FY2022", "target": "$10M", "achieved": "$12.2M", "percentage": "122%"},
        ],
    }


def _graduate() -> dict:
    return {
        "name": "Aisha Rahman",
        "title": "Computer Science Graduate",
        "email": "aisha.rahman@email.com",
        "phone": "+61 423 456 789",
        "linkedin": "linkedin.com/in/aisharahman",
        "github": "github.com/aisharahman",
        "portfolio": "",
        "summary": (
            "Recent Computer Science graduate with strong foundations in software "
            "development, algorithms, and data structures. Completed a 6-month "
            "internship building production features for a fintech startup. Eager to "
            "contribute to a collaborative engineering team and grow as a full-stack "
            "developer."
        ),
        "experience": [
            {
                "title": "Software Engineering Intern",
                "company": "PayTech Startup",
                "location": "Sydney, Australia",
                "date": "Jul 2025 – Dec 2025",
                "tech": "Python, Django, React, PostgreSQL",
                "bullets": [
                    "Built transaction history dashboard used by 5,000+ customers daily",
                    "Implemented REST API endpoints for payment reconciliation module",
                    "Wrote unit and integration tests achieving 85% code coverage on new features",
                    "Participated in Agile ceremonies including sprint planning and retrospectives",
                ],
            },
        ],
        "skills": [
            "Python", "Java", "JavaScript", "React", "Django",
            "PostgreSQL", "Git", "Docker", "REST APIs",
            "Data Structures", "Algorithms", "Agile/Scrum",
        ],
        "skills_grouped": [
            {"category": "Languages", "items": ["Python", "Java", "JavaScript", "SQL"]},
            {"category": "Frameworks", "items": ["Django", "React", "Flask"]},
            {"category": "Tools", "items": ["Git", "Docker", "VS Code", "Jira"]},
        ],
        "education": [
            {
                "degree": "Bachelor of Computer Science",
                "institution": "University of New South Wales",
                "date": "2023 – 2025",
            },
        ],
        "certifications": [],
        "key_achievements": [
            "Dean's List — 2 consecutive semesters (GPA 3.8/4.0)",
            "Winner — University Hackathon 2025 (AI-powered accessibility tool)",
        ],
        "projects": [
            {
                "name": "StudyBuddy",
                "url": "github.com/aisharahman/studybuddy",
                "description": "AI-powered study planner that generates revision schedules from lecture notes",
                "tech": ["Python", "FastAPI", "React", "OpenAI API"],
            },
            {
                "name": "EcoTrack",
                "url": "github.com/aisharahman/ecotrack",
                "description": "Carbon footprint calculator with personalised reduction suggestions",
                "tech": ["JavaScript", "Node.js", "MongoDB", "Chart.js"],
            },
        ],
    }


def _freelancer() -> dict:
    return {
        "name": "Chris Navarro",
        "title": "Freelance Full-Stack Developer",
        "email": "chris@navarro.dev",
        "phone": "+61 415 678 901",
        "linkedin": "linkedin.com/in/chrisnavarro",
        "github": "github.com/chrisnavarro",
        "portfolio": "navarro.dev",
        "summary": (
            "Freelance Full-Stack Developer with 7+ years building web applications, "
            "e-commerce platforms, and SaaS products for clients across Australia, the US, "
            "and Europe. Delivered 50+ projects ranging from MVPs to enterprise platforms. "
            "Specialising in React, Node.js, and cloud architecture with a focus on "
            "clean code, performance, and scalability."
        ),
        "experience": [
            {
                "title": "Freelance Full-Stack Developer",
                "company": "Self-Employed",
                "location": "Sydney, Australia (Remote)",
                "date": "Jan 2019 – Present",
                "tech": "React, Next.js, Node.js, TypeScript, AWS, PostgreSQL",
                "bullets": [
                    "Delivered 35+ client projects across e-commerce, SaaS, and fintech verticals",
                    "Maintained 100% client satisfaction with average project rating of 4.9/5",
                    "Built and deployed production applications handling 100K+ monthly users",
                    "Managed full project lifecycle from scoping through deployment and maintenance",
                    "Generated $180K+ annual revenue as solo practitioner",
                ],
            },
            {
                "title": "Software Developer",
                "company": "Digital Agency Co",
                "location": "Melbourne, Australia",
                "date": "Mar 2017 – Dec 2018",
                "tech": "Ruby on Rails, React, PostgreSQL, Heroku",
                "bullets": [
                    "Built web applications for 15+ agency clients across diverse industries",
                    "Developed reusable component library reducing development time by 30%",
                    "Collaborated with designers and project managers in Agile team of 8",
                ],
            },
        ],
        "skills": [
            "React", "Next.js", "Node.js", "TypeScript", "Python",
            "Ruby on Rails", "PostgreSQL", "MongoDB", "Redis",
            "AWS", "Vercel", "Docker", "CI/CD",
            "REST APIs", "GraphQL", "Stripe", "Shopify",
        ],
        "skills_grouped": [
            {"category": "Frontend", "items": ["React", "Next.js", "TypeScript", "Tailwind CSS", "HTML/CSS"]},
            {"category": "Backend", "items": ["Node.js", "Python", "Ruby on Rails", "GraphQL", "REST APIs"]},
            {"category": "Infrastructure", "items": ["AWS", "Vercel", "Docker", "CI/CD", "PostgreSQL", "MongoDB"]},
            {"category": "Integrations", "items": ["Stripe", "Shopify", "SendGrid", "Twilio", "Auth0"]},
        ],
        "education": [
            {"degree": "Bachelor of Information Technology", "institution": "RMIT University", "date": "2013 – 2016"},
        ],
        "certifications": [
            "AWS Certified Developer — Associate (2022)",
            "Shopify Partner Certification (2021)",
        ],
        "key_achievements": [
            "Delivered 50+ projects with 100% client satisfaction rating",
            "Built e-commerce platform processing $2M+ annually for retail client",
            "Generated $180K+ annual freelance revenue as solo practitioner",
        ],
        "projects": [
            {
                "name": "FreshCart — E-Commerce Platform",
                "url": "navarro.dev/freshcart",
                "description": "Custom Shopify Plus storefront with subscription management, processing $2M+ annually",
                "tech": ["Next.js", "Shopify API", "Stripe", "Vercel"],
            },
            {
                "name": "TradeFlow — SaaS Dashboard",
                "url": "navarro.dev/tradeflow",
                "description": "Real-time trading analytics platform for commodity brokers with 500+ daily active users",
                "tech": ["React", "Node.js", "WebSocket", "PostgreSQL", "AWS"],
            },
            {
                "name": "HealthBook — Appointment System",
                "url": "navarro.dev/healthbook",
                "description": "Multi-tenant appointment booking system for 30+ medical practices",
                "tech": ["Ruby on Rails", "React", "Twilio", "Heroku"],
            },
            {
                "name": "GreenBuild — Carbon Calculator",
                "url": "navarro.dev/greenbuild",
                "description": "Carbon footprint calculator for construction companies with PDF report generation",
                "tech": ["Python", "FastAPI", "React", "Docker"],
            },
            {
                "name": "LegalEase — Document Automation",
                "url": "navarro.dev/legalease",
                "description": "Contract generation and e-signature platform for small law firms",
                "tech": ["Next.js", "Node.js", "DocuSign API", "MongoDB"],
            },
        ],
        "availability": "Available for new projects",
    }


def _career_changer() -> dict:
    return {
        "name": "Diana Foster",
        "title": "UX Designer (Transitioning from Education)",
        "email": "diana.foster@email.com",
        "phone": "+61 419 012 345",
        "linkedin": "linkedin.com/in/dianafosterux",
        "github": "",
        "portfolio": "dianafoster.design",
        "summary": (
            "UX Designer transitioning from 10 years in education, bringing deep "
            "expertise in user empathy, curriculum design, and data-driven iteration. "
            "Completed intensive UX bootcamp and delivered 4 end-to-end design projects. "
            "Unique ability to translate complex requirements into intuitive, accessible "
            "experiences informed by years of understanding diverse learner needs."
        ),
        "experience": [
            {
                "title": "UX Designer (Contract)",
                "company": "EduTech Solutions",
                "location": "Sydney, Australia",
                "date": "Sep 2025 – Present",
                "tech": "",
                "bullets": [
                    "Designing student onboarding flow for learning management platform (40K+ users)",
                    "Conducted 15 user interviews and usability tests with students and educators",
                    "Created interactive prototypes in Figma tested across 3 iteration cycles",
                    "Reduced user onboarding drop-off by 25% through evidence-based redesign",
                ],
            },
            {
                "title": "Head of Curriculum & Teaching",
                "company": "Riverside Secondary College",
                "location": "Melbourne, Australia",
                "date": "Jan 2018 – Jun 2025",
                "tech": "",
                "bullets": [
                    "Led curriculum redesign for 1,200-student school improving NAPLAN results by 15%",
                    "Designed and facilitated 50+ professional development workshops for 80 staff",
                    "Managed $200K annual curriculum budget and vendor relationships",
                    "Analysed student performance data to drive evidence-based teaching strategies",
                    "Created accessible learning materials for students with diverse needs",
                ],
            },
            {
                "title": "English & Humanities Teacher",
                "company": "Bayside Grammar School",
                "location": "Melbourne, Australia",
                "date": "Feb 2015 – Dec 2017",
                "tech": "",
                "bullets": [
                    "Taught classes of 25–30 students across Years 7–12",
                    "Developed engaging lesson plans aligned to Victorian curriculum standards",
                    "Achieved highest student satisfaction scores in English department (2017)",
                ],
            },
        ],
        "skills": [
            "UX Design", "User Research", "Usability Testing", "Wireframing",
            "Prototyping", "Figma", "Information Architecture", "Accessibility",
            "Curriculum Design", "Workshop Facilitation", "Data Analysis",
            "Stakeholder Management", "Empathy Mapping", "Design Thinking",
        ],
        "skills_grouped": [
            {"category": "UX Design", "items": ["User Research", "Usability Testing", "Wireframing", "Prototyping", "Information Architecture"]},
            {"category": "Tools", "items": ["Figma", "Miro", "Maze", "Hotjar", "Google Analytics"]},
            {"category": "Transferable", "items": ["Curriculum Design", "Workshop Facilitation", "Data Analysis", "Stakeholder Management", "Accessibility"]},
        ],
        "education": [
            {"degree": "UX Design Immersive Bootcamp", "institution": "General Assembly", "date": "2025"},
            {"degree": "Master of Teaching (Secondary)", "institution": "University of Melbourne", "date": "2013 – 2014"},
            {"degree": "Bachelor of Arts (English & Psychology)", "institution": "Monash University", "date": "2009 – 2012"},
        ],
        "certifications": [
            "Google UX Design Professional Certificate (2025)",
            "Interaction Design Foundation — UX Management (2025)",
        ],
        "key_achievements": [
            "Reduced onboarding drop-off by 25% in first UX contract role",
            "Led curriculum redesign improving NAPLAN results by 15% across 1,200 students",
            "Designed 50+ professional development workshops with 95%+ satisfaction ratings",
            "Created accessible learning materials adopted across 3 schools in network",
        ],
        "projects": [
            {
                "name": "MindfulMe — Mental Health App",
                "url": "dianafoster.design/mindfulme",
                "description": "End-to-end UX design for teen mental health app (bootcamp capstone project)",
                "tech": ["Figma", "Maze", "User Research"],
            },
            {
                "name": "CommunityHub — Neighbourhood Platform",
                "url": "dianafoster.design/communityhub",
                "description": "Redesigned local community platform improving task completion rate by 40%",
                "tech": ["Figma", "Hotjar", "Usability Testing"],
            },
        ],
    }


# ---------------------------------------------------------------------------
# Role getter
# ---------------------------------------------------------------------------

_ROLE_DATA = {
    "software-engineer": _software_engineer,
    "marketing-manager": _marketing_manager,
    "financial-analyst": _financial_analyst,
    "vp-engineering": _vp_engineering,
    "ux-designer": _ux_designer,
    "project-manager": _project_manager,
    "professor": _professor,
    "nurse": _nurse,
    "lawyer": _lawyer,
    "graphic-designer": _graphic_designer,
    "sales-executive": _sales_executive,
    "graduate": _graduate,
    "freelancer": _freelancer,
    "career-changer": _career_changer,
}


# ---------------------------------------------------------------------------
# Region adaptation
# ---------------------------------------------------------------------------

_REGION_PHONES = {
    "AU": "+61 400 123 456", "US": "+1 (555) 123-4567", "UK": "+44 7700 900123",
    "CA": "+1 (416) 555-0123", "NZ": "+64 21 123 4567", "DE": "+49 170 1234567",
    "FR": "+33 6 12 34 56 78", "NL": "+31 6 1234 5678", "IN": "+91 98765 43210",
    "BR": "+55 11 98765-4321", "AE": "+971 50 123 4567", "JP": "+81 90-1234-5678",
}

_REGION_CITIES = {
    "AU": ["Sydney", "Melbourne", "Brisbane"],
    "US": ["San Francisco, CA", "Austin, TX", "New York, NY"],
    "UK": ["London", "Manchester", "Bristol"],
    "CA": ["Toronto, ON", "Vancouver, BC", "Montreal, QC"],
    "NZ": ["Auckland", "Wellington", "Christchurch"],
    "DE": ["Berlin", "Munich", "Hamburg"],
    "FR": ["Paris", "Lyon", "Toulouse"],
    "NL": ["Amsterdam", "Rotterdam", "Utrecht"],
    "IN": ["Bangalore", "Hyderabad", "Pune"],
    "BR": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"],
    "AE": ["Dubai", "Abu Dhabi", "Sharjah"],
    "JP": ["Tokyo", "Osaka", "Fukuoka"],
}

_REGION_COUNTRY = {
    "AU": "Australia", "US": "USA", "UK": "UK", "CA": "Canada", "NZ": "New Zealand",
    "DE": "Germany", "FR": "France", "NL": "Netherlands", "IN": "India",
    "BR": "Brazil", "AE": "UAE", "JP": "Japan",
}

_REGION_UNIS = {
    "AU": ["University of Queensland", "University of Melbourne", "University of Sydney"],
    "US": ["UC Berkeley", "MIT", "Stanford University"],
    "UK": ["University College London", "Imperial College London", "University of Edinburgh"],
    "CA": ["University of Toronto", "UBC", "McGill University"],
    "NZ": ["University of Auckland", "Victoria University of Wellington", "University of Canterbury"],
    "DE": ["TU Berlin", "TU Munich", "University of Heidelberg"],
    "FR": ["École Polytechnique", "HEC Paris", "Université Paris-Saclay"],
    "NL": ["Delft University of Technology", "University of Amsterdam", "Erasmus University Rotterdam"],
    "IN": ["IIT Bombay", "IIT Delhi", "IIM Ahmedabad"],
    "BR": ["Universidade de São Paulo (USP)", "Unicamp", "UFRJ"],
    "AE": ["American University of Sharjah", "University of Dubai", "NYU Abu Dhabi"],
    "JP": ["University of Tokyo", "Kyoto University", "Osaka University"],
}


def _apply_region(data: dict, region_code: str) -> dict:
    """Adapt base role data to regional conventions."""
    data["region"] = region_code
    data["phone"] = _REGION_PHONES.get(region_code, data["phone"])

    # Swap city names
    cities = _REGION_CITIES.get(region_code, _REGION_CITIES["AU"])
    country = _REGION_COUNTRY.get(region_code, "")
    for i, job in enumerate(data["experience"]):
        city = cities[i % len(cities)]
        if "," in city:  # Already has state/country
            job["location"] = city
        else:
            job["location"] = f"{city}, {country}"

    # Swap university
    unis = _REGION_UNIS.get(region_code, _REGION_UNIS["AU"])
    for i, edu in enumerate(data["education"]):
        edu["institution"] = unis[i % len(unis)]

    # American English for US/CA
    if region_code in ("US", "CA"):
        _americanize(data)

    # References for AU, NZ, NL, IN, AE
    if region_code in ("AU", "NZ", "NL", "IN", "AE"):
        data["references"] = [
            {"name": "Jane Smith", "title": "Director", "company": data["experience"][0]["company"],
             "contact": f"jane.smith@company.com | {_REGION_PHONES.get(region_code, '')}"},
            {"name": "John Doe", "title": "CTO", "company": data["experience"][1]["company"],
             "contact": f"john.doe@company.com | {_REGION_PHONES.get(region_code, '')}"},
        ]

    # DOB for DE, NL, IN, BR, AE, JP
    if region_code == "DE":
        data["dob"] = "15.03.1990"
        data["nationality"] = "Australian"
        data["languages"] = ["English (Native)", "German (B2)"]
    elif region_code == "NL":
        data["dob"] = "15-03-1990"
    elif region_code in ("IN",):
        data["dob"] = "15/03/1990"
        data["nationality"] = "Indian"
        data["marital_status"] = "Single"
        data["languages"] = ["English (Fluent)", "Hindi (Native)", "Tamil (Conversational)"]
    elif region_code == "BR":
        data["dob"] = "15/03/1990"
        data["nationality"] = "Brasileiro(a)"
        data["marital_status"] = "Solteiro(a)"
    elif region_code == "AE":
        data["dob"] = "15/03/1990"
        data["nationality"] = "Australian"
        data["marital_status"] = "Single"
        data["visa_status"] = "Employment Visa — Transferable"
        data["availability"] = "Immediate"
    elif region_code == "JP":
        data["dob"] = "1990/03/15"
        data["nationality"] = "Australian"
        data["marital_status"] = "Unmarried"
        data["dependents"] = "0"
        data["visa_status"] = "Engineer/Specialist in Humanities Visa"
    elif region_code == "FR":
        data["languages"] = ["English (Native)", "French (B2)"]
    elif region_code == "CA":
        data["languages"] = ["English (Native)", "French (Professional)"]

    return data


def _americanize(data: dict) -> None:
    """Convert British English spelling to American English."""
    replacements = {
        "optimisation": "optimization", "optimised": "optimized",
        "organisation": "organization", "organisations": "organizations",
        "organising": "organizing", "organised": "organized",
        "specialising": "specializing", "modernisation": "modernization",
        "colour": "color", "behaviour": "behavior",
        "programme": "program", "programmes": "programs",
        "centre": "center", "centres": "centers",
        "modelling": "modeling", "travelling": "traveling",
        "licence": "license", "defence": "defense",
        "catalogue": "catalog", "manoeuvre": "maneuver",
        "analyse": "analyze", "analysed": "analyzed",
        "recognise": "recognize", "recognised": "recognized",
        "summarise": "summarize", "summarised": "summarized",
        "visualisation": "visualization",
        "user-centred": "user-centered", "centred": "centered",
    }

    def _replace(text: str) -> str:
        for uk, us in replacements.items():
            text = text.replace(uk, us)
        return text

    if "summary" in data:
        data["summary"] = _replace(data["summary"])
    for job in data.get("experience", []):
        job["bullets"] = [_replace(b) for b in job.get("bullets", [])]
    for ach in data.get("key_achievements", []):
        idx = data["key_achievements"].index(ach)
        data["key_achievements"][idx] = _replace(ach)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def get_demo_data(region_code: str, role_id: str = "software-engineer") -> dict:
    """Return sample CV data for a role adapted to a specific region."""
    factory = _ROLE_DATA.get(role_id, _software_engineer)
    data = factory()
    return _apply_region(data, region_code)
