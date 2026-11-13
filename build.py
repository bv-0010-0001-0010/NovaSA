#!/usr/bin/env python3
"""Generates the static HTML pages for novaconstructions.com.au.

Static output only — the generated .html files are the deliverable.
Re-run this if you want to change the header, footer or disclaimer
in one place instead of editing every page.
"""
import pathlib

SITE = "https://www.novaconstructions.com.au"
OUT = pathlib.Path(__file__).parent

BIZ = {
    "name": "Nova Construction Solutions SA",
    "legal": "Nova Construction Solutions SA Pty Ltd",
    "street": "61 Stony Brook Way",
    "suburb": "Truganina",
    "state": "VIC",
    "postcode": "3029",
    "acn": "669 389 744",
    "email_admin": "admin@novaconstructions.com.au",
    "service_area": "South Australia",
}

LOGO_SVG = "/assets/Black%20and%20White%20Modern%20Building%20Logo.svg"
LOGO_PNG = "/assets/Black%20and%20White%20Modern%20Building%20Logo.png"

NAV = [
  ("Services", "/services.html"),
  ("Industries", "/industries.html"),
  ("About", "/about.html"),
  ("For workers", "/for-workers.html"),
  ("Contact", "/contact.html"),
]

DISCLAIMER = """<strong>Disclaimer.</strong> The information on this website is general in nature and provided for
information purposes only. While Nova Construction Solutions SA Pty Ltd takes reasonable care to keep it current,
no warranty is given as to its accuracy or completeness. Nothing here is professional, legal, financial, engineering
or work health and safety advice. Service descriptions and availability are indicative only; all engagements are
subject to a separate written agreement. Work health and safety requirements, inductions and supervision remain
subject to applicable law and the responsibilities of the parties controlling the worksite. This website may link
to third-party sites which Nova does not control or endorse. This disclaimer does not limit rights that cannot be
excluded under applicable law."""

LATTICE = """<svg class="hero-lattice" viewBox="0 0 1200 720" preserveAspectRatio="xMaxYMid slice" aria-hidden="true" focusable="false">
        <defs>
          <pattern id="lattice" width="120" height="207.846" patternUnits="userSpaceOnUse">
            <path d="M60 0 L120 34.641 L120 103.923 L60 138.564 L0 103.923 L0 34.641 Z" fill="none" stroke="var(--concrete-deep)" stroke-width="1.4"/>
            <path d="M120 103.923 L180 138.564 L180 207.846 L120 242.487 L60 207.846 L60 138.564 Z" fill="none" stroke="var(--concrete-deep)" stroke-width="1.4"/>
            <path d="M0 103.923 L60 138.564 L60 207.846 L0 242.487 L-60 207.846 L-60 138.564 Z" fill="none" stroke="var(--concrete-deep)" stroke-width="1.4"/>
          </pattern>
        </defs>
        <rect width="1200" height="720" fill="url(#lattice)"/>
        <path d="M900 138.564 L960 173.205 L960 242.487 L900 277.128 L840 242.487 L840 173.205 Z" fill="var(--crimson)" opacity="0.09"/>
        <path d="M1020 346.41 L1080 381.051 L1080 450.333 L1020 484.974 L960 450.333 L960 381.051 Z" fill="var(--ink)" opacity="0.06"/>
      </svg>"""


def head(title, desc, path, og_type="website", extra_ld=""):
    canonical = SITE + (path if path != "/" else "/")
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#102c27">
<meta name="geo.region" content="AU-SA">
<meta name="geo.placename" content="South Australia">

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BIZ['name']}">
<meta property="og:locale" content="en_AU">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display&display=swap">
<link rel="stylesheet" href="/css/style.css">
{extra_ld}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(active):
    links = ""
    for label, href in NAV:
        cur = ' aria-current="page"' if href == active else ""
        links += f'      <a href="{href}"{cur}>{label}</a>\n'
    return f"""<header class="site-head">
  <div class="wrap head-in">
    <a class="brand" href="/" aria-label="{BIZ['name']} — home">
      <picture class="brand__image brand__image--header">
        <source srcset="{LOGO_SVG}" type="image/svg+xml">
        <img src="{LOGO_PNG}" alt="Nova Construction Solutions SA logo">
      </picture>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
    <nav class="nav" id="primary-nav" data-open="false" aria-label="Primary">
{links}      <a class="btn btn--primary" href="/contact.html?type=Request%20workers">Request a crew</a>
    </nav>
  </div>
</header>
"""


def footer():
    return f"""<footer class="site-foot">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <picture class="brand__image brand__image--footer" aria-hidden="true">
          <source srcset="{LOGO_SVG}" type="image/svg+xml">
          <img src="{LOGO_PNG}" alt="" loading="lazy">
        </picture>
        <address>
          {BIZ['legal']}<br>ACN {BIZ['acn']}<br>
          Registered office:<br>
          {BIZ['street']}<br>
          {BIZ['suburb']} {BIZ['state']} {BIZ['postcode']}<br><br>
          <a href="mailto:{BIZ['email_admin']}">{BIZ['email_admin']}</a>
        </address>
      </div>
      <div>
        <h4>Company</h4>
        <ul class="foot-links">
          <li><a href="/about.html">About Nova</a></li>
          <li><a href="/industries.html">Industries</a></li>
          <li><a href="/contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul class="foot-links">
          <li><a href="/services.html#labour-hire">Construction labour hire</a></li>
          <li><a href="/services.html#skilled-trades">Skilled trades</a></li>
          <li><a href="/services.html#workforce">Workforce solutions</a></li>
          <li><a href="/services.html#site-support">Site &amp; project support</a></li>
        </ul>
      </div>
      <div>
        <h4>Get started</h4>
        <ul class="foot-links">
          <li><a href="/contact.html?type=Request%20workers">Request a crew</a></li>
          <li><a href="/for-workers.html">Looking for work</a></li>
          <li><a href="/privacy.html">Privacy policy</a></li>
          <li><a href="/terms.html">Terms of use</a></li>
        </ul>
      </div>
    </div>

    <p class="foot-disclaimer">{DISCLAIMER}</p>

    <div class="foot-base">
      <span>&copy; <span data-year>2026</span> {BIZ['legal']}. All rights reserved.</span>
      <span>Registered office in Victoria &middot; Services across {BIZ['service_area']}</span>
    </div>
  </div>
</footer>
<script src="/js/main.js" defer></script>
</body>
</html>
"""


def crumbs(label, path):
    return f"""<div class="wrap crumbs"><a href="/">Home</a> &nbsp;/&nbsp; {label}</div>"""


def breadcrumb_ld(label, path):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE}/"}},
{{"@type":"ListItem","position":2,"name":"{label}","item":"{SITE}{path}"}}]}}
</script>
"""


ORG_LD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "{SITE}/#organisation",
  "name": "{BIZ['name']}",
  "legalName": "{BIZ['legal']}",
  "identifier": {{"@type": "PropertyValue", "propertyID": "ACN", "value": "{BIZ['acn']}"}},
  "url": "{SITE}/",
  "description": "Construction labour hire, skilled trades and workforce support for builders and contractors across South Australia.",
  "email": "{BIZ['email_admin']}",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{BIZ['street']}",
    "addressLocality": "{BIZ['suburb']}",
    "addressRegion": "{BIZ['state']}",
    "postalCode": "{BIZ['postcode']}",
    "addressCountry": "AU"
  }},
  "areaServed": {{"@type": "State", "name": "{BIZ['service_area']}"}},
  "knowsAbout": ["Construction labour hire", "Skilled trades", "Workforce solutions", "Civil construction", "Residential construction"],
  "contactPoint": [{{
    "@type": "ContactPoint",
    "email": "{BIZ['email_admin']}",
    "contactType": "customer service",
    "areaServed": "{BIZ['service_area']}",
    "availableLanguage": "English"
  }}]
}}
</script>
"""

TRADES = [
    "General labourers", "Skilled labourers", "Carpenters", "Formworkers",
    "Steel fixers", "Concreters", "Bricklayers", "Plasterers",
    "Tilers", "Painters", "Waterproofers", "Roof plumbers",
    "Excavator operators", "Bobcat operators", "Traffic controllers", "Pipelayers",
    "Landscapers", "Fencers", "Demolition labourers", "Site cleaners",
]

TICKETS = [
    "Construction Induction Card (White Card)",
    "Working at Heights",
    "Confined Space",
    "EWP (Elevated Work Platform)",
    "Forklift licence (LF)",
    "Traffic Management / TCT",
    "Asbestos awareness",
    "First Aid",
]


# ============================================================
#  PAGES
# ============================================================

def page_home():
    ld = ORG_LD + f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebSite","url":"{SITE}/","name":"{BIZ['name']}","publisher":{{"@id":"{SITE}/#organisation"}}}}
</script>
"""
    trades_li = "\n".join(f"        <li>{t}</li>" for t in TRADES)

    return head(
        "Construction Labour Hire South Australia | Nova Construction Solutions SA",
        "Nova Construction Solutions SA supports construction projects across South Australia with labour hire, skilled trades and workforce support.",
        "/", extra_ld=ld) + header("/") + f"""
<main id="main">

  <section class="hero">
    {LATTICE}
    <div class="wrap hero-in">
      <span class="eyebrow">Construction labour hire &middot; South Australia</span>
      <h1>The right crew, on site, on time.</h1>
      <p class="lead">Nova Construction Solutions SA supports builders, contractors and project teams across South
        Australia with construction labour, skilled trades and site support matched to the scope of the job.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="/contact.html?type=Request%20workers">Request a crew</a>
        <a class="btn btn--ghost" href="/services.html">See what we supply</a>
      </div>
    </div>
    <div class="wrap">
      <dl class="hero-facts">
        <div><dt>Registered office</dt><dd>Truganina, VIC</dd></div>
        <div><dt>Coverage</dt><dd>South Australia</dd></div>
        <div><dt>Engagement</dt><dd>Day, week or program</dd></div>
        <div><dt>Enquiries</dt><dd><a href="mailto:{BIZ['email_admin']}">{BIZ['email_admin']}</a></dd></div>
      </dl>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="dimline"><span>What we supply</span><i></i></p>
      <div class="split reveal">
        <div>
          <h2>Labour, trades and the people who keep a site moving.</h2>
        </div>
        <div>
          <p class="lead">Four ways builders use Nova. Most start with one and end up using two or three as the
            program shifts.</p>
        </div>
      </div>
      <div class="grid grid--4 reveal" style="margin-top:2.5rem">
        <a class="card chamfer" href="/services.html#labour-hire">
          <p class="card-tag">01 / Labour</p>
          <h3>Construction labour hire</h3>
          <p>General and skilled labourers for day work, short-term surges or the length of a program.</p>
          <span class="more">Learn more &rarr;</span>
        </a>
        <a class="card chamfer" href="/services.html#skilled-trades">
          <p class="card-tag">02 / Trades</p>
          <h3>Skilled trades</h3>
          <p>Ticketed, trade-specific workers matched against the actual scope in front of them.</p>
          <span class="more">Learn more &rarr;</span>
        </a>
        <a class="card chamfer" href="/services.html#workforce">
          <p class="card-tag">03 / Planning</p>
          <h3>Workforce solutions</h3>
          <p>Ongoing supply and planning for builders managing several sites and moving dates.</p>
          <span class="more">Learn more &rarr;</span>
        </a>
        <a class="card chamfer" href="/services.html#site-support">
          <p class="card-tag">04 / Support</p>
          <h3>Site &amp; project support</h3>
          <p>Clean-downs, materials handling, traffic control and the tasks that stall a program.</p>
          <span class="more">Learn more &rarr;</span>
        </a>
      </div>
    </div>
  </section>

  <section class="section section--concrete">
    <div class="wrap">
      <p class="dimline"><span>Trades on the books</span><i></i></p>
      <div class="split">
        <div class="reveal">
          <h2>Tell us the task. We'll tell you who fits.</h2>
          <p class="lead">Nova supports construction projects across South Australia. If a
            requirement sits outside the list, say so — sourcing against a specific scope is the job.</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="/contact.html?type=Request%20workers">Request a crew</a>
          </div>
        </div>
        <ul class="chips reveal">
{trades_li}
        </ul>
      </div>
    </div>
  </section>

  <section class="section section--ink">
    <div class="wrap">
      <p class="dimline"><span>How it works</span><i></i></p>
      <h2 style="max-width:20ch">Four steps, in this order, every time.</h2>
      <div class="steps reveal" style="margin-top:2.5rem">
        <div class="step">
          <h3>Scope the job</h3>
          <p>We confirm the trade, the ticket requirements, the site, the start date and how long you need it before
            anyone is sourced.</p>
        </div>
        <div class="step">
          <h3>Match the people</h3>
          <p>Workers are selected against that scope — experience, tickets and availability checked, not pulled at
            random from a roster.</p>
        </div>
        <div class="step">
          <h3>Get them on site</h3>
          <p>Workers are briefed on your site expectations before they arrive, then work within your supervision
            and induction process.</p>
        </div>
        <div class="step">
          <h3>Stay across it</h3>
          <p>One point of contact for the length of the engagement. Numbers scale up or down as the program moves.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="dimline"><span>Where we work</span><i></i></p>
      <div class="split">
        <div class="reveal">
          <h2>Supporting projects across South Australia.</h2>
          <p class="lead">Nova Construction Solutions SA works with builders and contractors across South Australia.
            Share your site location and project requirements to discuss availability.</p>
        </div>
        <div class="reveal">
          <table class="spec">
            <tr><th>Registered office</th><td>{BIZ['street']}, {BIZ['suburb']} {BIZ['state']} {BIZ['postcode']}</td></tr>
            <tr><th>Entity</th><td>{BIZ['legal']}</td></tr>
            <tr><th>ACN</th><td>{BIZ['acn']}</td></tr>
            <tr><th>Enquiries</th><td><a href="mailto:{BIZ['email_admin']}">{BIZ['email_admin']}</a></td></tr>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="band chamfer reveal">
        <div class="split">
          <div>
            <h2>Need people this week?</h2>
            <p>Send through the trade, the site and the dates. We'll come back with what we can cover.</p>
            <div class="btn-row">
              <a class="btn btn--primary" href="/contact.html?type=Request%20workers">Request a crew</a>
            </div>
          </div>
          <div>
            <h3 style="margin-top:.4rem">On the tools and after work?</h3>
            <p>Register your trade, tickets and availability, and we'll consider you for work as opportunities arise
              across South Australia.</p>
            <div class="btn-row">
              <a class="btn btn--ghost" href="/for-workers.html">Register with Nova</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>
""" + footer()


def page_services():
    ld = breadcrumb_ld("Services", "/services.html") + f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","serviceType":"Construction labour hire","provider":{{"@id":"{SITE}/#organisation"}},"areaServed":{{"@type":"State","name":"South Australia"}},"hasOfferCatalog":{{"@type":"OfferCatalog","name":"Construction workforce services","itemListElement":[
{{"@type":"Offer","itemOffered":{{"@type":"Service","name":"Construction labour hire"}}}},
{{"@type":"Offer","itemOffered":{{"@type":"Service","name":"Skilled trades"}}}},
{{"@type":"Offer","itemOffered":{{"@type":"Service","name":"Workforce solutions"}}}},
{{"@type":"Offer","itemOffered":{{"@type":"Service","name":"Site and project support"}}}}]}}}}
</script>
"""
    return head(
        "Construction Labour Hire & Skilled Trades South Australia | Nova Construction Solutions SA",
        "Construction labour hire, skilled trades, workforce planning and site support for builders and contractors across South Australia.",
        "/services.html", extra_ld=ld) + header("/services.html") + f"""
""" + crumbs("Services", "/services.html") + f"""
<main id="main">
  <section class="wrap page-head">
    <span class="eyebrow">Services</span>
    <h1>Workforce, matched to the scope.</h1>
    <p class="lead">Four services that overlap. Builders normally start with labour hire and pull in the rest as the
      program tightens.</p>
  </section>

  <section class="section" id="labour-hire">
    <div class="wrap">
      <p class="dimline"><span>01 &middot; Labour hire</span><i></i></p>
      <div class="split">
        <div class="reveal">
          <h2>Construction labour hire</h2>
          <p class="lead">General and skilled labourers, available by the day, the week or the length of a program.</p>
          <p>Useful when a program moves, a subcontractor drops off, weather pushes everything right, or a stage
            needs more hands than the permanent crew can cover. You keep supervision and site control; Nova handles
            sourcing, availability and the administration behind the placement.</p>
        </div>
        <div class="reveal">
          <table class="spec">
            <tr><th>Typical roles</th><td>General labourers, skilled labourers, trade assistants, site cleaners, demolition labourers</td></tr>
            <tr><th>Engagement</th><td>Day work, short-term surge, ongoing placement</td></tr>
            <tr><th>Standard tickets</th><td>Construction Induction Card (White Card) as a minimum; further tickets to scope</td></tr>
            <tr><th>Supervision</th><td>Your site, your supervision, your induction process</td></tr>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--concrete" id="skilled-trades">
    <div class="wrap">
      <p class="dimline"><span>02 &middot; Skilled trades</span><i></i></p>
      <div class="split">
        <div class="reveal">
          <h2>Skilled trades</h2>
          <p class="lead">Trade-specific workers matched against the actual scope, with tickets checked before they
            are put forward.</p>
          <p>A placement only works if the person fits the job. Nova treats accurate matching — on trade, experience,
            tickets and availability — as the measure of a good outcome, not how fast a gap gets filled.</p>
        </div>
        <div class="reveal">
          <table class="spec">
            <tr><th>Trades supplied</th><td>Carpenters, formworkers, steel fixers, concreters, bricklayers, plasterers, tilers, painters, waterproofers, roof plumbers</td></tr>
            <tr><th>Plant operators</th><td>Excavator, bobcat, EWP and forklift operators to ticket</td></tr>
            <tr><th>Verification</th><td>Tickets and licences sighted and recorded before placement</td></tr>
            <tr><th>Lead time</th><td>Shorter for common trades; specialist scopes need more notice</td></tr>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="workforce">
    <div class="wrap">
      <p class="dimline"><span>03 &middot; Workforce solutions</span><i></i></p>
      <div class="split">
        <div class="reveal">
          <h2>Workforce solutions</h2>
          <p class="lead">Ongoing planning and supply for builders running several sites at once.</p>
          <p>Rather than a fresh scramble every time a stage starts, Nova works to your forecast — what is coming,
            when, and how many. Numbers scale up and down against the program instead of against a phone call made
            the night before.</p>
        </div>
        <div class="reveal">
          <table class="spec">
            <tr><th>Best for</th><td>Builders and contractors with rolling stages or multiple concurrent sites</td></tr>
            <tr><th>How it runs</th><td>Forecast against your program, then supply to the schedule</td></tr>
            <tr><th>Contact</th><td>One point of contact across every site</td></tr>
            <tr><th>Flexibility</th><td>Scale up for a pour or a handover, scale back after</td></tr>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--concrete" id="site-support">
    <div class="wrap">
      <p class="dimline"><span>04 &middot; Site &amp; project support</span><i></i></p>
      <div class="split">
        <div class="reveal">
          <h2>Site &amp; project support</h2>
          <p class="lead">The tasks that quietly hold up a program when nobody is free to do them.</p>
          <p>Site clean-downs, materials handling, loading and unloading, waste segregation, traffic control and
            pre-handover preparation. Small scopes, but they sit on the critical path more often than they should.</p>
        </div>
        <div class="reveal">
          <table class="spec">
            <tr><th>Site presentation</th><td>Progressive clean-downs, waste segregation, pre-handover clean</td></tr>
            <tr><th>Materials</th><td>Loading, unloading, distribution around site</td></tr>
            <tr><th>Traffic</th><td>Ticketed traffic controllers for deliveries and works zones</td></tr>
            <tr><th>Access</th><td>Labour support for temporary fencing, hoarding and edge protection</td></tr>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="band chamfer reveal">
        <h2>Send us the scope.</h2>
        <p>Trade, site, start date and how long you need it. That's enough for us to come back with what we can cover.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="/contact.html?type=Request%20workers">Request a crew</a>
          <a class="btn btn--ghost" href="mailto:{BIZ['email_admin']}">Email Nova</a>
        </div>
      </div>
    </div>
  </section>
</main>
""" + footer()


def page_industries():
    items = [
        ("Residential", "Detached housing, townhouses and multi-unit developments across the growth corridor — scaled to each stage of the build."),
        ("Commercial", "Labour and trades for commercial builds, where program certainty and site coordination matter as much as headcount."),
        ("Civil", "Site labour and ticketed plant operators for civil works, matched against the plant, ticketing and scheduling the job demands."),
        ("Infrastructure", "Crews for longer programs and multiple work fronts, where continuity of the same people is worth more than volume."),
        ("Fit-outs", "Trade and labour support for commercial and residential fit-outs, from base-build handover to practical completion."),
        ("Maintenance", "Ongoing and reactive labour for building and facilities maintenance programs."),
    ]
    cards = "\n".join(
        f"""        <div class="card chamfer">
          <h3>{n}</h3>
          <p>{d}</p>
        </div>""" for n, d in items)

    return head(
        "Industries We Supply | Nova Construction Solutions SA",
        "Construction workforce support for residential, commercial, civil, infrastructure, fit-out and maintenance projects across South Australia.",
        "/industries.html", extra_ld=breadcrumb_ld("Industries", "/industries.html")) + header("/industries.html") + f"""
""" + crumbs("Industries", "/industries.html") + f"""
<main id="main">
  <section class="wrap page-head">
    <span class="eyebrow">Industries</span>
    <h1>Built for how South Australian construction runs.</h1>
    <p class="lead">Different sectors want different things from a labour supplier. A civil job lives on tickets and
      plant; a fit-out lives on sequencing. Nova supplies against the sector, not a single template.</p>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="dimline"><span>Sectors</span><i></i></p>
      <div class="grid grid--3 reveal">
{cards}
      </div>
    </div>
  </section>

  <section class="section section--concrete">
    <div class="wrap">
      <p class="dimline"><span>Tickets &amp; compliance</span><i></i></p>
      <div class="split">
        <div class="reveal">
          <h2>Tickets checked before anyone is put forward.</h2>
          <p class="lead">Every worker holds a current Construction Induction Card as a minimum. Beyond that, tickets
            are matched to the scope and sighted before placement.</p>
          <p>Site safety requirements, inductions and supervision remain with the principal contractor. Nova's job is
            making sure workers arrive briefed, ticketed and ready to follow them.</p>
        </div>
        <ul class="chips reveal">
""" + "\n".join(f"          <li>{t}</li>" for t in TICKETS) + f"""
        </ul>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="band chamfer reveal">
        <h2>Working in one of these sectors?</h2>
        <p>Tell us the project and the stage you're at, and we'll tell you what we can cover.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="/contact.html?type=Request%20workers">Request a crew</a>
        </div>
      </div>
    </div>
  </section>
</main>
""" + footer()


def page_about():
    return head(
        "About Nova Construction Solutions SA | South Australia",
        "Nova Construction Solutions SA Pty Ltd supports builders and contractors with construction labour hire and skilled trades across South Australia.",
        "/about.html", extra_ld=breadcrumb_ld("About", "/about.html") + ORG_LD) + header("/about.html") + f"""
""" + crumbs("About", "/about.html") + f"""
<main id="main">
  <section class="wrap page-head">
    <span class="eyebrow">About Nova</span>
    <h1>A workforce partner, not a phone number.</h1>
    <p class="lead">Nova Construction Solutions SA helps projects across South Australia get the right people, tickets and support —
      from a single labourer for a day through to workforce planning across a program.</p>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="dimline"><span>What Nova does</span><i></i></p>
      <div class="split">
        <div class="reveal">
          <h2>Two needs, one point of contact.</h2>
          <p>Nova Construction Solutions Pty Ltd supplies construction labour hire, skilled trades and project support
            to builders, contractors and project teams. The business exists to solve a narrow problem well:
            construction projects need the right people on site at the right time, and finding them shouldn't slow a
            program down.</p>
          <p>We work across two related needs — supplying workforce to businesses that need labour and trades, and
            providing direct site support to project teams that need more than staffing. Both run through the same
            person, so nothing gets lost between departments.</p>
        </div>
        <div class="reveal">
          <table class="spec">
            <tr><th>Legal entity</th><td>{BIZ['legal']}</td></tr>
            <tr><th>ACN</th><td>{BIZ['acn']}</td></tr>
            <tr><th>Registered office</th><td>{BIZ['street']}, {BIZ['suburb']} {BIZ['state']} {BIZ['postcode']}</td></tr>
            <tr><th>Category</th><td>Construction labour hire &amp; workforce solutions</td></tr>
            <tr><th>Service area</th><td>{BIZ['service_area']}</td></tr>
            <tr><th>Contact</th><td><a href="mailto:{BIZ['email_admin']}">{BIZ['email_admin']}</a></td></tr>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--concrete">
    <div class="wrap">
      <p class="dimline"><span>How we work</span><i></i></p>
      <div class="grid grid--3 reveal">
        <div class="card chamfer">
          <h3>Right person, right job</h3>
          <p>Workers are matched against what the scope actually needs. Sending a warm body to fill a line on a roster
            helps nobody.</p>
        </div>
        <div class="card chamfer">
          <h3>Direct communication</h3>
          <p>Site supervisors deal with Nova directly. No account layers, no relay, no waiting for someone to call
            someone else.</p>
        </div>
        <div class="card chamfer">
          <h3>Reliability over volume</h3>
          <p>A smaller number of well-matched placements is worth more than a big number that turns over every week.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="dimline"><span>Safety &amp; quality</span><i></i></p>
      <div class="split">
        <div class="reveal">
          <h2>Safety is set by the site and upheld by the worker.</h2>
          <p>Every site has its own safety requirements, induction and supervision structure. Nova's role is making
            sure workers arrive ready to follow them — briefed on expectations before deployment, with current
            tickets, and clear that site procedures take precedence from the moment they walk through the gate.</p>
          <p>Work health and safety obligations vary by project and jurisdiction and remain subject to applicable law.
            Nothing on this site changes the responsibilities of the parties controlling a worksite.</p>
        </div>
        <div class="reveal">
          <h2>Quality means the right match.</h2>
          <p>A placement is only successful if the worker fits the requirement. Nova measures itself on accurate
            matching — trade, experience, tickets, availability — rather than on how quickly a gap gets closed.</p>
          <p>If someone isn't the right fit for your site, tell us. We'd rather fix it the same day than have you
            quietly stop calling.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="band chamfer reveal">
        <h2>Work with Nova on your next project.</h2>
        <p>Whether you need a crew or you're after work yourself, tell us what you're working on.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="/contact.html?type=Request%20workers">Request a crew</a>
          <a class="btn btn--ghost" href="/for-workers.html">Looking for work</a>
        </div>
      </div>
    </div>
  </section>
</main>
""" + footer()


def page_workers():
    return head(
        "Construction Jobs South Australia — Register With Nova Construction Solutions SA",
        "Register your trade, tickets and availability with Nova Construction Solutions SA for construction labour and trade work across South Australia.",
        "/for-workers.html", extra_ld=breadcrumb_ld("For workers", "/for-workers.html")) + header("/for-workers.html") + f"""
""" + crumbs("For workers", "/for-workers.html") + f"""
<main id="main">
  <section class="wrap page-head">
    <span class="eyebrow">For workers</span>
    <h1>Got a trade and a ticket? Let's talk.</h1>
    <p class="lead">Nova places labourers, trades and plant operators on sites across South Australia.
      Register your details and we'll consider you for jobs as they come up.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="/contact.html?type=Looking%20for%20work">Register with Nova</a>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="dimline"><span>What we look for</span><i></i></p>
      <div class="grid grid--3 reveal">
        <div class="card chamfer">
          <h3>Current tickets</h3>
          <p>A valid Construction Induction Card (White Card) is the minimum. Extra tickets — heights, EWP, confined
            space, forklift, traffic control — open up more work.</p>
        </div>
        <div class="card chamfer">
          <h3>You turn up</h3>
          <p>On time, in the right PPE, ready to work. It sounds obvious. It's the single thing site supervisors ask
            us about most.</p>
        </div>
        <div class="card chamfer">
          <h3>Straight answers</h3>
          <p>Tell us what you've actually done and what you're actually available for. We'd rather place you well
            once than badly three times.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--concrete">
    <div class="wrap">
      <p class="dimline"><span>Registering</span><i></i></p>
      <div class="split">
        <div class="reveal">
          <h2>Four things to have ready.</h2>
          <div class="steps" style="margin-top:2rem">
            <div class="step">
              <h3>Your trade</h3>
              <p>What you do, and how long you've been doing it.</p>
            </div>
            <div class="step">
              <h3>Your tickets</h3>
              <p>White Card number plus anything else current — we'll need to sight them before a placement.</p>
            </div>
            <div class="step">
              <h3>Your availability</h3>
              <p>Days, weeks, ongoing. Whether you can travel, and how far.</p>
            </div>
            <div class="step">
              <h3>Right to work</h3>
              <p>Australian citizenship, permanent residency or a visa with valid work rights.</p>
            </div>
          </div>
        </div>
        <div class="reveal">
          <h2>Tickets that open doors</h2>
          <ul class="chips" style="margin-top:1.25rem">
""" + "\n".join(f"            <li>{t}</li>" for t in TICKETS) + f"""
          </ul>
          <p style="margin-top:1.75rem">Don't have all of them? Register anyway. General labouring work starts with a
            White Card, and plenty of people build the rest up from there.</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="/contact.html?type=Looking%20for%20work">Register with Nova</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="band chamfer reveal">
        <h2>Registering isn't a job offer.</h2>
        <p>It puts you on our list for work that matches your trade, tickets and availability. If something fits,
          we'll email you if a suitable opportunity arises.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="/contact.html?type=Looking%20for%20work">Register with Nova</a>
          <a class="btn btn--ghost" href="mailto:{BIZ['email_admin']}">Email us</a>
        </div>
      </div>
    </div>
  </section>
</main>
""" + footer()


def page_contact():
    ld = breadcrumb_ld("Contact", "/contact.html") + ORG_LD
    return head(
        "Contact Nova Construction Solutions SA | South Australia",
        "Request a crew or ask a question. Contact Nova Construction Solutions SA by email for construction workforce enquiries across South Australia.",
        "/contact.html", extra_ld=ld) + header("/contact.html") + f"""
""" + crumbs("Contact", "/contact.html") + f"""
<main id="main">
  <section class="wrap page-head">
    <span class="eyebrow">Contact</span>
    <h1>Tell us what the job needs.</h1>
    <p class="lead">Trade, site, start date and duration is enough to get started. We'll come back with what we can
      cover.</p>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="reveal">
        <p class="dimline"><span>Send an enquiry</span><i></i></p>

        <form class="form" id="enquiry-form" novalidate>
          <div class="hp" aria-hidden="true">
            <label for="company_website">Leave this field empty</label>
            <input type="text" id="company_website" name="company_website" tabindex="-1" autocomplete="off">
          </div>

          <div class="field">
            <label for="enquiry_type">What's this about? <span class="req">*</span></label>
            <select id="enquiry_type" name="enquiry_type" required>
              <option value="Request workers">I need workers on site</option>
              <option value="Looking for work">I'm looking for work</option>
              <option value="General enquiry">General enquiry</option>
            </select>
          </div>

          <div class="field--row">
            <div class="field">
              <label for="name">Your name <span class="req">*</span></label>
              <input type="text" id="name" name="name" required autocomplete="name">
            </div>
            <div class="field">
              <label for="company">Company</label>
              <input type="text" id="company" name="company" autocomplete="organization">
            </div>
          </div>

          <div class="field--row">
            <div class="field">
              <label for="email">Email <span class="req">*</span></label>
              <input type="email" id="email" name="email" required autocomplete="email">
            </div>
            <div class="field">
              <label for="phone">Phone (optional)</label>
              <input type="tel" id="phone" name="phone" autocomplete="tel">
            </div>
          </div>

          <div class="field--row">
            <div class="field">
              <label for="trade">Trade or role</label>
              <input type="text" id="trade" name="trade" placeholder="e.g. formworker, general labourer">
            </div>
            <div class="field">
              <label for="suburb">Site suburb</label>
              <input type="text" id="suburb" name="suburb" placeholder="e.g. Pakenham">
            </div>
          </div>

          <div class="field--row">
            <div class="field">
              <label for="start_date">Start date</label>
              <input type="date" id="start_date" name="start_date">
            </div>
            <div class="field">
              <label for="duration">How long for?</label>
              <input type="text" id="duration" name="duration" placeholder="e.g. 3 days, 6 weeks, ongoing">
            </div>
          </div>

          <div class="field">
            <label for="message">Details <span class="req">*</span></label>
            <textarea id="message" name="message" required placeholder="Scope, number of workers, tickets required, site access, anything else we should know."></textarea>
          </div>

          <div class="field">
            <label style="display:flex;gap:.6rem;align-items:flex-start;font-weight:400;font-size:.92rem">
              <input type="checkbox" name="consent" required style="width:auto;margin-top:.3rem">
              <span>I agree that Nova Construction Solutions may contact me about this enquiry, and I've read the
                <a href="/privacy.html">privacy policy</a>. <span class="req">*</span></span>
            </label>
          </div>

          <div>
            <button class="btn btn--primary" type="submit">Send enquiry</button>
          </div>

          <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>

      <aside class="reveal">
        <div class="contact-card chamfer">
          <p class="dimline"><span>Direct</span><i></i></p>
          <dl class="contact-list">
            <div>
              <dt>Enquiries</dt>
              <dd><a href="mailto:{BIZ['email_admin']}">{BIZ['email_admin']}</a></dd>
            </div>
            <div>
              <dt>Registered office</dt>
              <dd>{BIZ['street']}<br>{BIZ['suburb']} {BIZ['state']} {BIZ['postcode']}</dd>
            </div>
            <div>
              <dt>Entity</dt>
              <dd>{BIZ['legal']}</dd>
            </div>
            <div>
              <dt>ACN</dt>
              <dd>{BIZ['acn']}</dd>
            </div>
          </dl>
        </div>
      </aside>
    </div>
  </section>
</main>
""" + footer()


def page_privacy():
    return head(
        "Privacy Policy | Nova Construction Solutions",
        "How Nova Construction Solutions SA Pty Ltd handles personal information submitted through this website.",
        "/privacy.html", extra_ld=breadcrumb_ld("Privacy policy", "/privacy.html")) + header("") + f"""
""" + crumbs("Privacy policy", "/privacy.html") + f"""
<main id="main">
  <section class="wrap page-head">
    <span class="eyebrow">Legal</span>
    <h1>Privacy policy</h1>
    <p class="lead">Last updated: <span data-year>2026</span>. This policy explains how {BIZ['legal']} handles personal
      information.</p>
  </section>

  <section class="section">
    <div class="wrap prose">
      <h2>Who we are</h2>
      <p>{BIZ['legal']} of {BIZ['street']}, {BIZ['suburb']} {BIZ['state']} {BIZ['postcode']}
        (&ldquo;Nova&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;) is committed to protecting personal information in
        accordance with the <em>Privacy Act 1988</em> (Cth) and the Australian Privacy Principles.</p>

      <h2>What we collect</h2>
      <p>We collect only what we need to respond to enquiries and provide our services. Depending on your dealings with us, that may
        include:</p>
      <ul>
        <li>Contact details — name, company, email address, phone number and site location.</li>
        <li>For workers — trade, work history, licences and tickets, availability, and right-to-work information you choose to provide.</li>
        <li>Enquiry content you choose to send us through this website, by email or by phone.</li>
        <li>Basic technical information such as pages visited, collected in aggregate.</li>
      </ul>

      <h2>How we collect it</h2>
      <p>Directly from you — through the enquiry form on this website, by email, by phone or in person. Enquiries
        submitted through this website are transmitted to a Google Workspace account controlled by Nova.</p>

      <h2>Why we collect it</h2>
      <ul>
        <li>To respond to your enquiry and supply the services you have asked about.</li>
        <li>To match workers to roles and to verify tickets, licences and right to work.</li>
        <li>To administer services and meet applicable legal obligations.</li>
      </ul>
      <p>We do not sell personal information, and we do not use it for unrelated marketing without your consent.</p>

      <h2>Who we disclose it to</h2>
      <p>We may disclose personal information to a host client or principal contractor where necessary to arrange or
        manage a placement, to our professional advisers and service providers (including payroll, accounting and IT
        providers), and to a government body or regulator where required or authorised by law.</p>

      <h2>Storage and security</h2>
      <p>Information is held in cloud-based systems that may store data in Australia or overseas. We take reasonable
        steps to protect information from misuse, loss and unauthorised access, but no method of transmission or
        storage is completely secure.</p>

      <h2>Access, correction and complaints</h2>
      <p>You may ask for access to the personal information we hold about you, or ask us to correct it, by emailing
        <a href="mailto:{BIZ['email_admin']}">{BIZ['email_admin']}</a>. We will respond within a reasonable period.
        If you are not satisfied with our response to a privacy complaint, you may contact the Office of the
        Australian Information Commissioner at oaic.gov.au.</p>

      <h2>Cookies</h2>
      <p>This website does not set advertising or tracking cookies. If analytics are added in future, this policy will
        be updated.</p>

      <h2>Changes</h2>
      <p>We may update this policy from time to time. The current version is always the one published on this
        <a href="/privacy.html">privacy policy page</a>.</p>

      <h2>Contact</h2>
      <p>{BIZ['legal']}<br>
        {BIZ['street']}, {BIZ['suburb']} {BIZ['state']} {BIZ['postcode']}<br>
        <a href="mailto:{BIZ['email_admin']}">{BIZ['email_admin']}</a></p>

      <p style="margin-top:2.5rem;font-size:.9rem;color:var(--muted)">This policy is provided as a general template and
        is not legal advice. Have it reviewed by an Australian legal practitioner before you rely on it.</p>
    </div>
  </section>
</main>
""" + footer()


def page_terms():
    return head(
        "Terms of Use | Nova Construction Solutions",
        "Terms of use for the Nova Construction Solutions SA Pty Ltd website.",
        "/terms.html", extra_ld=breadcrumb_ld("Terms of use", "/terms.html")) + header("") + f"""
""" + crumbs("Terms of use", "/terms.html") + f"""
<main id="main">
  <section class="wrap page-head">
    <span class="eyebrow">Legal</span>
    <h1>Terms of use</h1>
    <p class="lead">Last updated: <span data-year>2026</span>. By using this website you accept these terms.</p>
  </section>

  <section class="section">
    <div class="wrap prose">
      <h2>1. About these terms</h2>
      <p>This website is operated by {BIZ['legal']}. By accessing or using it, you agree to these
        terms. If you do not agree, please do not use the site.</p>

      <h2>2. Information is general only</h2>
      <p>Content on this website is general in nature and provided for information purposes. It does not constitute
        professional, legal, financial, engineering or work health and safety advice, and must not be relied on as a
        substitute for advice specific to your circumstances or project.</p>

      <h2>3. No offer or contract</h2>
      <p>Descriptions of services, trades, tickets, availability, coverage and timeframes are indicative only. Nothing
        on this website constitutes an offer capable of acceptance. All engagements are subject to a separate written
        agreement between Nova and the client, which prevails over anything published here.</p>

      <h2>4. Accuracy</h2>
      <p>We take reasonable care to keep content accurate and current, but give no warranty that it is accurate,
        complete or up to date, and it may change without notice.</p>

      <h2>5. Site safety and legal obligations</h2>
      <p>Nothing on this website transfers, reduces or alters any duty owed by a principal contractor, site occupier
        or employer. Site safety requirements, inductions, supervision, risk assessment and statutory obligations
        under applicable work health and safety laws remain the responsibility of the party controlling the workplace.</p>

      <h2>6. Third-party links</h2>
      <p>This website may link to third-party websites. We do not control, endorse or accept responsibility for their
        content, products or practices.</p>

      <h2>7. Intellectual property</h2>
      <p>All content on this website, including text, layout, graphics and the Nova Construction Solutions name and
        logo, is owned by or licensed to {BIZ['legal']}. You may view and print pages for your own use. You may not
        reproduce, adapt or republish any part of the site commercially without our written permission.</p>

      <h2>8. Submissions</h2>
      <p>Information you submit through this website must be accurate and must not infringe anyone else's rights. We
        handle submissions in accordance with our <a href="/privacy.html">privacy policy</a>. Do not send confidential or
        sensitive material through the enquiry form.</p>

      <h2>9. Limitation of liability</h2>
      <p>To the maximum extent permitted by law, {BIZ['legal']} excludes all liability for any loss or damage
        (including indirect or consequential loss) arising from use of, or reliance on, this website or its content.
        Nothing in these terms excludes any right or guarantee that cannot lawfully be excluded, including under the
        Australian Consumer Law.</p>

      <h2>10. Governing law</h2>
      <p>These terms are governed by the laws applicable in South Australia, Australia, and you submit to the
        non-exclusive jurisdiction of its courts.</p>

      <h2>11. Contact</h2>
      <p><a href="mailto:{BIZ['email_admin']}">{BIZ['email_admin']}</a></p>

      <p style="margin-top:2.5rem;font-size:.9rem;color:var(--muted)">These terms are provided as a general template
        and are not legal advice. Have them reviewed by an Australian legal practitioner before you rely on them.</p>
    </div>
  </section>
</main>
""" + footer()


def page_404():
    return head("Page not found | Nova Construction Solutions",
                "The page you were looking for isn't here.",
                "/404") .replace('<meta name="robots" content="index, follow, max-image-preview:large">',
                                 '<meta name="robots" content="noindex, follow">') + header("") + f"""
<main id="main">
  <section class="wrap notfound">
    <p class="code">404</p>
    <h1>That page isn't on site.</h1>
    <p class="lead" style="margin-inline:auto">It may have moved, or the link may be wrong. Try the services page or email us for help.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="/">Back to home</a>
      <a class="btn btn--ghost" href="/contact.html">Contact us</a>
    </div>
  </section>
</main>
""" + footer()


PAGES = {
    "index.html": page_home,
    "services.html": page_services,
    "industries.html": page_industries,
    "about.html": page_about,
    "for-workers.html": page_workers,
    "contact.html": page_contact,
    "privacy.html": page_privacy,
    "terms.html": page_terms,
    "404.html": page_404,
}

if __name__ == "__main__":
    for filename, builder in PAGES.items():
        (OUT / filename).write_text(builder(), encoding="utf-8")
        print("wrote", filename)
