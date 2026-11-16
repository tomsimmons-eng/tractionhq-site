"""Page content for tractionhq.ai."""
import json
import markdown as md

SITE = "https://tractionhq.ai"
EMAIL = "tom@tractionhq.ai"
MAILTO = "mailto:tom@tractionhq.ai?subject=Free%20consultation%20request"
ORG_ID = SITE + "/#organization"
TODAY = "2026-11-15"
EXPENSE_LINE = "The cost listed does not include subscriptions, token usage, and other expenses, which are kept to a minimum for the client's benefit."

LLMS_INTRO = ("Traction Consulting is an AI-focused business and technology consultancy for small businesses in Charlotte, North Carolina and the surrounding metro. "
              "Its forward deployed engineers embed with a client's team to map how the business runs, build and integrate practical tools (AI, websites, custom software, API integrations), "
              "train employees, and track results with KPIs. Pricing is weekly with no contracts.")

def cta_band(h="Ready to see where AI fits in your business?", p="Book a free consultation. We'll talk through how your business runs today and tell you honestly whether we're a good fit."):
    return f"""<section class="band"><div class="wrap"><h2>{h}</h2><p>{p}</p><div class="ctas"><a class="btn" href="{MAILTO}">Email for a free consultation</a><a class="btn btn-ghost" href="/contact/">Contact options</a></div></div></section>"""

def page_head(h1, lede, eyebrow=""):
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    return f'<section class="page-head"><div class="wrap">{eb}<h1>{h1}</h1><p class="lede">{lede}</p><div class="ctas"><a class="btn" href="{MAILTO}">Book a free consultation</a></div></div></section>'

def lc(t):
    return t if t.startswith(("AI", "Google")) else t[0].lower() + t[1:]

def ul(items, cls="checks"): return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def faq_block(faqs, heading="Frequently asked questions", level=2):
    h = f"<h{level}>{heading}</h{level}>" if heading else ""
    sub = level + 1
    return '<div class="faq">' + h + "".join(f"<details><summary><h{sub}>{q}</h{sub}></summary><p>{a}</p></details>" for q, a in faqs) + "</div>"

def faq_ld(faqs, url):
    import re
    return {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in faqs]}

# ---------------------------------------------------------------- services
SERVICES = [
 dict(slug="ai-integration-private-llms", short="AI integration & private LLMs", name="AI integration and privately hosted LLMs",
  title="AI Integration & Private LLMs for Small Business | Traction",
  description="Put AI into your team's daily work, or run a privately hosted LLM so sensitive data stays on infrastructure you control. Charlotte AI consulting, weekly.",
  h1="AI integration and privately hosted LLMs",
  lede="We build AI into the work your employees already do, and when your data is sensitive, we set up a private large language model that runs on infrastructure you control.",
  problem="Most teams have a few people using ChatGPT on their own, with no shared approach, no guardrails, and no way to know whether it's helping. Meanwhile, the documents and customer details that would make AI most useful are exactly the ones owners are nervous about pasting into a public tool.",
  do=["Find the repetitive, text-heavy tasks where AI saves real time: drafting quotes and emails, summarizing calls, answering internal questions, and sorting incoming requests.",
      "Choose and configure the right tools, from business tiers of mainstream assistants to AI features already included in software you pay for.",
      "Set up a privately hosted LLM when it fits: an open-weight model running on your own hardware or a private cloud account, connected to your documents.",
      "Build simple internal assistants that answer questions from your own policies, price lists, and procedures.",
      "Write a plain-English AI use policy so employees know what's allowed and what data stays out.",
      "Measure time saved against a baseline so you can see whether it's working."],
  fit="Private LLMs make the most sense when you handle confidential client files, internal financials, or regulated information, or when per-user subscription costs add up across a team. For many businesses, a well-configured business-tier AI tool is the better first step, and we'll tell you which one fits.",
  faqs=[("What is a privately hosted LLM?", "A large language model that runs on hardware or a cloud account you control, rather than a shared public service. Your prompts and documents aren't sent to a third-party AI provider."),
        ("Is a private LLM as capable as ChatGPT?", "Open-weight models have become very capable for everyday business work like drafting, summarizing, and answering questions from your documents. The largest public models still lead on the hardest tasks, so we match the tool to the job."),
        ("What does it cost to run?", "It depends on the model size and whether it runs on a local machine or in the cloud. We estimate running costs before anything is purchased, and they're billed at cost as an expense.")],
  related=["ai-training", "custom-software-api-integrations", "process-mapping-kpis"]),
 dict(slug="websites-seo-geo", short="Websites, SEO & GEO", name="Websites, SEO and generative engine optimization",
  title="Websites, SEO & GEO for Charlotte Businesses | Traction",
  description="Fast websites built to be found on Google and recommended by AI assistants like ChatGPT. SEO and generative engine optimization (GEO) for Charlotte businesses.",
  h1="Websites, SEO and GEO that get you found",
  lede="Your website is still the first place customers and AI assistants check. We build fast, clear sites and optimize them for Google search and for generative engines like ChatGPT, Gemini, Copilot, and Perplexity.",
  problem="Many small business sites are slow, out of date, and vague about what the business actually does, where it works, and what it costs. Search engines struggle to rank them, and AI assistants can't confidently recommend them.",
  do=["Design and build fast, mobile-friendly websites you own, with clean code and no lock-in.",
      "Write one clear page per service and per main town you serve, answering the questions customers actually ask.",
      "Technical SEO: titles, descriptions, headings, internal links, sitemaps, page speed, and structured data (schema).",
      "Generative engine optimization (GEO): make your facts easy for AI systems to read, quote, and cite, including allowing AI search crawlers and publishing an llms.txt file.",
      "Set up Google Search Console and Bing Webmaster Tools and fix what they report.",
      "Publish useful articles on a steady schedule so you build authority over time."],
  fit="GEO isn't a trick. AI assistants tend to cite businesses whose information is consistent, specific, and easy to verify across the web. That comes from a good website plus accurate listings, and it builds on solid SEO rather than replacing it.",
  faqs=[("What is generative engine optimization (GEO)?", "GEO is the practice of making your business easy for AI assistants such as ChatGPT, Google's AI features, Copilot, and Perplexity to understand and cite. It builds on SEO with clear facts, structured data, consistent listings, and pages that directly answer questions."),
        ("How long does SEO take to work?", "Technical fixes can show up within weeks, but rankings for competitive terms usually build over several months. We report on progress so you can see what's moving."),
        ("Do I own the website?", "Yes. The site, domain, and content are yours, in accounts you control.")],
  related=["google-business-profile-ai-search", "marketing-lead-generation", "custom-software-api-integrations"]),
 dict(slug="google-business-profile-ai-search", short="Google Business Profile & AI visibility", name="Google Business Profile and AI search visibility",
  title="Google Business Profile & ChatGPT Visibility | Traction",
  description="Claim and optimize your Google Business Profile, Bing Places, Apple Business Connect and ChatGPT business listing so local customers and AI assistants find you.",
  h1="Google Business Profile and AI search visibility",
  lede="When someone nearby asks Google, Apple Maps, or ChatGPT for a business like yours, your listings decide whether you show up. We claim them, fix them, and keep them consistent.",
  problem="Listings get created by customers, data brokers, or a past employee, and then drift: old hours, wrong categories, a disconnected phone number, no photos. Inconsistent details make search engines and AI assistants less confident about recommending you.",
  do=["Claim, verify, and fully complete your Google Business Profile: categories, services, service area, hours, photos, and description.",
      "Set up Bing Places for Business and Apple Business Connect, which feed Bing, Copilot, Apple Maps, and Siri.",
      "Claim your business in ChatGPT's Business Hub where your business type is eligible, so the details ChatGPT shows come from you.",
      "Make your name, contact details, and service area consistent across major directories.",
      "Set up a simple, honest review request process for happy customers.",
      "Post updates and answer common questions so your profiles stay active."],
  fit="This is often the fastest visible win for a local business. Listings are free to claim, and fixing them usually takes days, not months.",
  faqs=[("Can you get my business listed in ChatGPT?", "OpenAI's Business Hub lets eligible businesses claim and manage how they appear in ChatGPT. Eligibility depends on business type and location. ChatGPT also draws on web search results, so your website, Bing presence, and directory listings still matter. We handle all of it."),
        ("Do I need a storefront for a Google Business Profile?", "No. Service-area businesses that visit customers can hide their address and list the areas they serve instead."),
        ("Will you write fake reviews?", "Never. We help you ask real customers for reviews in ways that follow each platform's rules.")],
  related=["websites-seo-geo", "marketing-lead-generation", "ai-training"]),
 dict(slug="custom-software-api-integrations", short="Custom software & API integrations", name="Custom software and API integrations",
  title="Custom Software & API Integrations in Charlotte | Traction",
  description="Connect the software you already pay for and build small custom tools that remove double entry. Practical API integrations and automation for small businesses.",
  h1="Custom software and API integrations",
  lede="Most small businesses don't need a giant new system. They need the tools they already pay for to talk to each other, plus a few small custom tools that fit how they actually work.",
  problem="The same customer gets typed into the CRM, the invoicing tool, and a spreadsheet. Leads from the website sit in an inbox. Reports take a day to assemble by hand. Every one of those gaps costs time and causes errors.",
  do=["Map where data is entered more than once and where handoffs get dropped.",
      "Connect your systems through their APIs, such as CRM, accounting, scheduling, email, forms, and e-commerce.",
      "Automate routine workflows like lead intake, follow-ups, invoicing triggers, and status updates.",
      "Build small custom web apps and dashboards when off-the-shelf software doesn't fit.",
      "Add AI steps where they help, like summarizing, classifying, or drafting inside a workflow.",
      "Document everything and keep it in accounts you own, so you're never locked in."],
  fit="We favor simple, maintainable solutions. If an existing feature or low-cost automation tool solves the problem, we'll use that before writing custom code.",
  faqs=[("What is an API integration?", "An API is a doorway that lets one software system send data to another. An integration uses it so information flows automatically, for example a new web form lead appearing in your CRM and triggering a follow-up email."),
        ("Who owns the code you write?", "You do. It lives in your accounts, with documentation, so another developer could pick it up."),
        ("How big a project can you take on?", "Larger builds are scoped as a set number of weeks with a written scope before work starts.")],
  related=["process-mapping-kpis", "ai-integration-private-llms", "marketing-lead-generation"]),
 dict(slug="process-mapping-kpis", short="Process mapping, KPIs & efficiency", name="Business process mapping, KPIs and operational efficiency",
  title="Business Process Mapping & KPIs in Charlotte | Traction",
  description="We map how work really flows through your business, find where time and money leak, and set up a short list of KPIs you can track every week. Charlotte, NC.",
  h1="Business process mapping, KPIs and operational efficiency",
  lede="Before buying any tool, it pays to see how work actually moves through your business. We map it, find the bottlenecks, and agree on a handful of numbers that show whether things are improving.",
  problem="In many small businesses, the process lives in the owner's head. That works until the owner wants a day off, a key employee leaves, or the business grows past the point where one person can track everything.",
  do=["Sit with your team and document how key workflows really run today, from first contact to paid invoice.",
      "Turn that into clear, visual process maps your employees can follow.",
      "Find the delays, duplicate work, and dropped handoffs that cost the most.",
      "Pick 3 to 5 KPIs that matter to you, like lead response time, quote-to-close rate, or hours per job, and set a baseline.",
      "Build a simple dashboard so you see the numbers weekly without assembling them by hand.",
      "Prioritize fixes by impact, then implement them one at a time."],
  fit="Process mapping is where nearly every engagement starts. It produces the plan and the baseline that every other improvement is measured against.",
  faqs=[("What is business process mapping?", "It's documenting, step by step, how a piece of work gets done: who does what, with which tools, and where it waits. The map makes problems visible and gives employees a clear standard to follow."),
        ("Which KPIs should a small business track?", "Only the few that drive decisions. Common ones are lead response time, conversion rate, average job value, gross margin by service, and hours spent on admin. We choose them with you."),
        ("Will this disrupt my team?", "We work around your schedule. Most mapping happens by shadowing real work and short interviews.")],
  related=["exit-readiness", "custom-software-api-integrations", "ai-training"]),
 dict(slug="ai-training", short="AI training for teams", name="AI education and employee AI integration",
  title="AI Training for Small Business Teams in Charlotte | Traction",
  description="Hands-on AI training for owners and employees, built around your real tasks and tools. Practical skills, clear data rules, and follow-up until new habits stick.",
  h1="AI training for owners and teams",
  lede="Buying an AI tool doesn't change anything until people use it well. We train your team on their real work, set clear rules for data, and follow up until the new habits stick.",
  problem="Generic AI webinars leave people impressed but unsure what to do on Monday. Some employees avoid AI entirely, others paste in data they shouldn't, and nobody shares what works.",
  do=["Short, hands-on sessions built around your team's actual tasks, documents, and software.",
      "Prompt libraries and templates for the jobs your people do every week.",
      "A plain-English AI use policy covering what data can and can't go into which tools.",
      "Role-specific coaching for the owner, office staff, sales, and field teams.",
      "Office hours and follow-up so questions get answered after the session ends.",
      "Tracking adoption and time saved, so training ties back to results."],
  fit="Training works best alongside real implementation. That's why our forward deployed engineers teach the same tools they set up for you.",
  faqs=[("Do my employees need technical skills?", "No. If they can write an email, they can learn to use AI tools well. We start from the basics and focus on their daily work."),
        ("Is training on-site or remote?", "Either. Many teams like an in-person kickoff in the Charlotte area followed by short remote sessions."),
        ("How do we keep company data safe?", "We set clear rules on which tools are approved and what information stays out, and we configure business-tier settings that don't use your data for training where available.")],
  related=["ai-integration-private-llms", "process-mapping-kpis", "google-business-profile-ai-search"]),
 dict(slug="exit-readiness", short="Exit & sale readiness", name="Exit and sale readiness",
  title="Get Your Business Ready to Sell: Exit Readiness | Traction",
  description="Make your business easier to sell or step back from: documented processes, clean KPIs, less owner dependence and modern systems a buyer can trust. Charlotte.",
  h1="Exit and sale readiness",
  lede="Whether you plan to sell in two years or just want the business to run without you, the work is the same: document how it runs, clean up the numbers, and reduce dependence on the owner.",
  problem="A business that only runs because the owner is there is hard to sell and stressful to own. Buyers and lenders look for documented processes, reliable reporting, and systems that will keep working after the handoff.",
  do=["Document core processes so the business can run without the owner in every decision.",
      "Clean up and standardize KPIs and reporting so performance is easy to show.",
      "Modernize systems and remove fragile workarounds, spreadsheets, and single points of failure.",
      "Organize the information a buyer typically asks for during due diligence.",
      "Shift routine work from the owner to the team, supported by tools and training.",
      "Coordinate with your accountant, attorney, or business broker, without replacing them."],
  fit="We focus on operations and technology. Valuation, legal, and tax advice should come from licensed professionals, and we're happy to work alongside yours.",
  faqs=[("How early should I start preparing to sell?", "Ideally a year or more ahead, so improvements show up in your results. But even a few months of work on documentation and reporting can make a sale smoother."),
        ("Do you value businesses or broker sales?", "No. We prepare the operations and systems. Valuation and the sale itself belong with a broker, accountant, and attorney."),
        ("What if I'm not selling?", "The same work makes a business more efficient and less stressful to run day to day.")],
  related=["process-mapping-kpis", "custom-software-api-integrations", "ai-integration-private-llms"]),
 dict(slug="marketing-lead-generation", short="Marketing & lead generation", name="Marketing and lead generation",
  title="Marketing & Lead Generation in Charlotte, NC | Traction",
  description="Practical marketing and lead generation for small businesses: capture every lead, respond fast, follow up automatically and see which channels pay off.",
  h1="Marketing and lead generation",
  lede="More leads only help if you catch them, answer them quickly, and follow up. We set up the whole path, from being found to booked work, and measure which channels pay off.",
  problem="Leads arrive by phone, web form, email, social media, and text, and some fall through the cracks. Follow-up depends on someone remembering. Marketing spend goes out without a clear view of what it brings back.",
  do=["Map every channel leads come from and route them into one place.",
      "Set up fast, consistent responses and automated follow-up sequences.",
      "Use AI to help draft content, emails, and social posts in your voice, with human review.",
      "Track lead source, response time, and conversion so you know what's working.",
      "Improve landing pages and calls to action on your website.",
      "Plan simple, sustainable content and outreach your team can keep up."],
  fit="We start with the leads you already get. Faster response and reliable follow-up often add more business than new advertising spend.",
  faqs=[("Do you run paid ads?", "We can set up and monitor simple campaigns when they make sense, but we usually start by fixing lead capture and follow-up so any ad spend isn't wasted."),
        ("Can AI write our marketing?", "AI is great for first drafts and ideas. A person who knows your business should always review and approve anything that goes out."),
        ("How do you measure results?", "We track a few numbers: leads by source, response time, conversion rate, and cost per lead, and review them with you.")],
  related=["websites-seo-geo", "google-business-profile-ai-search", "custom-software-api-integrations"]),
]
SVC = {s["slug"]: s for s in SERVICES}

def service_page(s):
    path = f"/services/{s['slug']}/"; url = SITE + path
    rel = "".join(f'<div class="card"><h3>{SVC[r]["name"]}</h3><p>{SVC[r]["lede"].split(".")[0]}.</p><p class="more"><a href="/services/{r}/">Learn about {lc(SVC[r]["short"])}</a></p></div>' for r in s["related"])
    body = page_head(s["h1"], s["lede"], "Services") + f"""
<section class="section"><div class="wrap narrow"><h2 class="first">The problem we solve</h2><p>{s['problem']}</p>
<h2>What we do</h2>{ul(s['do'])}
<h2>When it makes sense</h2><p>{s['fit']}</p>
<h2>How it fits a weekly engagement</h2><p>This work is delivered by our <a href="/how-it-works/">forward deployed engineers</a> as part of a simple weekly engagement with no contract. See <a href="/pricing/">pricing</a> for details, or read our <a href="/faq/">FAQ</a>.</p>
{faq_block(s['faqs'])}</div></section>
<section class="section alt"><div class="wrap"><h2 class="first">Related services</h2><div class="grid">{rel}</div><p><a href="/services/">See all services</a></p></div></section>
{cta_band()}"""
    ld = [{"@type": "Service", "@id": url + "#service", "name": s["name"], "serviceType": s["name"], "description": s["description"], "url": url,
           "provider": {"@id": ORG_ID}, "areaServed": {"@type": "AdministrativeArea", "name": "Charlotte metropolitan area, NC and SC"},
           "audience": {"@type": "BusinessAudience", "audienceType": "Small businesses"}}, faq_ld(s["faqs"], url)]
    return dict(path=path, title=s["title"], description=s["description"], h1=s["h1"], body=body, crumbs=[("Services", "/services/"), (s["short"], path)], ld=ld)

PAGES = []

# ---------------------------------------------------------------- general FAQ
FAQ_ALL = [
 ("What does Traction Consulting do?", "We're an AI-focused business and technology consultancy for small businesses in the Charlotte area. Our forward deployed engineers work inside your business to map how it runs, set up and connect the right tools (AI, websites, custom software, integrations), train your team, and track results with KPIs."),
 ("What is a forward deployed engineer?", "A technologist who works inside your business instead of from a distance. They learn how work actually gets done, then build, connect, and configure the tools that fix the bottlenecks, and stay until your team is using them."),
 ("How much does it cost?", "Pricing is weekly. Tier 1, for businesses under $1M in revenue with 1 to 10 employees, is $1,250 per week. Businesses with $1M to $3M in revenue and up to 15 employees get a custom quote. " + EXPENSE_LINE),
 ("Do I have to sign a contract?", "No. There are no contracts. You pay as you go, week by week, and can stop anytime."),
 ("What kinds of businesses do you work with?", "Owner-led small businesses, generally under $3M in revenue with up to 15 employees, in the Charlotte metro. Professional services, trades, retail, and other local businesses are all a good fit."),
 ("What areas do you serve?", "Charlotte and the surrounding area, including Waxhaw, Matthews, Ballantyne, Mint Hill, Huntersville, Cornelius, Davidson, Concord, Indian Trail, Monroe, and Fort Mill and Rock Hill in South Carolina. Much of the work can also be done remotely."),
 ("Is the first consultation really free?", "Yes. The first conversation is free and there's no obligation. We'll learn how your business runs and tell you honestly whether we can help."),
 ("How many clients do you take on?", "We keep a limited client roster so the engineer who learns your business is the one building for it, and your work doesn't wait in a long queue."),
 ("Will AI replace my employees?", "Our goal is to make your existing team more productive by taking repetitive work off their plates, so they can spend more time on customers and higher-value work."),
 ("Is my business data safe?", "We work only inside the access you grant, prefer accounts you own, keep sensitive data out of public AI tools unless you approve it in writing, and remove our access when an engagement ends. Where data is sensitive, a privately hosted LLM can keep it on infrastructure you control."),
 ("Who owns the work you create?", "You do. Websites, code, documentation, and accounts are set up in your name so you're never locked in."),
 ("How do I get started?", f"Email <a href=\"{MAILTO}\">{EMAIL}</a> to book a free consultation. Tell us a little about your business and what's slowing it down."),
]

# ---------------------------------------------------------------- home
svc_cards = "".join(f'<div class="card"><h3>{s["name"]}</h3><p>{s["lede"].split(". ")[0].rstrip(".")}.</p><p class="more"><a href="/services/{s["slug"]}/">Explore {lc(s["short"])}</a></p></div>' for s in SERVICES)
home_faq = [FAQ_ALL[i] for i in (1, 2, 3, 5)]
home_body = f"""<section class="hero"><div class="wrap"><span class="eyebrow">Charlotte AI consulting for small business</span>
<h1>Making AI work for you, inside your business</h1>
<p class="lede">Traction Consulting helps Charlotte-area small businesses put AI and modern technology to work. Our forward deployed engineers embed with your team to map how work gets done, build the right tools, and train your people, so everyone gets more done and the business earns more.</p>
<div class="ctas"><a class="btn" href="{MAILTO}">Book a free consultation</a><a class="btn btn-ghost" href="/how-it-works/">See how it works</a></div></div></section>
<section class="section"><div class="wrap narrow"><h2 class="first">AI is everywhere. Making it useful is the hard part.</h2>
<p>Most small business owners know AI and modern software could save them time and money. Few have the hours to figure out which tools matter, how to connect them, or how to get employees to use them.</p>
<p>So it stalls. A few people try ChatGPT on their own. The website goes stale. Leads come in through five channels and nobody tracks them. The business runs on the owner's memory instead of a process.</p>
<p>Large companies solve this with in-house technology teams. Small businesses deserve the same advantage at a price that makes sense. That's what we do.</p></div></section>
<section class="section alt"><div class="wrap"><h2 class="first">What we help with</h2><div class="grid">{svc_cards}</div><p><a href="/services/">See all services</a></p></div></section>
<section class="section"><div class="wrap narrow"><h2 class="first">Forward deployed engineers, not slide decks</h2>
<p>A forward deployed engineer works inside your business instead of from a distance. They don't hand you a report and leave. They learn how work actually gets done, then build, connect, and configure the tools that fix the bottlenecks they find.</p>
<ol class="steps"><li><strong>Discover and map.</strong> We learn how your business runs and where it loses time, money, or leads.</li>
<li><strong>Plan and measure.</strong> We agree on priorities and 3 to 5 KPIs that show progress.</li>
<li><strong>Build and integrate.</strong> We set up the AI, software, and integrations your plan calls for.</li>
<li><strong>Train and adopt.</strong> We work alongside your team until the new tools are part of the routine.</li>
<li><strong>Review and improve.</strong> We check the numbers with you and adjust.</li></ol>
<p><a href="/how-it-works/">Learn more about how we work</a></p></div></section>
<section class="section alt"><div class="wrap narrow"><h2 class="first">Simple weekly pricing. No contracts.</h2>
<p>Tier 1 is <strong>$1,250 per week</strong> for businesses under $1M in revenue with 1 to 10 employees. Larger businesses, up to $3M in revenue and 15 employees, get a custom quote. Pay as you go and stop anytime. We keep a limited client roster so your work gets real attention.</p>
<p class="note">{EXPENSE_LINE}</p><p><a class="btn btn-outline" href="/pricing/">View pricing</a></p></div></section>
<section class="section"><div class="wrap narrow"><h2 class="first">Built for Charlotte small businesses</h2>
<p>We work with owner-led businesses across the Charlotte metro, from Ballantyne and south Charlotte to Waxhaw, Matthews, Huntersville, Concord, and Fort Mill. Meetings can happen in person or online, and much of the build work is done remotely. <a href="/charlotte-ai-consulting/">See our Charlotte service area</a>.</p>
{faq_block(home_faq, "Common questions")}<p><a href="/faq/">Read all FAQs</a> or browse <a href="/blog/">practical AI articles</a>.</p></div></section>
{cta_band()}"""
PAGES.append(dict(path="/", title="Traction Consulting | AI Consulting for Charlotte Businesses",
  description="Charlotte AI consulting for small businesses. Forward deployed engineers build AI tools, websites and integrations, then train your team. Weekly pricing.",
  h1="Making AI work for you, inside your business", body=home_body, ld=[faq_ld(home_faq, SITE + "/")]))

# ---------------------------------------------------------------- services index
groups = [("Strategy and operations", ["process-mapping-kpis", "exit-readiness"]), ("AI implementation", ["ai-integration-private-llms", "ai-training"]),
          ("Custom technology", ["custom-software-api-integrations"]), ("Visibility and growth", ["websites-seo-geo", "google-business-profile-ai-search", "marketing-lead-generation"])]
gh = ""
for g, slugs in groups:
    gh += f'<h2>{g}</h2><div class="grid">' + "".join(f'<div class="card"><h3>{SVC[x]["name"]}</h3><p>{SVC[x]["lede"]}</p><p class="more"><a href="/services/{x}/">More on {lc(SVC[x]["short"])}</a></p></div>' for x in slugs) + "</div>"
PAGES.append(dict(path="/services/", title="AI & Technology Consulting Services in Charlotte | Traction",
  description="Our services: AI integration, private LLMs, websites, SEO and GEO, Google Business Profile, custom software, process mapping, AI training and exit readiness.",
  h1="Services", crumbs=[("Services", "/services/")],
  body=page_head("Services", "One embedded team for the strategy, AI, software, and visibility work a small business needs. Every service is delivered inside a simple weekly engagement, and we start wherever the payoff is biggest.", "What we do")
  + f'<section class="section"><div class="wrap">{gh}<p class="note">Not sure where to start? Most engagements begin with <a href="/services/process-mapping-kpis/">process mapping and KPIs</a>, plus quick visibility wins like your <a href="/services/google-business-profile-ai-search/">Google Business Profile</a>.</p></div></section>' + cta_band(),
  ld=[{"@type": "ItemList", "@id": SITE + "/services/#list", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/services/{s['slug']}/", "name": s["name"]} for i, s in enumerate(SERVICES)]}]))
for s in SERVICES:
    PAGES.append(service_page(s))

# ---------------------------------------------------------------- how it works
hiw_faq = [FAQ_ALL[1], ("How much time does my team need to give?", "Usually a short weekly check-in plus time for training sessions and occasional shadowing. We work around your schedule and do most of the build work without pulling people off their jobs."),
           ("Do you work on-site?", "When it helps. Shadowing, training, and kickoffs often happen in person in the Charlotte area. Building and configuration are usually done remotely.")]
PAGES.append(dict(path="/how-it-works/", title="How It Works: Forward Deployed Engineers | Traction",
  description="Our forward deployed engineers embed with your team, map how work gets done, build and integrate tools, train staff and report KPIs. See what a week looks like.",
  h1="How it works: forward deployed engineers", crumbs=[("How it works", "/how-it-works/")],
  body=page_head("How it works: forward deployed engineers", "We don't sell software and walk away, and we don't hand over a slide deck. We embed with your team, build what's needed, and stay until it works.", "Our approach") + f"""
<section class="section"><div class="wrap narrow"><h2 class="first">What is a forward deployed engineer?</h2>
<p>The term comes from technology companies that send engineers to work directly inside a customer's organization instead of supporting them from headquarters. A forward deployed engineer learns the customer's real problems up close and builds solutions on the spot.</p>
<p>We bring that model to small businesses. Your engineer sits with your team (in person or online), learns how work actually gets done, and then builds, connects, and configures the tools that fix the bottlenecks they find. Behind them, AI agents handle research, first drafts, and routine build work, which is how we keep the price within reach of a small business. A person reviews and approves everything before it reaches you.</p>
<h2>How an engagement runs</h2>
<ol class="steps"><li><strong>Free consultation.</strong> A no-obligation conversation about your business and what's slowing it down. We'll tell you honestly if we're not the right fit.</li>
<li><strong>Foundation (first two weeks).</strong> Discovery and process mapping, a KPI baseline, an audit of the tools and subscriptions you already pay for, and quick wins such as fixing your Google Business Profile. You get a written roadmap.</li>
<li><strong>Build and integrate.</strong> One main workstream at a time from the roadmap: an automation, an integration, website pages, an AI assistant, or a training program.</li>
<li><strong>Train and adopt.</strong> We work with your employees until the new tools become part of their routine.</li>
<li><strong>Measure and adjust.</strong> We review your KPIs with you regularly and re-prioritize based on what the numbers say.</li></ol>
<h2>What a typical week looks like</h2>
<table class="tbl"><thead><tr><th scope="col">When</th><th scope="col">What happens</th></tr></thead><tbody>
<tr><td>Start of week</td><td>We confirm this week's priority from your roadmap.</td></tr>
<tr><td>Check-in</td><td>A 30 to 45 minute meeting, on-site or by video, to review progress and collect anything we need.</td></tr>
<tr><td>Midweek</td><td>Building, configuring, and testing. Your team keeps working normally.</td></tr>
<tr><td>End of week</td><td>Changes go live after your approval, and you get a short written summary: what was done, KPI movement, next steps, and any expenses.</td></tr></tbody></table>
<h2>What we always keep human</h2>{ul(["A named person leads your engagement and is your point of contact.", "Client meetings, on-site work, and sensitive conversations are handled by people.", "Nothing goes live in your business without a person reviewing it and your approval.", "You control access to your systems and data, and we remove ours when we're done."])}
<p>See <a href="/pricing/">pricing</a> or browse our <a href="/services/">services</a>.</p>
{faq_block(hiw_faq)}</div></section>{cta_band()}""",
  ld=[faq_ld(hiw_faq, SITE + "/how-it-works/")]))

# ---------------------------------------------------------------- pricing
pr_faq = [FAQ_ALL[3], ("What isn't included in the weekly price?", EXPENSE_LINE + " We review any expense with you before buying and show it on your invoice."),
          ("How does billing work?", "You're billed weekly. There's no long-term commitment, so you can pause or stop whenever you like."),
          ("What if my business is over $3M in revenue?", "Get in touch. We'll learn about your business in a free consultation and quote a custom engagement."),
          ("Can larger projects like a new website fit?", "Yes. Bigger builds such as a full website, a private LLM, or custom software are scoped as a set number of weeks, with a written scope before work starts.")]
PAGES.append(dict(path="/pricing/", title="Pricing: Weekly AI Consulting, No Contracts | Traction",
  description="Simple weekly pricing for Charlotte small businesses: $1,250/week for businesses under $1M revenue, custom quotes up to $3M. No contracts. Pay as you go.",
  h1="Simple weekly pricing", crumbs=[("Pricing", "/pricing/")],
  body=page_head("Simple weekly pricing", "No contracts. Pay as you go. Stay because it's working, not because you signed something.", "Pricing") + f"""
<section class="section"><div class="wrap"><div class="price-grid">
<div class="price featured"><h2 class="first">Tier 1</h2><p>For businesses under <strong>$1M in revenue</strong> with <strong>1 to 10 employees</strong>.</p><p class="amount">$1,250<small> / week</small></p>{ul(["Embedded forward deployed engineer", "Process mapping and KPI baseline", "One main workstream at a time", "Weekly check-in and written summary", "No contract, stop anytime"])}<a class="btn" href="{MAILTO}">Book a free consultation</a></div>
<div class="price"><h2 class="first">Tier 2</h2><p>For businesses with <strong>$1M to $3M in revenue</strong> and <strong>up to 15 employees</strong>.</p><p class="amount">Custom<small> quote</small></p>{ul(["More engineering time each week", "Room for parallel workstreams", "Everything in Tier 1", "Scoped after a free consultation", "No contract, stop anytime"])}<a class="btn btn-outline" href="mailto:tom@tractionhq.ai?subject=Tier%202%20quote%20request">Contact us for a quote</a></div>
</div>
<p class="note">{EXPENSE_LINE}</p>
<div class="narrow"><h2>Why weekly pricing?</h2><p>A small first step should be easy to say yes to. Weekly pricing lets you see real progress before committing more, and because there's no contract, we have to earn your business every week.</p>
<h2>Limited client roster</h2><p>We deliberately keep a limited client roster. The engineer who learns your business is the one who builds for it, and your work never waits behind a long queue.</p>
<p>Want to know what's included? See <a href="/how-it-works/">how it works</a> and our full list of <a href="/services/">services</a>.</p>
{faq_block(pr_faq)}</div></div></section>{cta_band()}""",
  ld=[{"@type": "Offer", "@id": SITE + "/pricing/#tier1", "name": "Tier 1 weekly engagement", "description": "For businesses under $1M revenue with 1 to 10 employees. No contract.",
       "priceCurrency": "USD", "price": "1250", "priceSpecification": {"@type": "UnitPriceSpecification", "price": "1250", "priceCurrency": "USD", "unitText": "week", "referenceQuantity": {"@type": "QuantitativeValue", "value": 1, "unitCode": "WEE"}},
       "seller": {"@id": ORG_ID}, "areaServed": "Charlotte metropolitan area", "url": SITE + "/pricing/"}, faq_ld(pr_faq, SITE + "/pricing/")]))

# ---------------------------------------------------------------- about
PAGES.append(dict(path="/about/", title="About Traction Consulting | Charlotte AI Consultancy",
  description="Traction Consulting equips Charlotte small businesses with affordable AI and technology, plus the engineers to put it to work. Founded by Tom Simmons.",
  h1="About Traction Consulting", crumbs=[("About", "/about/")], pagetype="AboutPage",
  body=page_head("About Traction Consulting", "We help small businesses get the same technology advantage large companies have, at a price that makes sense.", "About us") + f"""
<section class="section"><div class="wrap narrow"><h2 class="first">Our mission: making AI work for you</h2>
<p>Traction Consulting equips small businesses with practical, affordable AI and technology, and with the forward deployed engineers to put it to work, so every employee gets more done and the business becomes more profitable. We help owners prepare their businesses for how work gets done in the 21st century, whether the goal is running more efficiently, growing, or getting ready to sell.</p>
<h2>Why we started</h2>
<p>Large companies have in-house technology teams that evaluate tools, connect systems, and train staff. Most small businesses don't. AI has made it far faster and cheaper to build websites, integrations, and custom software, which means a small, focused team can now deliver that kind of help at a weekly price a local business can afford.</p>
<h2>Founder</h2>
<p>Traction Consulting was founded by <strong>Tom Simmons</strong>, a Charlotte-area business owner. Tom leads client relationships and strategy, and works with a technical delivery team and AI agents to build and support what each client needs. You can reach Tom directly at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>What we believe</h2>{ul(["<strong>Practical over hype.</strong> We recommend tools because they solve a real problem, not because they're new.", "<strong>Measure it.</strong> If we can't show progress in numbers you care about, we change course.", "<strong>You own it.</strong> Your accounts, your data, your code, with no lock-in.", "<strong>People stay in charge.</strong> AI does the heavy lifting; people review, approve, and stay accountable.", "<strong>Earn it every week.</strong> No contracts means we keep showing value or you keep your money."])}
<h2>Where we work</h2><p>We serve businesses across the <a href="/charlotte-ai-consulting/">Charlotte metro</a>, in person when it helps and remotely when it doesn't. Learn <a href="/how-it-works/">how we work</a> or see our <a href="/services/">services</a>.</p>
</div></section>{cta_band()}""",
  ld=[{"@type": "Person", "@id": SITE + "/about/#tom", "name": "Tom Simmons", "jobTitle": "Founder", "worksFor": {"@id": ORG_ID}, "email": EMAIL}]))

# ---------------------------------------------------------------- Charlotte
towns = [("Waxhaw", "NC"), ("Matthews", "NC"), ("Ballantyne and south Charlotte", "NC"), ("Mint Hill", "NC"), ("Indian Trail", "NC"), ("Monroe", "NC"), ("Huntersville", "NC"), ("Cornelius", "NC"), ("Davidson", "NC"), ("Mooresville", "NC"), ("Concord", "NC"), ("Gastonia", "NC"), ("Fort Mill", "SC"), ("Tega Cay", "SC"), ("Rock Hill", "SC"), ("Indian Land", "SC")]
clt_faq = [("Do you meet in person in Charlotte?", "Yes, when it helps. Kickoffs, process mapping, shadowing, and training sessions often happen on-site at your business. Day-to-day building is usually done remotely."),
           ("Do you work with businesses outside Charlotte?", "Our focus is the Charlotte metro, including nearby towns in North and South Carolina. Much of our work can be done remotely, so ask if you're farther away."),
           ("Do you have an office I can visit?", "We're a service-area business. We come to you or meet online, which keeps our costs, and your price, down.")]
PAGES.append(dict(path="/charlotte-ai-consulting/", title="AI Consulting in Charlotte, NC for Small Business | Traction",
  description="Hands-on AI and technology consulting for small businesses in Charlotte, NC and nearby towns like Waxhaw, Matthews, Huntersville, Concord and Fort Mill, SC.",
  h1="AI consulting for Charlotte small businesses", crumbs=[("Charlotte service area", "/charlotte-ai-consulting/")],
  body=page_head("AI consulting for Charlotte small businesses", "Traction Consulting works with owner-led businesses across the Charlotte metro, in person when it matters and remotely when it doesn't.", "Charlotte, NC") + f"""
<section class="section"><div class="wrap narrow"><h2 class="first">Local help, hands-on work</h2>
<p>Charlotte is one of the fastest-growing regions in the Southeast, and competition for customers and employees keeps rising. Small businesses here are being asked to do more with the same size team. AI and better-connected software can close that gap, but only if someone takes the time to set them up properly and teach people to use them.</p>
<p>That's our job. Because we're based in the area, your forward deployed engineer can sit with your team, watch how work really flows, and run training face to face. Then the building and configuration happen remotely, so you aren't paying for drive time.</p>
<h2>What Charlotte businesses ask us for</h2>{ul([f'<a href="/services/google-business-profile-ai-search/">Showing up on Google Maps and in ChatGPT</a> when nearby customers search', f'<a href="/services/websites-seo-geo/">A faster, clearer website</a> that ranks and converts', f'<a href="/services/ai-training/">AI training</a> so employees use tools safely and well', f'<a href="/services/custom-software-api-integrations/">Connecting the software</a> they already pay for', f'<a href="/services/process-mapping-kpis/">Documenting processes and tracking KPIs</a>', f'<a href="/services/exit-readiness/">Getting ready to sell</a> or step back from day-to-day work'])}
<h2>Towns we serve near Charlotte</h2>
<p>We serve small businesses throughout Mecklenburg, Union, Cabarrus, Iredell, Gaston, York, and Lancaster counties, including:</p>
<ul class="towns">{"".join(f"<li>{t}, {st}</li>" for t, st in towns)}</ul>
<p>Not on the list? If you're within driving distance of Charlotte, or happy to work mostly online, get in touch.</p>
<h2>Pricing for Charlotte small businesses</h2><p>Tier 1 is $1,250 per week for businesses under $1M in revenue with 1 to 10 employees, with no contract. Businesses from $1M to $3M in revenue get a custom quote. <a href="/pricing/">See full pricing</a>.</p>
{faq_block(clt_faq)}</div></section>{cta_band("Talk to a Charlotte AI consultant")}""",
  ld=[faq_ld(clt_faq, SITE + "/charlotte-ai-consulting/"), {"@type": "Service", "@id": SITE + "/charlotte-ai-consulting/#service", "name": "AI consulting for small businesses in Charlotte, NC", "serviceType": "AI and technology consulting", "provider": {"@id": ORG_ID},
      "areaServed": [{"@type": "City", "name": "Charlotte, NC"}] + [{"@type": "City", "name": f"{t.replace('Ballantyne and south Charlotte', 'Ballantyne')}, {st}"} for t, st in towns]}]))

# ---------------------------------------------------------------- FAQ
PAGES.append(dict(path="/faq/", title="FAQ: AI Consulting, Pricing & How We Work | Traction",
  description="Answers to common questions about Traction Consulting: forward deployed engineers, weekly pricing, no contracts, service area, data security and how to start.",
  h1="Frequently asked questions", crumbs=[("FAQ", "/faq/")],
  body=page_head("Frequently asked questions", "Straight answers about what we do, what it costs, and how we work.", "FAQ") + f'<section class="section"><div class="wrap narrow">{faq_block(FAQ_ALL, "", level=1)}<p>Have a question that isn\'t here? Email <a href="mailto:{EMAIL}">{EMAIL}</a>, or read more about <a href="/how-it-works/">how it works</a> and <a href="/pricing/">pricing</a>.</p></div></section>' + cta_band(),
  ld=[faq_ld(FAQ_ALL, SITE + "/faq/")]))

# ---------------------------------------------------------------- contact
contact_body = page_head("Contact Traction Consulting", "The first consultation is free. Tell us a little about your business and what's slowing it down, and we'll reply by email to set up a time.", "Contact") + f"""
<section class="section"><div class="wrap narrow"><h2 class="first">Email us</h2>
<p>The fastest way to reach us is email: <a href="{MAILTO}"><strong>{EMAIL}</strong></a>.</p>
<h2>Or use this form</h2>
<p>This form opens a pre-filled email in your email app, so nothing is stored on this website.</p>
<form class="contact" id="cf" action="mailto:{EMAIL}" method="post" enctype="text/plain">
<div><label for="n">Your name</label><input id="n" name="name" autocomplete="name" required></div>
<div><label for="b">Business name</label><input id="b" name="business" autocomplete="organization"></div>
<div><label for="s">Business size</label><select id="s" name="size"><option>Under $1M revenue, 1 to 10 employees</option><option>$1M to $3M revenue, up to 15 employees</option><option>Over $3M revenue</option><option>Not sure</option></select></div>
<div><label for="m">What would you like help with?</label><textarea id="m" name="message" rows="5" required></textarea></div>
<button class="btn" type="submit">Open email to send</button></form>
<script>document.getElementById('cf').addEventListener('submit',function(e){{e.preventDefault();var f=this,v=function(i){{return document.getElementById(i).value}};var body='Name: '+v('n')+'\\nBusiness: '+v('b')+'\\nSize: '+v('s')+'\\n\\n'+v('m');location.href='mailto:{EMAIL}?subject='+encodeURIComponent('Free consultation request: '+(v('b')||v('n')))+'&body='+encodeURIComponent(body);}});</script>
<h2>Where we work</h2><p>We serve small businesses across the <a href="/charlotte-ai-consulting/">Charlotte, NC metro</a>, meeting on-site or online. We don't have a public office.</p>
<h2>Before you reach out</h2><p>You might find answers in our <a href="/faq/">FAQ</a> or on our <a href="/pricing/">pricing page</a>.</p></div></section>"""
PAGES.append(dict(path="/contact/", title="Contact Traction Consulting | Free AI Consultation", 
  description="Book a free consultation with Traction Consulting. Email tom@tractionhq.ai to talk about AI, software and process improvements for your Charlotte-area business.",
  h1="Contact Traction Consulting", crumbs=[("Contact", "/contact/")], pagetype="ContactPage", body=contact_body))

# ---------------------------------------------------------------- privacy
PAGES.append(dict(path="/privacy/", title="Privacy Policy | Traction Consulting, Charlotte NC",
  description="How Traction Consulting handles information on tractionhq.ai: no tracking cookies, no visitor profiling, and email inquiries used only to respond to you.",
  h1="Privacy policy", crumbs=[("Privacy", "/privacy/")],
  body=f"""<section class="page-head"><div class="wrap narrow"><h1>Privacy policy</h1><p class="meta">Last updated November 15, 2026</p></div></section>
<section class="section"><div class="wrap narrow prose">
<p>This policy explains how Traction Consulting, LLC ("we") handles information related to this website, tractionhq.ai.</p>
<h2>Information we collect</h2>
<p><strong>Email you send us.</strong> If you email us or use the contact form (which opens your own email app), we receive what you choose to send, such as your name, email address, business name, and message. We use it only to respond, discuss working together, and provide services you request.</p>
<p><strong>Website visits.</strong> This site doesn't use advertising or tracking cookies and doesn't run analytics that build profiles of visitors. Our hosting provider may keep standard server logs (such as IP address, browser type, and pages requested) for security and reliability.</p>
<h2>How we share information</h2><p>We don't sell or rent personal information. We share it only with service providers that help us operate (for example, our email provider), when required by law, or with your permission.</p>
<h2>Client data</h2><p>Information we access while working for a client is governed by our agreement with that client. We work only inside the access a client grants, keep sensitive data out of public AI tools unless the client approves in writing, and remove our access when an engagement ends.</p>
<h2>Your choices</h2><p>You can ask us to access, correct, or delete the personal information you've sent us by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Changes</h2><p>We may update this policy and will change the date above when we do.</p>
<h2>Contact</h2><p>Questions? Email <a href="mailto:{EMAIL}">{EMAIL}</a>. You can also return to the <a href="/">home page</a>.</p></div></section>"""))

# ---------------------------------------------------------------- 404
PAGES.append(dict(path="/404.html", title="Page Not Found (404) | Traction Consulting Charlotte NC", noindex=True, nocanon=True,
  description="Sorry, that page doesn't exist on tractionhq.ai. Head back to the Traction Consulting home page, browse our services, or email us to book a free consultation.",
  h1="Page not found",
  body=f"""<section class="page-head"><div class="wrap narrow"><h1>Page not found</h1><p class="lede">Sorry, we couldn't find that page. It may have moved.</p>
<ul><li><a href="/">Home</a></li><li><a href="/services/">Services</a></li><li><a href="/pricing/">Pricing</a></li><li><a href="/blog/">Blog</a></li><li><a href="/contact/">Contact</a></li></ul></div></section>{cta_band()}"""))

# ---------------------------------------------------------------- blog
from pathlib import Path
import re as _re
POSTS = []
_order = ["forward-deployed-engineer-small-business", "get-recommended-by-chatgpt-google-ai", "ai-tasks-to-automate-small-business",
          "private-ai-small-business-data", "employee-ai-use-policy", "prepare-business-to-sell-processes-kpis"]
for slug in _order:
    raw = (Path(__file__).resolve().parents[1] / "posts" / f"{slug}.md").read_text()
    _, fm, text = raw.split("---", 2)
    meta = dict(l.split(": ", 1) for l in fm.strip().splitlines())
    words = len(text.split())
    body_html = md.markdown(text, extensions=["tables"])
    body_html = _re.sub(r"<h([1-5])>", lambda m: f"<h{int(m.group(1))+1}>", body_html) if "<h1>" in body_html else body_html
    body_html = body_html.replace("<table>", '<table class="tbl">')
    for a in _re.findall(r'<a href="(https?://[^"]+)"', body_html):
        body_html = body_html.replace(f'<a href="{a}"', f'<a href="{a}" rel="noopener"', 1)
    path = f"/blog/{slug}/"; url = SITE + path
    body = f"""<article><header class="page-head"><div class="wrap narrow"><span class="eyebrow">Blog</span><h1>{meta['h1']}</h1>
<p class="meta">By Traction Consulting &middot; <time datetime="{TODAY}">November 15, 2026</time> &middot; {max(1, round(words/230))} min read</p></div></header>
<div class="wrap narrow prose">{body_html}</div></article>
<section class="section"><div class="wrap narrow"><h2 class="first">Keep reading</h2><ul>{{related}}</ul></div></section>{cta_band()}"""
    POSTS.append(dict(slug=slug, path=path, title=meta["title"], description=meta["description"], h1=meta["h1"], date=TODAY, article=True, body=body,
        crumbs=[("Blog", "/blog/"), (meta["h1"] if len(meta["h1"]) < 40 else meta["h1"][:38].rsplit(" ", 1)[0] + "…", path)], words=words,
        ld=[{"@type": "BlogPosting", "@id": url + "#article", "headline": meta["h1"][:110], "description": meta["description"], "datePublished": TODAY, "dateModified": TODAY,
             "author": {"@type": "Organization", "@id": ORG_ID, "name": "Traction Consulting", "url": SITE + "/"}, "publisher": {"@id": ORG_ID},
             "mainEntityOfPage": {"@id": url + "#webpage"}, "image": SITE + "/assets/img/og-default.jpg", "wordCount": words, "inLanguage": "en-US",
             "isPartOf": {"@id": SITE + "/blog/#blog"}}]))
for i, p in enumerate(POSTS):
    rel = [POSTS[(i + k) % len(POSTS)] for k in (1, 2)]
    p["body"] = p["body"].replace("{related}", "".join(f'<li><a href="{r["path"]}">{r["h1"]}</a></li>' for r in rel) + '<li><a href="/blog/">All articles</a></li>')

items = "".join(f'<li><h2><a href="{p["path"]}">{p["h1"]}</a></h2><p class="meta"><time datetime="{p["date"]}">November 15, 2026</time></p><p>{p["description"]}</p></li>' for p in POSTS)
PAGES.append(dict(path="/blog/", title="Practical AI Blog for Charlotte Small Businesses | Traction",
  description="Plain-English articles on practical AI for small business owners: getting found by ChatGPT, private AI, AI policies, automation ideas and getting ready to sell.",
  h1="Practical AI for small business", crumbs=[("Blog", "/blog/")], pagetype="CollectionPage",
  body=f'<section class="page-head"><div class="wrap narrow"><span class="eyebrow">Blog</span><h1>Practical AI for small business</h1><p class="lede">Plain-English guides for Charlotte-area owners who want results from AI, not hype.</p></div></section><section class="section"><div class="wrap narrow"><ul class="post-list">{items}</ul></div></section>' + cta_band(),
  ld=[{"@type": "Blog", "@id": SITE + "/blog/#blog", "name": "Traction Consulting blog", "url": SITE + "/blog/", "publisher": {"@id": ORG_ID},
       "blogPost": [{"@id": SITE + p["path"] + "#article"} for p in POSTS]}]))
