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
