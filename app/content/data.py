"""
Central bilingual content store for the site.

Templates are written once per page type (templates/pages/*.html) and are
rendered twice — once under /en/ and once under /ta/ — by pulling the copy
for the requested language out of this module. This keeps the HTML in one
place (no duplicated markup between languages) while every route still gets
its own real, translated content and its own URL.
"""

SITE = {
    "company_name": "Sri Annamalayar Transport & Logistics",
    "phones": ["8248454617", "8838259156"],
    "whatsapp_number": None,  # [TO BE CONFIRMED] — see BUSINESS_DETAILS_TO_CONFIRM.md
    "email": None,  # [TO BE CONFIRMED]
    "gstin": "33DLKPK2599N1ZD",
    "office_address": [
        "No. 97, SIDCO Industrial Estate,",
        "SIPCOT, Ranipet,",
        "Ranipet Taluk,",
        "Ranipet District,",
        "Tamil Nadu – 632403, India.",
    ],
    "transport_address": [
        "No. 86, Anna Nagar,",
        "Sathiram Pudhur,",
        "Vellore, Tamil Nadu.",
    ],
    "hours": [
        ("Monday", "9:00 AM – 9:00 PM"),
        ("Tuesday", "9:00 AM – 9:00 PM"),
        ("Wednesday", "9:00 AM – 9:00 PM"),
        ("Thursday", "9:00 AM – 9:00 PM"),
        ("Friday", "9:00 AM – 9:00 PM"),
        ("Saturday", "9:00 AM – 9:00 PM"),
        ("Sunday", "Closed"),
    ],
    "lunch": "1:00 PM – 2:00 PM",
}

NAV = {
    "en": [
        ("Home", "/en/"),
        ("About", "/en/about"),
        ("Services", "/en/services"),
        ("Industries", "/en/industries"),
        ("Gallery", "/en/gallery"),
        ("Reviews", "/en/reviews"),
        ("Contact", "/en/contact"),
    ],
    "ta": [
        ("முகப்பு", "/ta/"),
        ("எங்களைப் பற்றி", "/ta/about"),
        ("சேவைகள்", "/ta/services"),
        ("தொழில்கள்", "/ta/industries"),
        ("கேலரி", "/ta/gallery"),
        ("கருத்துகள்", "/ta/reviews"),
        ("தொடர்பு", "/ta/contact"),
    ],
}

SERVICES_DROPDOWN = {
    "en": [
        ("Manpower Supply", "/en/manpower"),
        ("Facility Management", "/en/facility-management"),
        ("Transport & Logistics", "/en/transport"),
        ("Heavy Vehicle Rental", "/en/heavy-vehicle-rental"),
    ],
    "ta": [
        ("மனிதவள சப்ளை", "/ta/manpower"),
        ("Facility Management", "/ta/facility-management"),
        ("போக்குவரத்து & லாஜிஸ்டிக்ஸ்", "/ta/transport"),
        ("கனரக வாகன வாடகை", "/ta/heavy-vehicle-rental"),
    ],
}

UI = {
    "en": {
        "lang_label": "EN",
        "other_lang_label": "தமிழ்",
        "request_quote": "Request a Quote",
        "call_us": "Call Us",
        "whatsapp": "WhatsApp",
        "explore_services": "Explore Our Services",
        "learn_more": "Learn More",
        "read_more": "Read More",
        "go_home": "Go Home",
        "contact_us": "Contact Us",
        "call_now": "Call Now",
        "submit": "Submit Requirement",
        "submitting": "Submitting...",
        "submit_success": "Your enquiry has been submitted successfully.",
        "submit_error": "Something went wrong. Please call us directly.",
        "required": "required",
        "quote_bar_label": "Quote",
        "call_bar_label": "Call",
        "whatsapp_bar_label": "WhatsApp",
        "back_to_top": "Back to top",
        "all_label": "All",
    },
    "ta": {
        "lang_label": "தமிழ்",
        "other_lang_label": "EN",
        "request_quote": "விலை விவரம் கேட்க",
        "call_us": "தொடர்பு கொள்ள",
        "whatsapp": "WhatsApp",
        "explore_services": "எங்கள் சேவைகள்",
        "learn_more": "மேலும் அறிய",
        "read_more": "மேலும் படிக்க",
        "go_home": "முகப்புக்கு செல்ல",
        "contact_us": "தொடர்பு கொள்ள",
        "call_now": "இப்போது அழைக்க",
        "submit": "கோரிக்கையை அனுப்பவும்",
        "submitting": "அனுப்பப்படுகிறது...",
        "submit_success": "உங்கள் கோரிக்கை வெற்றிகரமாக அனுப்பப்பட்டது.",
        "submit_error": "ஏதோ தவறு நேர்ந்தது. தயவுசெய்து எங்களை நேரடியாக அழைக்கவும்.",
        "required": "அவசியம்",
        "quote_bar_label": "விலை",
        "call_bar_label": "அழைக்க",
        "whatsapp_bar_label": "WhatsApp",
        "back_to_top": "மேலே செல்ல",
        "all_label": "அனைத்தும்",
    },
}

FOOTER = {
    "en": {
        "tagline": "Reliable workforce, facility management and transportation solutions for businesses and industries.",
        "company_col": "Company",
        "services_col": "Services",
        "contact_col": "Contact",
        "language_col": "Language",
        "copyright": "© 2026 Sri Annamalayar Transport & Logistics. All Rights Reserved.",
    },
    "ta": {
        "tagline": "நிறுவனங்கள் மற்றும் தொழிற்சாலைகளுக்கான நம்பகமான மனிதவளம், Facility Management மற்றும் போக்குவரத்து தீர்வுகள்.",
        "company_col": "நிறுவனம்",
        "services_col": "சேவைகள்",
        "contact_col": "தொடர்பு",
        "language_col": "மொழி",
        "copyright": "© 2026 Sri Annamalayar Transport & Logistics. அனைத்து உரிமைகளும் பாதுகாக்கப்பட்டவை.",
    },
}

WHATSAPP_MESSAGES = {
    "en": {
        "general": "Hello Sri Annamalayar Transport & Logistics, I would like to enquire about your services.",
        "quote": "Hello, I would like to request a quote for your services.",
    },
    "ta": {
        "general": "வணக்கம் Sri Annamalayar Transport & Logistics, உங்கள் சேவைகள் குறித்து விசாரிக்க விரும்புகிறேன்.",
        "quote": "வணக்கம், உங்கள் சேவைகளுக்கான விலை விவரம் தெரிந்துகொள்ள விரும்புகிறேன்.",
    },
}

# ---------------------------------------------------------------------------
# Shared building blocks used across multiple pages
# ---------------------------------------------------------------------------

TRUST_STRIP = {
    "en": ["5+ Years Experience", "Manpower Solutions", "Facility Management", "Transport Services", "Heavy Vehicle Rental"],
    "ta": ["5+ ஆண்டுகள் அனுபவம்", "மனிதவள தீர்வுகள்", "Facility Management", "போக்குவரத்து சேவைகள்", "கனரக வாகன வாடகை"],
}

SERVICE_CARDS = {
    "en": [
        {
            "icon": "people",
            "image": "/static/images/services/manpower.jpg",
            "image_alt": "Sri Annamalayar Transport & Logistics manpower team at an industrial site",
            "title": "Manpower Supply",
            "desc": "Reliable workforce solutions based on your operational requirements.",
            "points": ["Skilled", "Semi-skilled", "Unskilled", "ITI", "Diploma", "Degree", "Administrative"],
            "cta": "Explore Manpower Services",
            "link": "/en/manpower",
        },
        {
            "icon": "building",
            "image": "/static/images/services/facility.jpg",
            "image_alt": "Sri Annamalayar facility management team — housekeeping and gardening staff",
            "title": "Facility Management",
            "desc": "Professional workforce support for housekeeping, cleaning, gardening and facility operations.",
            "points": ["Housekeeping", "Professional Cleaning", "Gardening", "Facility Support"],
            "cta": "Explore Facility Services",
            "link": "/en/facility-management",
        },
        {
            "icon": "truck",
            "image": "/static/images/services/transport.jpg",
            "image_alt": "Sri Annamalayar transport and logistics vehicles at a warehouse",
            "title": "Transport & Logistics",
            "desc": "Transportation solutions for corporate, workforce, goods and commercial requirements.",
            "points": ["Corporate Transport", "Workforce Transport", "Goods Transport", "Commercial Logistics"],
            "cta": "Explore Transport Services",
            "link": "/en/transport",
        },
        {
            "icon": "tipper",
            "image": "/static/images/services/heavy-vehicle.jpg",
            "image_alt": "10-wheeler tipper trucks on an industrial site — Sri Annamalayar heavy vehicle rental",
            "title": "Heavy Vehicle Rental",
            "desc": "Heavy vehicle solutions for commercial and industrial requirements.",
            "points": ["10-Wheeler Tipper Trucks", "Bharat Benz", "U-Truck"],
            "cta": "Explore Vehicle Rental",
            "link": "/en/heavy-vehicle-rental",
        },
    ],
    "ta": [
        {
            "icon": "people",
            "image": "/static/images/services/manpower.jpg",
            "image_alt": "தொழிற்சாலை தளத்தில் Sri Annamalayar மனிதவள குழு",
            "title": "மனிதவள சப்ளை",
            "desc": "உங்கள் நிறுவனத்தின் செயல்பாட்டு தேவைகளுக்கு ஏற்ப நம்பகமான மனிதவள தீர்வுகள்.",
            "points": ["Skilled", "Semi-skilled", "Unskilled", "ITI", "Diploma", "Degree", "நிர்வாக பணியாளர்கள்"],
            "cta": "மனிதவள சேவைகளை காண",
            "link": "/ta/manpower",
        },
        {
            "icon": "building",
            "image": "/static/images/services/facility.jpg",
            "image_alt": "Sri Annamalayar Facility Management குழு — Housekeeping மற்றும் Gardening பணியாளர்கள்",
            "title": "Facility Management",
            "desc": "Housekeeping, cleaning, gardening மற்றும் Facility பணிகளுக்கான தொழில்முறை பணியாளர் ஆதரவு.",
            "points": ["Housekeeping", "Professional Cleaning", "Gardening", "Facility Support"],
            "cta": "Facility சேவைகளை காண",
            "link": "/ta/facility-management",
        },
        {
            "icon": "truck",
            "image": "/static/images/services/transport.jpg",
            "image_alt": "Warehouse-இல் Sri Annamalayar போக்குவரத்து வாகனங்கள்",
            "title": "போக்குவரத்து & லாஜிஸ்டிக்ஸ்",
            "desc": "Corporate, workforce, goods மற்றும் commercial தேவைகளுக்கான போக்குவரத்து தீர்வுகள்.",
            "points": ["Corporate Transport", "Workforce Transport", "Goods Transport", "Commercial Logistics"],
            "cta": "போக்குவரத்து சேவைகளை காண",
            "link": "/ta/transport",
        },
        {
            "icon": "tipper",
            "image": "/static/images/services/heavy-vehicle.jpg",
            "image_alt": "தொழில்துறை தளத்தில் 10-Wheeler Tipper வாகனங்கள் — Sri Annamalayar கனரக வாகன வாடகை",
            "title": "கனரக வாகன வாடகை",
            "desc": "வணிக மற்றும் தொழில் தேவைகளுக்கான கனரக வாகன தீர்வுகள்.",
            "points": ["10-Wheeler Tipper Trucks", "Bharat Benz", "U-Truck"],
            "cta": "வாகன வாடகையை காண",
            "link": "/ta/heavy-vehicle-rental",
        },
    ],
}

CAPABILITY_CARDS = {
    "en": [
        {"title": "Workforce Solutions", "desc": "Skilled, semi-skilled and unskilled manpower support."},
        {"title": "Facility Support", "desc": "Housekeeping, cleaning, gardening and facility workforce."},
        {"title": "Corporate Transportation", "desc": "Transportation solutions for organizations and workforce."},
        {"title": "Commercial Logistics", "desc": "Support for goods and commercial transportation requirements."},
        {"title": "Heavy Vehicles", "desc": "Heavy vehicle and tipper rental solutions."},
        {"title": "Flexible Service Support", "desc": "Solutions designed around customer requirements."},
    ],
    "ta": [
        {"title": "மனிதவள தீர்வுகள்", "desc": "Skilled, semi-skilled மற்றும் unskilled மனிதவள ஆதரவு."},
        {"title": "Facility ஆதரவு", "desc": "Housekeeping, cleaning, gardening மற்றும் facility பணியாளர் ஆதரவு."},
        {"title": "Corporate போக்குவரத்து", "desc": "நிறுவனங்கள் மற்றும் பணியாளர்களுக்கான போக்குவரத்து தீர்வுகள்."},
        {"title": "வணிக Logistics", "desc": "பொருட்கள் மற்றும் வணிக போக்குவரத்து தேவைகளுக்கான ஆதரவு."},
        {"title": "கனரக வாகனங்கள்", "desc": "கனரக வாகனம் மற்றும் டிப்பர் வாடகை தீர்வுகள்."},
        {"title": "நெகிழ்வான சேவை ஆதரவு", "desc": "வாடிக்கையாளர் தேவைகளுக்கு ஏற்ப வடிவமைக்கப்பட்ட தீர்வுகள்."},
    ],
}

INDUSTRY_CARDS = {
    "en": ["Automotive", "Manufacturing", "Industrial", "Logistics", "Warehousing", "Corporate", "Infrastructure", "Commercial"],
    "ta": ["Automotive", "உற்பத்தி (Manufacturing)", "தொழில்துறை", "Logistics", "Warehousing", "Corporate", "Infrastructure", "வணிகம்"],
}

WHY_CHOOSE_US = {
    "en": [
        {"num": "01", "title": "Experience", "desc": "More than 5 years of experience."},
        {"num": "02", "title": "Reliable Workforce", "desc": "Workforce solutions based on customer requirements."},
        {"num": "03", "title": "Professional Service", "desc": "Customer-focused approach."},
        {"num": "04", "title": "Operational Support", "desc": "Practical workforce, facility and transportation support."},
        {"num": "05", "title": "Safety Focus", "desc": "Focus on safe and responsible service."},
        {"num": "06", "title": "Timely Service", "desc": "Understanding the importance of timely business operations."},
    ],
    "ta": [
        {"num": "01", "title": "அனுபவம்", "desc": "5+ ஆண்டுகளுக்கும் மேலான அனுபவம்."},
        {"num": "02", "title": "நம்பகமான மனிதவளம்", "desc": "வாடிக்கையாளர் தேவைக்கு ஏற்ப மனிதவள தீர்வுகள்."},
        {"num": "03", "title": "தொழில்முறை சேவை", "desc": "வாடிக்கையாளர் மையப்படுத்திய அணுகுமுறை."},
        {"num": "04", "title": "செயல்பாட்டு ஆதரவு", "desc": "நடைமுறை மனிதவளம், Facility மற்றும் போக்குவரத்து ஆதரவு."},
        {"num": "05", "title": "பாதுகாப்பு கவனம்", "desc": "பாதுகாப்பான மற்றும் பொறுப்புள்ள சேவையில் கவனம்."},
        {"num": "06", "title": "சரியான நேரத்தில் சேவை", "desc": "வணிக செயல்பாடுகளின் நேர முக்கியத்துவத்தை புரிந்துகொள்ளுதல்."},
    ],
}

CORPORATE_REQUIREMENTS = {
    "en": {
        "title": "Solutions for Growing Businesses & Industrial Organizations",
        "desc": "From workforce requirements to facility support and transportation, we provide practical service solutions designed around your operational needs.",
        "cards": [
            {"title": "Workforce Requirements", "desc": "For ongoing and project-based workforce needs."},
            {"title": "Facility Requirements", "desc": "Housekeeping, cleaning, gardening and facility support."},
            {"title": "Transportation Requirements", "desc": "Corporate and workforce transportation support."},
            {"title": "Heavy Vehicle Requirements", "desc": "Commercial heavy vehicle and tipper rental."},
        ],
        "cta": "Discuss Your Requirement With Us",
    },
    "ta": {
        "title": "நிறுவனங்கள் மற்றும் தொழிற்சாலைகளுக்கான தீர்வுகள்",
        "desc": "மனிதவள தேவைகள் முதல் Facility ஆதரவு மற்றும் போக்குவரத்து வரை, உங்கள் செயல்பாட்டு தேவைகளுக்கு ஏற்ப நடைமுறை சேவை தீர்வுகளை வழங்குகிறோம்.",
        "cards": [
            {"title": "மனிதவள தேவைகள்", "desc": "தொடர்ச்சியான மற்றும் திட்ட அடிப்படையிலான மனிதவள தேவைகளுக்கு."},
            {"title": "Facility தேவைகள்", "desc": "Housekeeping, cleaning, gardening மற்றும் facility ஆதரவு."},
            {"title": "போக்குவரத்து தேவைகள்", "desc": "Corporate மற்றும் பணியாளர் போக்குவரத்து ஆதரவு."},
            {"title": "கனரக வாகன தேவைகள்", "desc": "வணிக கனரக வாகனம் மற்றும் டிப்பர் வாடகை."},
        ],
        "cta": "உங்கள் தேவையை எங்களுடன் பகிரவும்",
    },
}

CTA_CORPORATE = {
    "en": {
        "title": "Looking for a Reliable Workforce or Transport Partner?",
        "desc": "Whether you are managing a factory, office, warehouse or business operation, let's discuss your manpower, facility and transportation requirements.",
    },
    "ta": {
        "title": "நம்பகமான மனிதவளம் அல்லது போக்குவரத்து கூட்டாளி தேவையா?",
        "desc": "உங்கள் தொழிற்சாலை, அலுவலகம், warehouse அல்லது நிறுவனத்தின் மனிதவளம், Facility மற்றும் போக்குவரத்து தேவைகளைப் பற்றி எங்களுடன் பேசலாம்.",
    },
}

CTA_LOCAL = {
    "en": {"title": "Need a Tipper or Transport Vehicle?", "desc": "Contact us for availability and pricing."},
    "ta": {"title": "டிப்பர் அல்லது போக்குவரத்து வாகனம் தேவையா?", "desc": "Availability மற்றும் விலை விவரங்களுக்கு எங்களை தொடர்பு கொள்ளுங்கள்."},
}

REVIEWS_NOTE = {
    "en": "Customer reviews will be published here once the business owner confirms names, ratings and permission to publish. [TO BE CONFIRMED]",
    "ta": "வாடிக்கையாளர் கருத்துகள், பெயர், மதிப்பீடு மற்றும் வெளியிட அனுமதி நிறுவன உரிமையாளரிடமிருந்து உறுதிப்படுத்தப்பட்ட பிறகு இங்கு வெளியிடப்படும். [TO BE CONFIRMED]",
}

# ---------------------------------------------------------------------------
# Per-page content
# ---------------------------------------------------------------------------

PAGES = {
    "index": {
        "en": {
            "meta_title": "Sri Annamalayar Transport & Logistics | Manpower, Transport & Heavy Vehicle Rental",
            "meta_desc": "Sri Annamalayar Transport & Logistics provides manpower supply, facility management, transportation and heavy vehicle rental solutions for businesses and industries in Tamil Nadu.",
            "h1": "Reliable Workforce & Transport Solutions",
            "eyebrow": "BUSINESS & INDUSTRIAL SERVICE SOLUTIONS",
            "hero_desc": "Supporting businesses and industries with dependable manpower, facility management, transportation and heavy vehicle rental services.",
            "hero_support": "5+ Years of Experience | Professional Service | Customer Focused",
            "hero_badge": "5+ Years Experience",
            "positioning_title": "Supporting Businesses & Industries",
            "positioning_desc": "We provide workforce, facility management and transportation solutions designed around the operational requirements of businesses and industrial organizations.",
            "positioning_points": ["Workforce Support", "Facility Support", "Transportation", "Heavy Vehicles"],
            "positioning_cta": "Discuss Your Requirement",
            "services_title": "Our Services",
            "services_subtitle": "Practical workforce, facility and transportation solutions for business and industrial requirements.",
            "capabilities_title": "Our Capabilities",
            "industries_title": "Industries & Business Requirements We Support",
            "clients_title": "Serving Businesses & Industries",
            "clients_line": "Serving Leading Industrial & Corporate Clients",
            "why_title": "Why Choose Sri Annamalayar?",
            "about_title": "About Sri Annamalayar Transport & Logistics",
            "about_body": [
                "Sri Annamalayar Transport & Logistics is a service-oriented business providing manpower, facility management, transportation and heavy vehicle rental solutions to businesses and industrial customers.",
                "With more than 5 years of experience, we support organizations with dependable workforce and transportation solutions based on their operational requirements.",
                "We understand that reliable manpower and transportation play an important role in maintaining smooth business operations.",
                "Our focus is to provide practical, professional and dependable service while understanding the individual requirements of every customer.",
            ],
            "about_cta": "Learn More About Us",
            "gallery_title": "Our Operations",
            "gallery_subtitle": "A glimpse of our workforce, vehicles and service operations.",
            "reviews_title": "What Our Customers Say",
        },
        "ta": {
            "meta_title": "Sri Annamalayar Transport & Logistics | மனிதவளம், போக்குவரத்து & கனரக வாகன வாடகை",
            "meta_desc": "தமிழ்நாட்டில் நிறுவனங்கள் மற்றும் தொழிற்சாலைகளுக்கு மனிதவள சப்ளை, Facility Management, போக்குவரத்து மற்றும் கனரக வாகன வாடகை சேவைகளை Sri Annamalayar Transport & Logistics வழங்குகிறது.",
            "h1": "நம்பகமான மனிதவளம் & போக்குவரத்து தீர்வுகள்",
            "eyebrow": "நிறுவனங்கள் மற்றும் தொழிற்சாலைகளுக்கான சேவை தீர்வுகள்",
            "hero_desc": "நிறுவனங்கள் மற்றும் தொழிற்சாலைகளின் தேவைகளுக்காக நம்பகமான மனிதவளம், Facility Management, போக்குவரத்து மற்றும் கனரக வாகன வாடகை சேவைகளை வழங்குகிறோம்.",
            "hero_support": "5+ ஆண்டுகள் அனுபவம் | தொழில்முறை சேவை | வாடிக்கையாளர் கவனம்",
            "hero_badge": "5+ ஆண்டுகள் அனுபவம்",
            "positioning_title": "நிறுவனங்கள் மற்றும் தொழிற்சாலைகளுக்கு ஆதரவு",
            "positioning_desc": "நிறுவனங்களின் செயல்பாட்டு தேவைகளுக்கு ஏற்ப மனிதவளம், Facility Management மற்றும் போக்குவரத்து தீர்வுகளை வழங்குகிறோம்.",
            "positioning_points": ["மனிதவள ஆதரவு", "Facility ஆதரவு", "போக்குவரத்து", "கனரக வாகனங்கள்"],
            "positioning_cta": "உங்கள் தேவையை பகிரவும்",
            "services_title": "எங்கள் சேவைகள்",
            "services_subtitle": "வணிக மற்றும் தொழில்துறை தேவைகளுக்கான நடைமுறை மனிதவளம், Facility மற்றும் போக்குவரத்து தீர்வுகள்.",
            "capabilities_title": "எங்கள் திறன்கள்",
            "industries_title": "நாங்கள் ஆதரிக்கும் தொழில் மற்றும் நிறுவன தேவைகள்",
            "clients_title": "நிறுவனங்கள் மற்றும் தொழிற்சாலைகளுக்கு சேவை",
            "clients_line": "முன்னணி தொழில்துறை & Corporate வாடிக்கையாளர்களுக்கு சேவை",
            "why_title": "ஏன் Sri Annamalayar-ஐ தேர்வு செய்ய வேண்டும்?",
            "about_title": "Sri Annamalayar Transport & Logistics பற்றி",
            "about_body": [
                "Sri Annamalayar Transport & Logistics என்பது நிறுவனங்கள் மற்றும் தொழில்துறை வாடிக்கையாளர்களுக்கு மனிதவளம், Facility Management, போக்குவரத்து மற்றும் கனரக வாகன வாடகை தீர்வுகளை வழங்கும் ஒரு சேவை சார்ந்த நிறுவனம்.",
                "5 ஆண்டுகளுக்கும் மேலான அனுபவத்துடன், நிறுவனங்களின் செயல்பாட்டு தேவைகளுக்கு ஏற்ப நம்பகமான மனிதவளம் மற்றும் போக்குவரத்து தீர்வுகளை வழங்கி வருகிறோம்.",
                "நம்பகமான மனிதவளம் மற்றும் போக்குவரத்து, வணிக செயல்பாடுகள் சீராக நடைபெற முக்கிய பங்கு வகிக்கிறது என்பதை நாங்கள் புரிந்துகொள்கிறோம்.",
                "ஒவ்வொரு வாடிக்கையாளரின் தனிப்பட்ட தேவைகளையும் புரிந்துகொண்டு, நடைமுறையான, தொழில்முறையான மற்றும் நம்பகமான சேவையை வழங்குவதே எங்கள் குறிக்கோள்.",
            ],
            "about_cta": "மேலும் அறிய",
            "gallery_title": "எங்கள் செயல்பாடுகள்",
            "gallery_subtitle": "எங்கள் மனிதவளம், வாகனங்கள் மற்றும் சேவை செயல்பாடுகளின் ஒரு பார்வை.",
            "reviews_title": "எங்கள் வாடிக்கையாளர்கள் கூறுவது",
        },
    },
    "about": {
        "en": {
            "meta_title": "About Sri Annamalayar Transport & Logistics | Tamil Nadu",
            "meta_desc": "Learn about Sri Annamalayar Transport & Logistics — 5+ years supporting businesses and industries with manpower, facility management and transport solutions.",
            "h1": "About Sri Annamalayar Transport & Logistics",
            "intro": [
                "Sri Annamalayar Transport & Logistics is a service-oriented business providing manpower, facility management, transportation and heavy vehicle rental solutions to businesses and industrial customers.",
                "With more than 5 years of experience, we support organizations with dependable workforce and transportation solutions based on their operational requirements.",
            ],
            "experience_title": "Our Experience",
            "experience_desc": "More than 5 years of experience supporting businesses and industries with workforce and transportation solutions.",
            "what_we_do_title": "What We Do",
            "what_we_do_desc": "We provide manpower supply, facility management, transport & logistics and heavy vehicle rental — built around each customer's operational requirements.",
            "vision_title": "Our Vision",
            "vision": "To become a trusted workforce and transportation solutions partner for businesses and industries.",
            "mission_title": "Our Mission",
            "mission": "To deliver reliable people, professional services and dependable transportation solutions that help our customers operate efficiently.",
            "approach_title": "Our Approach",
            "approach_desc": "We understand that reliable manpower and transportation play an important role in maintaining smooth business operations. Our focus is to provide practical, professional and dependable service while understanding the individual requirements of every customer.",
            "why_title": "Why Choose Us",
            "cta_title": "Let's Discuss Your Requirement",
        },
        "ta": {
            "meta_title": "Sri Annamalayar Transport & Logistics பற்றி | Tamil Nadu",
            "meta_desc": "5+ ஆண்டுகளாக நிறுவனங்கள் மற்றும் தொழிற்சாலைகளுக்கு மனிதவளம், Facility Management மற்றும் போக்குவரத்து தீர்வுகளை வழங்கும் Sri Annamalayar Transport & Logistics பற்றி அறிக.",
            "h1": "Sri Annamalayar Transport & Logistics பற்றி",
            "intro": [
                "Sri Annamalayar Transport & Logistics என்பது நிறுவனங்கள் மற்றும் தொழில்துறை வாடிக்கையாளர்களுக்கு மனிதவளம், Facility Management, போக்குவரத்து மற்றும் கனரக வாகன வாடகை தீர்வுகளை வழங்கும் ஒரு சேவை சார்ந்த நிறுவனம்.",
                "5 ஆண்டுகளுக்கும் மேலான அனுபவத்துடன், நிறுவனங்களின் செயல்பாட்டு தேவைகளுக்கு ஏற்ப நம்பகமான மனிதவளம் மற்றும் போக்குவரத்து தீர்வுகளை வழங்கி வருகிறோம்.",
            ],
            "experience_title": "எங்கள் அனுபவம்",
            "experience_desc": "நிறுவனங்கள் மற்றும் தொழிற்சாலைகளுக்கு மனிதவளம் மற்றும் போக்குவரத்து தீர்வுகளில் 5+ ஆண்டுகளுக்கும் மேலான அனுபவம்.",
            "what_we_do_title": "நாங்கள் என்ன செய்கிறோம்",
            "what_we_do_desc": "மனிதவள சப்ளை, Facility Management, போக்குவரத்து & லாஜிஸ்டிக்ஸ் மற்றும் கனரக வாகன வாடகை — ஒவ்வொரு வாடிக்கையாளரின் செயல்பாட்டு தேவைக்கும் ஏற்ப வழங்குகிறோம்.",
            "vision_title": "எங்கள் நோக்கம்",
            "vision": "நிறுவனங்கள் மற்றும் தொழிற்சாலைகளின் நம்பகமான மனிதவளம் மற்றும் போக்குவரத்து சேவை கூட்டாளராக வளர்வதே எங்களின் நோக்கம்.",
            "mission_title": "எங்கள் பணி",
            "mission": "எங்கள் வாடிக்கையாளர்களின் செயல்பாடுகள் சிறப்பாக நடைபெற நம்பகமான மனிதவளம், தொழில்முறை சேவைகள் மற்றும் சிறந்த போக்குவரத்து தீர்வுகளை வழங்குவது எங்களின் நோக்கம்.",
            "approach_title": "எங்கள் அணுகுமுறை",
            "approach_desc": "நம்பகமான மனிதவளம் மற்றும் போக்குவரத்து, வணிக செயல்பாடுகள் சீராக நடைபெற முக்கிய பங்கு வகிக்கிறது என்பதை நாங்கள் புரிந்துகொள்கிறோம். ஒவ்வொரு வாடிக்கையாளரின் தனிப்பட்ட தேவைகளையும் புரிந்துகொண்டு, நடைமுறையான, தொழில்முறையான மற்றும் நம்பகமான சேவையை வழங்குவதே எங்கள் கவனம்.",
            "why_title": "எங்களை ஏன் தேர்வு செய்ய வேண்டும்",
            "cta_title": "உங்கள் தேவையை நம்முடன் பகிரவும்",
        },
    },
    "services": {
        "en": {
            "meta_title": "Our Services | Manpower, Facility, Transport & Heavy Vehicle Rental | Sri Annamalayar",
            "meta_desc": "Explore manpower supply, facility management, transport & logistics and heavy vehicle rental services from Sri Annamalayar Transport & Logistics.",
            "h1": "Our Services",
            "subtitle": "Practical workforce, facility and transportation solutions for business and industrial requirements.",
        },
        "ta": {
            "meta_title": "எங்கள் சேவைகள் | மனிதவளம், Facility, போக்குவரத்து & கனரக வாகன வாடகை | Sri Annamalayar",
            "meta_desc": "Sri Annamalayar Transport & Logistics வழங்கும் மனிதவள சப்ளை, Facility Management, போக்குவரத்து & லாஜிஸ்டிக்ஸ் மற்றும் கனரக வாகன வாடகை சேவைகளை காணுங்கள்.",
            "h1": "எங்கள் சேவைகள்",
            "subtitle": "வணிக மற்றும் தொழில்துறை தேவைகளுக்கான நடைமுறை மனிதவளம், Facility மற்றும் போக்குவரத்து தீர்வுகள்.",
        },
    },
    "manpower": {
        "en": {
            "meta_title": "Manpower Supply Services in Ranipet & Vellore | Sri Annamalayar",
            "meta_desc": "Skilled, semi-skilled, unskilled, ITI, diploma, degree and administrative manpower supply for businesses and industries in Ranipet and Vellore.",
            "h1": "Manpower Supply",
            "intro": "Reliable workforce solutions based on your operational requirements. We supply manpower across skill levels for businesses, factories and industrial operations.",
            "types_title": "Types of Workforce",
            "types": ["Skilled Manpower", "Semi-skilled Manpower", "Unskilled Manpower", "ITI-Qualified Workers", "Diploma Holders", "Degree Holders", "Administrative Personnel"],
            "requirements_title": "Business Requirements",
            "requirements_desc": "We work with businesses to understand their day-to-day and project-based workforce requirements, and supply manpower accordingly.",
            "corporate_title": "Corporate Workforce Support",
            "corporate_desc": "For factories, warehouses and corporate operations, we provide ongoing manpower support designed around shift patterns and operational needs.",
            "why_title": "Why Choose Us",
            "faq": [
                {"q": "What types of manpower do you provide?", "a": "Skilled, semi-skilled, unskilled, ITI, diploma, degree and administrative personnel based on requirements."},
                {"q": "Can businesses discuss specific workforce requirements?", "a": "Yes. Customers can contact the team to discuss their workforce needs."},
            ],
        },
        "ta": {
            "meta_title": "மனிதவள சப்ளை சேவைகள் - ராணிப்பேட்டை & வேலூர் | Sri Annamalayar",
            "meta_desc": "ராணிப்பேட்டை மற்றும் வேலூரில் நிறுவனங்கள் மற்றும் தொழிற்சாலைகளுக்கு Skilled, Semi-skilled, Unskilled, ITI, Diploma, Degree மற்றும் நிர்வாக மனிதவளம் வழங்குகிறோம்.",
            "h1": "மனிதவள சப்ளை",
            "intro": "உங்கள் நிறுவனத்தின் செயல்பாட்டு தேவைகளுக்கு ஏற்ப நம்பகமான மனிதவள தீர்வுகள். தொழிற்சாலைகள், நிறுவனங்கள் மற்றும் தொழில்துறை செயல்பாடுகளுக்கு அனைத்து திறன் நிலைகளிலும் மனிதவளம் வழங்குகிறோம்.",
            "types_title": "மனிதவள வகைகள்",
            "types": ["Skilled Manpower", "Semi-skilled Manpower", "Unskilled Manpower", "ITI தகுதியுள்ளவர்கள்", "Diploma படித்தவர்கள்", "Degree படித்தவர்கள்", "நிர்வாக பணியாளர்கள்"],
            "requirements_title": "வணிக தேவைகள்",
            "requirements_desc": "நிறுவனங்களின் அன்றாட மற்றும் திட்ட அடிப்படையிலான மனிதவள தேவைகளை புரிந்துகொண்டு, அதற்கேற்ப மனிதவளம் வழங்குகிறோம்.",
            "corporate_title": "Corporate மனிதவள ஆதரவு",
            "corporate_desc": "தொழிற்சாலைகள், warehouse மற்றும் corporate செயல்பாடுகளுக்கு, shift முறைமை மற்றும் செயல்பாட்டு தேவைகளுக்கு ஏற்ப தொடர்ச்சியான மனிதவள ஆதரவை வழங்குகிறோம்.",
            "why_title": "எங்களை ஏன் தேர்வு செய்ய வேண்டும்",
            "faq": [
                {"q": "நீங்கள் எந்த வகையான மனிதவளம் வழங்குகிறீர்கள்?", "a": "தேவைக்கு ஏற்ப Skilled, semi-skilled, unskilled, ITI, diploma, degree மற்றும் நிர்வாக பணியாளர்கள்."},
                {"q": "நிறுவனங்கள் குறிப்பிட்ட மனிதவள தேவைகளை பேச முடியுமா?", "a": "ஆம். வாடிக்கையாளர்கள் தங்கள் மனிதவள தேவைகளை எங்கள் குழுவுடன் தொடர்பு கொண்டு பேசலாம்."},
            ],
        },
    },
    "facility-management": {
        "en": {
            "meta_title": "Facility Management & Housekeeping Services | Sri Annamalayar",
            "meta_desc": "Housekeeping, professional cleaning, gardening and facility support services for businesses and industries from Sri Annamalayar Transport & Logistics.",
            "h1": "Facility Management",
            "intro": "Professional workforce support for housekeeping, cleaning, gardening and facility operations.",
            "sections": [
                {"title": "Housekeeping", "desc": "Trained housekeeping staff for offices, factories and commercial premises."},
                {"title": "Professional Cleaning", "desc": "Regular and deep cleaning support for business premises."},
                {"title": "Gardening", "desc": "Gardening and landscaping support to maintain facility grounds."},
                {"title": "Facility Support", "desc": "General facility workforce support based on your site requirements."},
            ],
            "why_title": "Why Choose Us",
            "faq": [
                {"q": "Can facility staffing be arranged for ongoing operations?", "a": "Yes, we support both ongoing and short-term facility management requirements."},
            ],
        },
        "ta": {
            "meta_title": "Facility Management & Housekeeping சேவைகள் | Sri Annamalayar",
            "meta_desc": "Sri Annamalayar Transport & Logistics வழங்கும் நிறுவனங்கள் மற்றும் தொழிற்சாலைகளுக்கான Housekeeping, Professional Cleaning, Gardening மற்றும் Facility ஆதரவு சேவைகள்.",
            "h1": "Facility Management",
            "intro": "Housekeeping, cleaning, gardening மற்றும் Facility பணிகளுக்கான தொழில்முறை பணியாளர் ஆதரவு.",
            "sections": [
                {"title": "Housekeeping", "desc": "அலுவலகங்கள், தொழிற்சாலைகள் மற்றும் வணிக வளாகங்களுக்கு பயிற்சி பெற்ற Housekeeping பணியாளர்கள்."},
                {"title": "Professional Cleaning", "desc": "வணிக வளாகங்களுக்கான வழக்கமான மற்றும் Deep Cleaning ஆதரவு."},
                {"title": "Gardening", "desc": "வளாக மைதானங்களை பராமரிக்க Gardening மற்றும் Landscaping ஆதரவு."},
                {"title": "Facility ஆதரவு", "desc": "உங்கள் தள தேவைகளுக்கு ஏற்ப பொதுவான Facility பணியாளர் ஆதரவு."},
            ],
            "why_title": "எங்களை ஏன் தேர்வு செய்ய வேண்டும்",
            "faq": [
                {"q": "தொடர்ச்சியான செயல்பாடுகளுக்கு Facility பணியாளர்களை ஏற்பாடு செய்ய முடியுமா?", "a": "ஆம், தொடர்ச்சியான மற்றும் குறுகிய கால Facility Management தேவைகளுக்கு நாங்கள் ஆதரவு அளிக்கிறோம்."},
            ],
        },
    },
    "transport": {
        "en": {
            "meta_title": "Transport & Logistics Services in Ranipet & Vellore | Sri Annamalayar",
            "meta_desc": "Corporate transportation, workforce transportation, goods transportation and commercial logistics support in Ranipet and Vellore.",
            "h1": "Transport & Logistics",
            "intro": "Transportation solutions for corporate, workforce, goods and commercial requirements.",
            "sections": [
                {"title": "Corporate Transportation", "desc": "Transportation solutions for corporate offices and business operations."},
                {"title": "Workforce Transportation", "desc": "Reliable transport for employees and site workforce."},
                {"title": "Goods Transportation", "desc": "Transportation support for business goods and materials."},
                {"title": "Commercial Logistics", "desc": "Logistics support for commercial and business transportation requirements."},
            ],
            "why_title": "Why Choose Us",
        },
        "ta": {
            "meta_title": "போக்குவரத்து & லாஜிஸ்டிக்ஸ் சேவைகள் - ராணிப்பேட்டை & வேலூர் | Sri Annamalayar",
            "meta_desc": "ராணிப்பேட்டை மற்றும் வேலூரில் Corporate போக்குவரத்து, பணியாளர் போக்குவரத்து, பொருட்கள் போக்குவரத்து மற்றும் வணிக Logistics ஆதரவு.",
            "h1": "போக்குவரத்து & லாஜிஸ்டிக்ஸ்",
            "intro": "Corporate, workforce, goods மற்றும் commercial தேவைகளுக்கான போக்குவரத்து தீர்வுகள்.",
            "sections": [
                {"title": "Corporate போக்குவரத்து", "desc": "Corporate அலுவலகங்கள் மற்றும் வணிக செயல்பாடுகளுக்கான போக்குவரத்து தீர்வுகள்."},
                {"title": "பணியாளர் போக்குவரத்து", "desc": "பணியாளர்கள் மற்றும் தள மனிதவளத்திற்கான நம்பகமான போக்குவரத்து."},
                {"title": "பொருட்கள் போக்குவரத்து", "desc": "வணிக பொருட்கள் மற்றும் பொருள்களுக்கான போக்குவரத்து ஆதரவு."},
                {"title": "வணிக Logistics", "desc": "வணிக மற்றும் business போக்குவரத்து தேவைகளுக்கான Logistics ஆதரவு."},
            ],
            "why_title": "எங்களை ஏன் தேர்வு செய்ய வேண்டும்",
        },
    },
    "heavy-vehicle-rental": {
        "en": {
            "meta_title": "Heavy Vehicle & Tipper Rental | Sri Annamalayar",
            "meta_desc": "10-wheeler tipper truck, Bharat Benz and U-Truck rental for commercial and industrial requirements. Contact us for availability.",
            "h1": "Heavy Vehicle Rental",
            "intro": "Heavy vehicle solutions for commercial and industrial requirements.",
            "primary": "10-Wheeler Tipper Trucks",
            "types": ["10-Wheeler Tipper Trucks", "Bharat Benz", "U-Truck"],
            "rental_title": "Rental Requirements",
            "rental_desc": "Vehicle availability and pricing depend on current requirements. Please contact us to confirm availability for your project or business need.",
            "availability_note": "Vehicle availability must be confirmed before booking.",
            "why_title": "Why Choose Us",
        },
        "ta": {
            "meta_title": "கனரக வாகனம் & டிப்பர் வாடகை | Sri Annamalayar",
            "meta_desc": "வணிக மற்றும் தொழில்துறை தேவைகளுக்கு 10-Wheeler Tipper Truck, Bharat Benz மற்றும் U-Truck வாடகை. Availability-க்கு எங்களை தொடர்பு கொள்ளுங்கள்.",
            "h1": "கனரக வாகன வாடகை",
            "intro": "வணிக மற்றும் தொழில் தேவைகளுக்கான கனரக வாகன தீர்வுகள்.",
            "primary": "10-Wheeler Tipper Trucks",
            "types": ["10-Wheeler Tipper Trucks", "Bharat Benz", "U-Truck"],
            "rental_title": "வாடகை தேவைகள்",
            "rental_desc": "வாகன Availability மற்றும் விலை தற்போதைய தேவைகளைப் பொறுத்தது. உங்கள் திட்டம் அல்லது வணிக தேவைக்கான Availability-ஐ உறுதிசெய்ய எங்களை தொடர்பு கொள்ளுங்கள்.",
            "availability_note": "Booking செய்வதற்கு முன் வாகன Availability உறுதி செய்யப்பட வேண்டும்.",
            "why_title": "எங்களை ஏன் தேர்வு செய்ய வேண்டும்",
        },
    },
    "industries": {
        "en": {
            "meta_title": "Industries We Support | Sri Annamalayar Transport & Logistics",
            "meta_desc": "Manpower, facility and transportation service solutions for automotive, manufacturing, industrial, logistics, warehousing and corporate businesses.",
            "h1": "Industries & Business Requirements We Support",
            "intro": "We provide workforce, facility and transportation service solutions for a range of business and industrial requirements.",
            "note": "Tell us about your operational requirement.",
            "cta": "Discuss Your Requirement",
        },
        "ta": {
            "meta_title": "நாங்கள் ஆதரிக்கும் தொழில்கள் | Sri Annamalayar Transport & Logistics",
            "meta_desc": "Automotive, Manufacturing, Industrial, Logistics, Warehousing மற்றும் Corporate வணிகங்களுக்கு மனிதவளம், Facility மற்றும் போக்குவரத்து சேவை தீர்வுகள்.",
            "h1": "நாங்கள் ஆதரிக்கும் தொழில் மற்றும் நிறுவன தேவைகள்",
            "intro": "பல்வேறு வணிக மற்றும் தொழில்துறை தேவைகளுக்கு மனிதவளம், Facility மற்றும் போக்குவரத்து சேவை தீர்வுகளை வழங்குகிறோம்.",
            "note": "உங்கள் செயல்பாட்டு தேவையைப் பற்றி எங்களிடம் கூறுங்கள்.",
            "cta": "உங்கள் தேவையை பகிரவும்",
        },
    },
    "gallery": {
        "en": {
            "meta_title": "Gallery | Our Operations | Sri Annamalayar Transport & Logistics",
            "meta_desc": "A glimpse of our workforce, vehicles, facility management teams and transport operations.",
            "h1": "Our Operations",
            "subtitle": "A glimpse of our workforce, vehicles and service operations.",
            "categories": ["Workforce", "Transport", "Heavy Vehicles", "Facility Management", "Company"],
            "note": "Photographs will be added here once supplied by the business. [TO BE CONFIRMED]",
        },
        "ta": {
            "meta_title": "கேலரி | எங்கள் செயல்பாடுகள் | Sri Annamalayar Transport & Logistics",
            "meta_desc": "எங்கள் மனிதவளம், வாகனங்கள், Facility Management குழு மற்றும் போக்குவரத்து செயல்பாடுகளின் ஒரு பார்வை.",
            "h1": "எங்கள் செயல்பாடுகள்",
            "subtitle": "எங்கள் மனிதவளம், வாகனங்கள் மற்றும் சேவை செயல்பாடுகளின் ஒரு பார்வை.",
            "categories": ["மனிதவளம்", "போக்குவரத்து", "கனரக வாகனங்கள்", "Facility Management", "நிறுவனம்"],
            "note": "நிறுவனத்திடமிருந்து புகைப்படங்கள் கிடைத்தவுடன் இங்கு சேர்க்கப்படும். [TO BE CONFIRMED]",
        },
    },
    "reviews": {
        "en": {
            "meta_title": "Customer Reviews | Sri Annamalayar Transport & Logistics",
            "meta_desc": "What our customers say about our manpower, facility management and transport services.",
            "h1": "What Our Customers Say",
        },
        "ta": {
            "meta_title": "வாடிக்கையாளர் கருத்துகள் | Sri Annamalayar Transport & Logistics",
            "meta_desc": "எங்கள் மனிதவளம், Facility Management மற்றும் போக்குவரத்து சேவைகள் குறித்து எங்கள் வாடிக்கையாளர்கள் கூறுவது.",
            "h1": "எங்கள் வாடிக்கையாளர்கள் கூறுவது",
        },
    },
    "contact": {
        "en": {
            "meta_title": "Contact Sri Annamalayar Transport & Logistics | Ranipet",
            "meta_desc": "Contact Sri Annamalayar Transport & Logistics for manpower, facility management and transportation requirements in Ranipet and Vellore.",
            "h1": "Contact Us",
            "intro": "Have a manpower, facility management or transportation requirement? Contact our team and tell us what you need.",
            "office_label": "Office Address",
            "transport_label": "Transport Service Address",
            "hours_label": "Business Hours",
            "lunch_label": "Lunch Break",
            "map_title": "Find Us",
        },
        "ta": {
            "meta_title": "Sri Annamalayar Transport & Logistics தொடர்பு | ராணிப்பேட்டை",
            "meta_desc": "ராணிப்பேட்டை மற்றும் வேலூரில் மனிதவளம், Facility Management மற்றும் போக்குவரத்து தேவைகளுக்கு Sri Annamalayar Transport & Logistics-ஐ தொடர்பு கொள்ளுங்கள்.",
            "h1": "தொடர்பு கொள்ளுங்கள்",
            "intro": "மனிதவளம், Facility Management அல்லது போக்குவரத்து தேவையா? உங்கள் தேவையை எங்கள் குழுவிடம் கூறுங்கள்.",
            "office_label": "அலுவலக முகவரி",
            "transport_label": "போக்குவரத்து சேவை முகவரி",
            "hours_label": "வணிக நேரம்",
            "lunch_label": "மதிய இடைவேளை",
            "map_title": "எங்களை கண்டறியுங்கள்",
        },
    },
    "privacy": {
        "en": {
            "meta_title": "Privacy Policy | Sri Annamalayar Transport & Logistics",
            "meta_desc": "Privacy policy for Sri Annamalayar Transport & Logistics — what information we collect through our enquiry form and how it is used.",
            "h1": "Privacy Policy",
            "body": [
                ("Information We Collect", "When you submit an enquiry through this website, we collect the details you provide: your name, company name, phone number, email address, location, service required and requirement details."),
                ("Why We Collect It", "This information is used only to respond to your enquiry, understand your requirement and, where relevant, contact you by phone, WhatsApp or email."),
                ("How Enquiries Are Handled", "Enquiries submitted through the quote form are sent to our team by email so we can follow up. We do not sell or share your information with third parties."),
                ("Contact", "If you have questions about this policy or your information, please contact us using the details on our Contact page."),
            ],
        },
        "ta": {
            "meta_title": "தனியுரிமை கொள்கை | Sri Annamalayar Transport & Logistics",
            "meta_desc": "Sri Annamalayar Transport & Logistics தனியுரிமை கொள்கை — எங்கள் Enquiry படிவம் மூலம் சேகரிக்கப்படும் தகவல்கள் மற்றும் அவை எவ்வாறு பயன்படுத்தப்படுகின்றன.",
            "h1": "தனியுரிமை கொள்கை",
            "body": [
                ("நாங்கள் சேகரிக்கும் தகவல்", "இந்த வலைத்தளம் மூலம் Enquiry அனுப்பும்போது, உங்கள் பெயர், நிறுவனப் பெயர், தொலைபேசி எண், மின்னஞ்சல், இடம், தேவையான சேவை மற்றும் தேவை விவரங்களை நாங்கள் சேகரிக்கிறோம்."),
                ("ஏன் சேகரிக்கிறோம்", "இந்த தகவல் உங்கள் Enquiry-க்கு பதிலளிக்கவும், உங்கள் தேவையை புரிந்துகொள்ளவும், தொலைபேசி, WhatsApp அல்லது மின்னஞ்சல் மூலம் தொடர்பு கொள்ளவும் மட்டுமே பயன்படுத்தப்படும்."),
                ("Enquiry எவ்வாறு கையாளப்படுகிறது", "Quote படிவம் மூலம் அனுப்பப்படும் Enquiries, தொடர்ந்து பின்தொடர எங்கள் குழுவுக்கு மின்னஞ்சல் மூலம் அனுப்பப்படும். உங்கள் தகவலை மூன்றாம் தரப்பினருக்கு விற்கவோ பகிரவோ மாட்டோம்."),
                ("தொடர்பு", "இந்த கொள்கை அல்லது உங்கள் தகவல் குறித்து கேள்விகள் இருந்தால், எங்கள் தொடர்பு பக்கத்தில் உள்ள விவரங்களைப் பயன்படுத்தி எங்களை தொடர்பு கொள்ளுங்கள்."),
            ],
        },
    },
    "404": {
        "en": {
            "meta_title": "Page Not Found | Sri Annamalayar Transport & Logistics",
            "meta_desc": "The page you're looking for may have moved or no longer exists.",
            "h1": "Page Not Found",
            "body": "The page you're looking for may have moved or no longer exists.",
        },
        "ta": {
            "meta_title": "பக்கம் கிடைக்கவில்லை | Sri Annamalayar Transport & Logistics",
            "meta_desc": "நீங்கள் தேடும் பக்கம் நகர்த்தப்பட்டிருக்கலாம் அல்லது இனி இல்லை.",
            "h1": "பக்கம் கிடைக்கவில்லை",
            "body": "நீங்கள் தேடும் பக்கம் நகர்த்தப்பட்டிருக்கலாம் அல்லது இனி இல்லை.",
        },
    },
}

QUOTE_FORM = {
    "en": {
        "title": "Request a Quote",
        "name": "Full Name",
        "company": "Company Name",
        "phone": "Phone Number",
        "email": "Email",
        "location": "Location",
        "service": "Service Required",
        "count": "Number of Workers / Vehicles",
        "details": "Requirement Details",
        "services": [
            "Manpower Supply", "Facility Management", "Housekeeping", "Professional Cleaning",
            "Gardening", "Corporate Transportation", "Workforce Transportation", "Goods Transportation",
            "Heavy Vehicle Rental", "10-Wheeler Tipper Rental", "Other",
        ],
    },
    "ta": {
        "title": "விலை விவரம் கேட்க",
        "name": "முழுப் பெயர்",
        "company": "நிறுவனப் பெயர்",
        "phone": "தொலைபேசி எண்",
        "email": "மின்னஞ்சல்",
        "location": "இடம்",
        "service": "தேவையான சேவை",
        "count": "பணியாளர்கள் / வாகனங்களின் எண்ணிக்கை",
        "details": "தேவை விவரங்கள்",
        "services": [
            "மனிதவள சப்ளை", "Facility Management", "Housekeeping", "Professional Cleaning",
            "Gardening", "Corporate போக்குவரத்து", "பணியாளர் போக்குவரத்து", "பொருட்கள் போக்குவரத்து",
            "கனரக வாகன வாடகை", "10-Wheeler Tipper வாடகை", "மற்றவை",
        ],
    },
}
