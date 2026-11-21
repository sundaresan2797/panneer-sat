"""SAGBS company details and service descriptions in plain English."""

COMPANY = {
    "name": "Sri Annamalai Global Business Solutions",
    "short_name": "SAGBS",
    "tagline": "Your partner for data, websites and business support.",
    "locations": "Ranipet & Vellore, Tamil Nadu, India",
}

SERVICES = [
    {
        "slug": "data-entry", "title": "Data Entry Services", "short_title": "Data entry",
        "icon": "keyboard", "category": "Business records", "accent": "violet",
        "headline": "We type and organise your records.",
        "summary": "We enter details from bills, forms and documents into Excel, Google Sheets or your business system.",
        "intro": "Send us the details you need to enter. We can type them, put them in the right order and check for mistakes. You can ask for help with one job or regular work.",
        "groups": [
            ("Paper and document work", ["Copy details from PDF files into Excel or Word", "Type details from photos and scanned pages", "Turn paper records into computer files", "Type small or large amounts of information", "Name, sort and organise documents"]),
            ("Business records", ["Enter details in Excel and Google Sheets", "Enter customer and employee records", "Enter bills (invoices) and purchase orders", "Enter stock and product details"]),
            ("Regular updates", ["Add product details to online shops", "Update customer records in CRM software", "Enter contact details and sales enquiries", "Enter answers from forms and surveys"]),
        ],
        "deliverables": ["Files in the format we agree with you", "Checks for missing details and typing mistakes", "A list of details that still need your attention"],
        "tools": ["Microsoft Excel", "Google Sheets", "CRM (customer record software)"],
        "example": "You have a folder of scanned purchase orders. We enter the details in Excel so you can search them. We mark any missing details for you to check.",
        "monthly": "We can enter bills, update product lists and keep customer records up to date each month.",
    },
    {
        "slug": "data-management", "title": "Data Cleaning & Management", "short_title": "Data cleaning",
        "icon": "database-check", "category": "Business records", "accent": "teal",
        "headline": "Keep your records clean and up to date.",
        "summary": "We remove repeated entries, fix formats and bring records from different files together.",
        "intro": "Records can be hard to use when names, dates and numbers are written in different ways. We sort them, check them and note what has changed. You get files that are easier to use.",
        "groups": [
            ("Find and fix problems", ["Remove repeated entries", "Find missing details", "Check that records are correct", "Use the same format for names, dates and numbers", "Compare records and find differences"]),
            ("Work with files", ["Read and organise Excel and CSV files", "Read and change JSON and XML data files", "Bring information from several files together", "Update records in a database", "Move data into or out of a business system"]),
            ("Store and move records", ["Move records from one database to another", "Keep main customer, product and supplier lists up to date", "Sort and store older records"]),
        ],
        "deliverables": ["A clear file format and checks agreed with you", "Cleaned records and a list of problems to check", "Written steps for moving or updating your records"],
        "tools": ["Microsoft Excel", "Python", "SQL", "PostgreSQL", "MySQL"],
        "example": "Your branches have separate customer lists. We combine them, find repeated names and make the date formats match before adding the records to your customer system.",
        "monthly": "We can check your records, compare files and update your main business lists every month.",
    },
    {
        "slug": "data-analytics", "title": "Business Reports & Data Analysis", "short_title": "Business reports",
        "icon": "bar-chart-line", "category": "Reports & charts", "accent": "violet",
        "headline": "Understand your business numbers.",
        "summary": "We turn sales, costs, stock and other figures into reports and charts that are easy to read.",
        "intro": "Want to know what sold well, where costs increased or how much stock is left? We collect the figures and make useful reports. A dashboard is a screen that shows key numbers and charts in one place.",
        "groups": [
            ("Reports and dashboards", ["Study figures using advanced Excel tools", "Build Excel reports and dashboards", "Build Power BI dashboards", "Create charts you can filter and explore", "Collect records from databases using SQL", "Track key business numbers, also called KPIs"]),
            ("Reports for your team", ["Sales, income and cost reports", "Customer and stock reports", "Employee and HR reports", "Transport and delivery reports"]),
            ("Regular reports", ["Reports for business owners and managers", "Monthly reports and reports every three months", "Study past changes and estimate future trends"]),
        ],
        "deliverables": ["Agreement on the numbers and records to use", "A report, dashboard or Excel workbook", "Steps to update the report and help using it"],
        "tools": ["Microsoft Excel", "Power BI", "SQL", "Python", "Power Query", "DAX"],
        "example": "You want to compare this month’s sales, costs and stock. We bring the figures into one report so you can see changes and check anything unusual.",
        "monthly": "We can update your dashboards and prepare reports for you each month.",
    },
    {
        "slug": "bpo-services", "title": "Office Support & BPO Services", "short_title": "Office support",
        "icon": "people", "category": "Daily business help", "accent": "orange",
        "headline": "Get help with daily office work.",
        "summary": "We help with documents, orders, customer records, emails and other regular office tasks.",
        "intro": "BPO means asking an outside team to handle some of your business work. We agree on the tasks and steps with you. We keep track of the work and ask your team about anything that needs a decision.",
        "groups": [
            ("Office records", ["Help with office tasks and documents", "Process bills and purchase orders", "Update customer and supplier records", "Find business information", "Collect and check details"]),
            ("Orders and customer messages", ["Help run online shop tasks", "Process orders and update stock records", "Answer written customer messages", "Manage emails and customer support requests", "Update customer details in CRM software"]),
            ("Staff and accounts records", ["Update staff and hiring records", "Organise resumes and job applicant details", "Enter records of money to pay and money to receive", "Track business expenses"]),
        ],
        "deliverables": ["A clear list of tasks and how to do them", "Work updates and a list of issues for your team", "Regular checks at times we agree with you"],
        "tools": ["Microsoft Excel", "Google Workspace", "CRM (customer record software)", "Customer support tools"],
        "example": "We update products and orders for your online shop. If an order has a problem, we send it to your team for a decision.",
        "monthly": "We can handle regular office tasks or discuss assigning a person to work on your tasks.",
    },
    {
        "slug": "website-development", "title": "Website Development", "short_title": "Websites",
        "icon": "window-stack", "category": "Websites & software", "accent": "teal",
        "headline": "Help people find your business online.",
        "summary": "We build websites that explain your work and make it easy for people to contact you.",
        "intro": "We build websites for businesses, shops and individuals. Your site can show your services, take enquiries or sell products. We make the pages work on phones, tablets and computers.",
        "groups": [
            ("New websites", ["Company and business websites", "Websites for new businesses", "Personal websites to show your work", "Online shops", "Single pages for products, offers or events"]),
            ("Design and features", ["WordPress websites you can update", "Websites built for your needs", "New designs for existing websites", "Pages that work on phones and computers", "Contact forms and WhatsApp buttons", "Online payment setup"]),
            ("Updates and support", ["Website maintenance and content updates", "Help pages load faster", "Basic SEO to help search engines understand your site", "Help with your web address (domain) and hosting"]),
        ],
        "deliverables": ["Website pages that work on different screen sizes", "Forms and other features checked before launch", "Help putting the site online and instructions to manage it"],
        "tools": ["HTML5", "CSS3", "JavaScript", "Bootstrap", "Jinja2", "WordPress"],
        "example": "Your old website is hard to use. We rebuild it with clear service pages, a contact form and pages your customers can read on their phones.",
        "monthly": "We can update your website content, check the site and help with fixes each month.",
    },
    {
        "slug": "software-development", "title": "Business Software Development", "short_title": "Business software",
        "icon": "braces", "category": "Websites & software", "accent": "violet",
        "headline": "Software made for your daily work.",
        "summary": "We build tools to manage customers, staff, stock, bills and other business tasks.",
        "intro": "If your team uses many separate files, a single business application may help. We first understand the work, who will use the software and what it must do. Then we build and test it with you.",
        "groups": [
            ("Tools for business work", ["Web applications made for your needs", "Business management software", "CRM software to manage customers", "Staff and stock management systems", "Billing and invoice software", "ERP tools that bring business tasks together"]),
            ("Access and stored records", ["Customer login pages and staff control screens", "Databases to store and organise records", "Backend software that handles data and requests", "User login and access controls"]),
            ("Connect your tools", ["Build REST APIs so programs can share information", "Connect software to other services through APIs", "Connect online payment services"]),
        ],
        "deliverables": ["Agreement on the work the software must do", "The software, record storage and agreed connections", "Testing, help putting it online and instructions for your team"],
        "tools": ["Python", "FastAPI", "React.js", "JavaScript", "PostgreSQL", "MySQL", "MongoDB", "REST APIs"],
        "example": "Your customers need a place to send requests and see updates. We build a login area that tracks requests and lets your team assign and update the work.",
        "monthly": "We can help maintain your software, fix problems and add agreed improvements over time.",
    },
    {
        "slug": "business-automation", "title": "Task Automation & Reporting", "short_title": "Automatic tasks",
        "icon": "diagram-3", "category": "Save time on repeat work", "accent": "orange",
        "headline": "Let software do the repeated work.",
        "summary": "We help software repeat tasks such as combining files, making reports and sending reminders.",
        "intro": "Automation means setting up software to do a task by following clear steps. We check which parts can run on their own and which still need a person to check them.",
        "groups": [
            ("Files and Excel work", ["Make Excel tasks run automatically using VBA", "Use Python programs for repeated tasks", "Process PDF and Excel files automatically", "Combine details from several files"]),
            ("Reports and reminders", ["Create reports automatically", "Run reports at set times", "Send email reminders and updates", "Update Power BI reports automatically"]),
            ("Daily business tasks", ["Connect the steps in a work process", "Save form answers directly into a database", "Make repeated business tasks run automatically"]),
        ],
        "specialist": ["Using AI to read documents", "Adding AI tools to business tasks"],
        "deliverables": ["Written steps and rules for each task", "Programs or connected tools that have been tested", "Instructions and a way to handle problems"],
        "tools": ["Python", "Microsoft Excel", "VBA", "Power BI", "REST APIs"],
        "example": "Each week, your branches send Excel files. A program can combine them, mark missing details and prepare a report for your team to check.",
        "monthly": "We can help run regular reports, check automatic tasks and keep them working each month.",
    },
]

SERVICE_MAP = {service["slug"]: service for service in SERVICES}

SERVICE_GROUPS = {
    "records": {
        "title": "Records & reports", "icon": "folder2-open",
        "description": "Turn paper bills and scattered files into lists and reports you can use.",
        "slugs": ("data-entry", "data-management", "data-analytics"),
    },
    "web": {
        "title": "Websites & software", "icon": "window-sidebar",
        "description": "Show customers what you do online or build a tool for your team.",
        "slugs": ("website-development", "software-development"),
    },
    "office": {
        "title": "Daily office work", "icon": "briefcase",
        "description": "Keep up with orders, emails and jobs that repeat every week.",
        "slugs": ("bpo-services", "business-automation"),
    },
}

INDUSTRIES = [
    {"title": "Transport & delivery", "icon": "truck", "problem": "Trip details, bills and delivery updates are kept in different files.", "solution": "We can bring the records together, update delivery details and prepare cost and delivery reports.", "services": ["data-entry", "data-analytics", "business-automation"]},
    {"title": "Healthcare office work", "icon": "hospital", "problem": "Office staff spend time sorting records and making reports.", "solution": "We can enter records you allow us to use, sort documents and prepare office reports. We agree with you on how records must be handled. We do not give medical advice or provide treatment.", "services": ["data-management", "bpo-services"]},
    {"title": "Schools & training centres", "icon": "mortarboard", "problem": "Student, attendance and course details are stored in different places.", "solution": "We can organise these records, update them, make reports and build websites where people can send enquiries.", "services": ["data-entry", "software-development"]},
    {"title": "Online shops & retail", "icon": "bag", "problem": "Product lists, orders and stock records need regular updates.", "solution": "We can add products, update orders and stock, and prepare sales reports.", "services": ["bpo-services", "website-development", "data-analytics"]},
    {"title": "Factories & manufacturers", "icon": "gear-wide-connected", "problem": "Production, purchase and stock figures do not always match.", "solution": "We can check and organise records, enter purchase details and set up regular stock and work reports.", "services": ["data-management", "business-automation"]},
    {"title": "Accounts office work", "icon": "receipt", "problem": "Bills, expense records and account checks can pile up.", "solution": "We can enter bills, organise expenses and prepare figures for your accounts team. We do not offer investment advice, audits, tax certification or other financial services that need a licence.", "services": ["data-entry", "bpo-services"]},
    {"title": "Property businesses", "icon": "buildings", "problem": "Property lists and customer enquiries are hard to keep up to date.", "solution": "We can update property and customer records, build websites and help your team track follow-up work.", "services": ["website-development", "software-development"]},
    {"title": "Service businesses", "icon": "briefcase", "problem": "Staff spend time on records instead of helping customers.", "solution": "We can organise documents, help with office tasks and set up regular reports. Work that needs a qualified professional stays with your adviser.", "services": ["bpo-services", "business-automation"]},
    {"title": "New & small businesses", "icon": "rocket-takeoff", "problem": "You need help with records and online tools, but may not need a large team.", "solution": "We can start with a website, organised records or one automatic task. You can ask for more help as your work grows.", "services": ["website-development", "data-management", "software-development"]},
]

PROCESS = [
    {"title": "Tell us what you need", "icon": "chat-square-text", "desc": "Explain your work and what you want help with. You do not need to know technical terms."},
    {"title": "Agree on the work", "icon": "journal-check", "desc": "We discuss the tasks, price, time needed and how you will check the work."},
    {"title": "We do the work", "icon": "layers", "desc": "We work in steps, check the results and keep you updated."},
    {"title": "Get help when needed", "icon": "life-preserver", "desc": "We show you how to use the result. You can also discuss regular monthly help."},
]

ENGAGEMENTS = [
    {"code": "project", "title": "Help with one job", "icon": "box", "desc": "Choose this when you have a task with a clear start and finish.", "examples": "Clean a data file · Build a website · Make a report"},
    {"code": "monthly", "title": "Help every month", "icon": "calendar2-check", "desc": "Ask us to handle regular tasks. We agree on the work and when it needs to be done.", "examples": "Office tasks · Record updates · Monthly reports"},
    {"code": "dedicated", "title": "A person for your work", "icon": "person-workspace", "desc": "Talk to us about assigning a person to help with your regular tasks.", "examples": "Data entry · Office support"},
    {"code": "maintenance", "title": "Website & software care", "icon": "tools", "desc": "Get help with updates, fixes and checks after your website or software is ready.", "examples": "Website updates · Software support · Regular checks"},
]

TECHNOLOGIES = [
    {
        "title": "Keep records and make reports", "icon": "bar-chart-line",
        "example": "Turn a daily sales list into a chart that shows which months were busiest.",
        "tools": [
            ("Microsoft Excel", "Keep a list of sales, add up costs or check how much stock is left."),
            ("Google Sheets", "Let several people update the same list online."),
            ("Power Query", "Clean up files and bring them together before making a report."),
            ("SQL", "Ask a database for the records you need, such as orders from last month."),
            ("Power BI", "Turn figures into charts you can explore."),
            ("DAX", "Calculate figures for a report, such as the change in sales since last month."),
        ],
    },
    {
        "title": "Build a website or business tool", "icon": "window-sidebar",
        "example": "Give customers a page where they can read about your work and send an enquiry.",
        "tools": [
            ("HTML5 and CSS3", "Put headings, text and forms on a page and control how they look."),
            ("JavaScript", "Make a page respond when someone chooses a filter or presses a button."),
            ("Bootstrap 5", "Arrange pages so they work on phones and larger screens."),
            ("Jinja2", "Reuse a page layout and fill it with the right details for each service."),
            ("React.js", "Build interactive screens, such as a stock list that updates as you work."),
            ("Python and FastAPI", "Handle work behind the page, such as checking an enquiry before saving it."),
            ("WordPress", "Let your team edit website content without writing code."),
        ],
    },
    {
        "title": "Store and share information", "icon": "database",
        "example": "Keep customer details in one place and send order updates to another program.",
        "tools": [
            ("PostgreSQL and MySQL", "Store connected records, such as customers and their orders, in tables."),
            ("MongoDB", "Store records that can have different details, such as products with different features."),
            ("REST APIs", "Let one program ask another for information or send it an update."),
            ("CSV", "Move rows and columns between spreadsheets and other programs."),
            ("JSON and XML", "Give information a clear structure so different programs can read it."),
        ],
    },
    {
        "title": "Save time on repeated jobs", "icon": "arrow-repeat",
        "example": "Combine files from several branches each week and mark missing figures for someone to check.",
        "tools": [
            ("Python scripts", "Follow a set of steps to read files, check details and prepare a report."),
            ("VBA", "Repeat a series of steps in Excel, such as formatting a monthly workbook."),
        ],
    },
    {
        "title": "Make a website easier to follow", "icon": "layers",
        "example": "Use a clear menu symbol on a phone or bring a chart into view as someone reads.",
        "tools": [
            ("Bootstrap Icons", "Add familiar symbols for actions like opening a menu."),
            ("GSAP and ScrollTrigger", "Animate an item when it comes into view on the page."),
            ("Lenis", "Smooth the movement as someone scrolls."),
            ("Lottie", "Play small animated drawings, such as a moving check mark."),
        ],
    },
]

PROJECTS = [
    {"slug": "operations-dashboard", "title": "See delivery work in one place.", "type": "Analytics", "label": "Try a sample · Made-up data", "desc": "Choose a few months and see delivery totals, on-time deliveries and problems. These are sample figures, not customer records.", "icon": "bar-chart-line", "tools": ["JavaScript", "Reports with filters", "HTML / CSS"], "theme": "dashboard"},
    {"slug": "invoice-workflow", "title": "Find mistakes in sample bills.", "type": "Automation", "label": "Try a sample · Made-up data", "desc": "Check sample bills for repeated numbers, missing supplier names and wrong amounts. No files are sent to us, and no AI is used.", "icon": "diagram-3", "tools": ["Checks using fixed rules", "JavaScript", "CSV file download"], "theme": "workflow"},
    {"slug": "corporate-website", "title": "See this business website.", "type": "Web development", "label": "Working example · This website", "desc": "See how this website explains our services, works on phones and saves contact messages.", "icon": "window-stack", "tools": ["FastAPI", "Jinja2", "GSAP", "PostgreSQL support"], "theme": "website"},
]
PROJECT_MAP = {project["slug"]: project for project in PROJECTS}

PAGE_META = {
    "home": ("Data Entry, Websites & Business Support", "SAGBS helps with data entry, record updates, business reports, office work, websites, software and automatic tasks. Based in Ranipet and Vellore, India."),
    "about": ("About SAGBS", "Learn about Sri Annamalai Global Business Solutions. We help businesses in India and other countries with records, reports, office work, websites and software."),
    "services": ("Data Entry, Reports, Office Support & Website Services", "See seven SAGBS services: data entry, data cleaning, reports, office support and BPO, websites, business software and task automation."),
    "industries": ("Businesses We Help", "See how SAGBS can help transport companies, shops, schools, factories, healthcare offices and other businesses with records, reports and websites."),
    "technology": ("Tools We Use", "Learn what Excel, Power BI, Python, SQL and other tools do, and how SAGBS uses them for records, reports, websites, software and automatic tasks."),
    "work": ("Sample Work You Can Try", "Try a sample delivery report, check sample bills and explore this business website. Sample projects use made-up records, not customer data."),
    "contact": ("Contact SAGBS", "Call, WhatsApp or email SAGBS in Ranipet and Vellore. Tell us what help you need with records, reports, office work, websites or software."),
    "request-quote": ("Ask for a Price", "Tell SAGBS what work you need done. Ask for a price for one job or regular monthly help with records, reports, office tasks, websites or software."),
    "privacy": ("How We Use Your Details", "Read how SAGBS saves and uses your contact form details, and how you can ask to see, correct or delete them."),
}

PUBLIC_PATHS = ["/sagbs"] + [f"/sagbs/{slug}" for slug in PAGE_META if slug != "home"] + [f"/sagbs/services/{s['slug']}" for s in SERVICES] + [f"/sagbs/work/{p['slug']}" for p in PROJECTS]
