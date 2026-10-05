import json, os, re, sys, shutil, html
from plan import PAGES
import assets as A

PHONE = "01908 000000"          # <- swap for your call-tracking number
PHONE_TEL = "+441908000000"
FORM_ENDPOINT = ""            # <- paste your Formspree (or similar) form URL here, e.g. https://formspree.io/f/xxxx
DOMAIN = "https://www.garage-doors-milton-keynes.co.uk"
BRAND = "Garage Doors Milton Keynes"
AUTHOR = "Muhammad Usman Siddiqui"
AUTHOR_BIO = (f"{AUTHOR} researches and writes the buying guides and advice on {BRAND}. "
              "He focuses on plain-English explanations of door types, costs, security and upkeep so Milton Keynes homeowners can make a confident decision before they book a survey.")
HUB_OF = {"door": "garage-doors", "service": "services", "area": "areas", "guide": "guides", "brand": "brands"}
SECTION_CHILD = {v: k for k, v in HUB_OF.items()}
TAG = {"door": "Door type", "service": "Service", "area": "Area", "guide": "Guide", "brand": "Brand", "hub": "Explore", "util": ""}

MODE = sys.argv[1] if len(sys.argv) > 1 else "preview"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[2] if len(sys.argv) > 2 else f"{ROOT}/dist-" + MODE

meta = {s or "home": dict(slug=s, section=sec, label=lab, primary=pk, related=rel) for s, sec, lab, pk, rx, rel in PAGES}
content = {}
for key in meta:
    p = f"{ROOT}/content/{key}.json"
    if os.path.exists(p):
        content[key] = json.load(open(p))
LIVE = [k for k in meta if k in content]

CUR = {"key": "home"}
def _pre():
    return "" if CUR["key"] == "home" else "../"
def url(key, mode=None):
    key = key or "home"
    if mode == "abs":   # absolute path for canonical/schema
        return "/" if key == "home" else f"/{key}/"
    if MODE == "preview":
        return "index.html" if key == "home" else f"{key}.html"
    p = _pre()
    return (p or "./") if key == "home" else f"{p}{key}/"

def asset(name):
    return f"assets/{name}" if MODE == "preview" else f"{_pre()}assets/{name}"

def fix_links(h):
    def rep(m):
        href = m.group(1)
        if href.startswith("/") and not href.startswith("//"):
            path, _, frag = href.partition("#")
            k = path.strip("/") or "home"
            if k in meta:
                return f'href="{url(k)}{("#"+frag) if frag else ""}"'
        return m.group(0)
    return re.sub(r'href="([^"]+)"', rep, h)

def esc(s): return html.escape(s or "", quote=True)

def by_section(sec): return [k for k in LIVE if meta[k]["section"] == sec]

def nav_menu(sec):
    return "".join(f'<a href="{url(k)}">{esc(meta[k]["label"])}</a>' for k in by_section(sec))

def header(current):
    def dd(label, hub, sec):
        return f'<details><summary>{label}</summary><div class="menu"><a href="{url(hub)}"><strong>All {label.lower()}</strong></a>{nav_menu(sec)}</div></details>'
    burger = "".join([
        f'<b>Garage doors</b>' + "".join(f'<a href="{url(k)}">{esc(meta[k]["label"])}</a>' for k in by_section("door")),
        f'<b>Services</b>' + "".join(f'<a href="{url(k)}">{esc(meta[k]["label"])}</a>' for k in by_section("service")),
        f'<b>More</b><a href="{url("areas")}">Areas we cover</a><a href="{url("brands")}">Brands</a><a href="{url("guides")}">Guides</a><a href="{url("about")}">About</a><a href="{url("contact")}">Get a free quote</a>'])
    return f'''<div class="strip"><div class="wrap"><ul><li>Free, no-obligation quotes</li><li>All makes repaired</li><li>Milton Keynes &amp; surrounding towns</li></ul><span>Call <a href="tel:{PHONE_TEL}">{PHONE}</a></span></div></div>
<header class="hdr"><div class="wrap">
<a class="brand" href="{url("home")}" aria-label="{BRAND} home"><img src="{asset("logo.svg")}" alt="{BRAND}" width="230" height="49"></a>
<nav class="nav" aria-label="Main">{dd("Garage Doors","garage-doors","door")}{dd("Services","services","service")}<a href="{url("garage-door-prices")}">Prices</a><a href="{url("areas")}">Areas</a><a href="{url("guides")}">Guides</a><a href="{url("contact")}">Contact</a></nav>
<a class="btn btn-call" href="tel:{PHONE_TEL}">Call {PHONE}</a>
<details class="burger"><summary>Menu</summary><div class="panel">{burger}</div></details>
</div></header>'''

def crumbs(key):
    m = meta[key]
    if key == "home": return ""
    parts = [f'<a href="{url("home")}">Home</a>']
    hub = HUB_OF.get(m["section"])
    if hub and hub in content: parts.append(f'<a href="{url(hub)}">{esc(meta[hub]["label"])}</a>')
    parts.append(f'<span aria-current="page">{esc(m["label"])}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>›</span>'.join(parts) + '</nav>'

def quote_form(fid, compact=False, dark=False):
    services = ["New garage door", "Garage door repair", "Electric conversion", "Servicing", "Springs / cables", "Something else"]
    opts = "".join(f"<option>{s}</option>" for s in services)
    msg = "" if compact else f'<label for="{fid}-msg">Tell us about the door<textarea id="{fid}-msg" name="message" rows="4" placeholder="Door type, rough size, what\'s wrong or what you\'d like"></textarea></label>'
    return f'''<form class="qf" name="quote" method="POST" action="{FORM_ENDPOINT or url("thank-you")}">
<input type="hidden" name="_next" value="{DOMAIN}/thank-you/"><p hidden><label>Company <input name="_gotcha"></label></p>
<div class="row"><label for="{fid}-name">Name<input id="{fid}-name" name="name" required autocomplete="name"></label>
<label for="{fid}-pc">Postcode<input id="{fid}-pc" name="postcode" required autocomplete="postal-code" placeholder="MK…"></label></div>
<label for="{fid}-tel">Phone<input id="{fid}-tel" name="phone" type="tel" required autocomplete="tel"></label>
<label for="{fid}-svc">I need<select id="{fid}-svc" name="service">{opts}</select></label>
{msg}<button class="btn btn-call" type="submit">Get my free quote</button>
<p class="fine">We only use your details to reply to this enquiry.</p></form>'''

def sidebar(key):
    sec = meta[key]["section"]
    lists = []
    for title, s in (("Garage doors", "door"), ("Services", "service")):
        items = "".join(f'<li><a href="{url(k)}"{" aria-current=\"page\"" if k==key else ""}>{esc(meta[k]["label"])}</a></li>' for k in by_section(s))
        lists.append(f'<div class="box"><h3>{title}</h3><ul>{items}</ul></div>')
    if sec in ("guide",):
        items = "".join(f'<li><a href="{url(k)}"{" aria-current=\"page\"" if k==key else ""}>{esc(meta[k]["label"])}</a></li>' for k in by_section("guide"))
        lists = [f'<div class="box"><h3>More guides</h3><ul>{items}</ul></div>', lists[0]]
    if sec == "area":
        lists = [lists[1], lists[0]]
    return f'''<aside class="side"><div class="box quote"><h3>Free quote</h3><p style="margin:0">Call our local team:</p><a class="big" href="tel:{PHONE_TEL}">{PHONE}</a>{quote_form("sb", compact=True)}</div>{"".join(lists)}</aside>'''

CTA_INLINE = lambda: f'''<div class="cta-inline"><div><h3>Want a price for your garage?</h3><p>Free survey and written quote. Call or send a few details.</p></div><div class="ctas"><a class="btn btn-call" href="tel:{PHONE_TEL}">Call {PHONE}</a><a class="btn btn-ghost" href="{url("contact")}">Online quote</a></div></div>'''

def render_body(h):
    h = h.replace("{{PHONE}}", PHONE)
    h = re.sub(r'<div class="cta-inline">\s*</div>', lambda m: CTA_INLINE(), h)
    h = re.sub(r'<table', '<div class="tbl"><table', h)
    h = h.replace('</table>', '</table></div>')
    return fix_links(h)

PHOTO_DIR = f"{ROOT}/photos"
def photo(key):
    for ext in ("jpg","jpeg","webp","png"):
        if os.path.exists(f"{PHOTO_DIR}/{key}.{ext}"): return f"{key}.{ext}"
    return None
def art_src(key):
    p = photo(key)
    return asset("photos/"+p) if p else asset("door-"+key+".svg")

def card(k, thumb=True):
    c = content[k]; m = meta[k]
    img = ""
    if thumb and (k in A.DOOR_ART or photo(k)):
        img = f'<div class="thumb"><img src="{art_src(k)}" alt="" loading="lazy" width="480" height="360"></div>'
    return f'<a class="card" href="{url(k)}">{img}<span class="tag">{TAG[m["section"]]}</span><h3>{esc(c.get("h1") or m["label"])}</h3><p>{esc(c.get("summary",""))}</p><span class="go">Read more →</span></a>'

def related(key):
    m = meta[key]; out = []
    for r in m["related"]:
        if r in content and r != key and r not in out: out.append(r)
    sibs = by_section(m["section"])
    if key in sibs:
        i = sibs.index(key)
        for j in range(1, len(sibs)):
            s = sibs[(i + j) % len(sibs)]
            if s not in out and s != key: out.append(s)
            if len(out) >= 6: break
    if m["section"] == "area":
        out = [k for k in ["roller-garage-doors","sectional-garage-doors","electric-garage-doors","garage-door-repairs","garage-door-automation","garage-door-prices"] if k in content]
    return out[:6]

def areas_band():
    chips = "".join(f'<a href="{url(k)}">{esc(meta[k]["label"])}</a>' for k in by_section("area"))
    return f'<section class="band ink"><div class="wrap"><h2>Covering Milton Keynes and nearby towns</h2><p class="lead">From central Milton Keynes out to the market towns and villages around it. Not sure if we reach you? Call and ask.</p><div class="chips"><a href="{url("home")}">Milton Keynes</a>{chips}</div></div></section>'

def steps_band():
    return f'''<section class="band sky"><div class="wrap"><h2>How it works</h2><p class="lead">A simple, no-pressure process from first call to finished door.</p><div class="steps">
<div><h3>Call or send details</h3><p>Tell us about your door, or send a photo and your postcode.</p></div>
<div><h3>Free survey</h3><p>We measure up, check the opening and talk through the options.</p></div>
<div><h3>Clear written quote</h3><p>A fixed price with no obligation and no pushy follow-up.</p></div>
<div><h3>Fitted or fixed</h3><p>Old door removed, new one fitted, tested and explained.</p></div></div></div></section>'''

def faq_html(faqs):
    if not faqs: return ""
    items = "".join(f'<details><summary>{esc(f["q"])}</summary><div class="a"><p>{fix_links(f["a"].replace("{{PHONE}}", PHONE))}</p></div></details>' for f in faqs)
    return f'<section class="band"><div class="wrap"><h2>Frequently asked questions</h2><p class="lead">Straight answers to what people ask us most.</p><div class="faq">{items}</div></div></section>'

def schema(key):
    c = content[key]; m = meta[key]; graph = []
    biz = {"@type": "HomeAndConstructionBusiness", "@id": DOMAIN + "/#business", "name": BRAND, "url": DOMAIN + "/",
           "telephone": PHONE_TEL, "logo": DOMAIN + "/assets/logo.png", "image": DOMAIN + "/assets/van-side.png",
           "priceRange": "££", "areaServed": ["Milton Keynes"] + [meta[k]["label"] for k in by_section("area")],
           "address": {"@type": "PostalAddress", "addressLocality": "Milton Keynes", "addressRegion": "Buckinghamshire", "addressCountry": "GB"}}
    graph.append(biz)
    if key != "home":
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}]
        hub = HUB_OF.get(m["section"])
        if hub and hub in content:
            items.append({"@type": "ListItem", "position": 2, "name": meta[hub]["label"], "item": DOMAIN + url(hub, "abs")})
        items.append({"@type": "ListItem", "position": len(items) + 1, "name": m["label"], "item": DOMAIN + url(key, "abs")})
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    if m["section"] in ("door", "service", "brand"):
        graph.append({"@type": "Service", "name": c["h1"], "serviceType": m["label"], "provider": {"@id": DOMAIN + "/#business"}, "areaServed": "Milton Keynes"})
    if m["section"] == "guide":
        graph.append({"@type": "Article", "headline": c["h1"], "description": c["meta"], "author": {"@type": "Person", "name": AUTHOR, "url": DOMAIN + "/about/"},
                      "publisher": {"@id": DOMAIN + "/#business"}, "mainEntityOfPage": DOMAIN + url(key, "abs")})
    if c.get("faqs"):
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", f["a"]).replace("{{PHONE}}", PHONE)}} for f in c["faqs"]]})
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) + '</script>'

def footer():
    col = lambda t, s: f'<div><h4>{t}</h4><ul>' + "".join(f'<li><a href="{url(k)}">{esc(meta[k]["label"])}</a></li>' for k in by_section(s)) + '</ul></div>'
    return f'''<footer class="foot"><div class="wrap"><div class="grid">
<div class="brandbox"><img src="{asset("logo-white.svg")}" alt="{BRAND}" width="240" height="51"><p>Garage door supply, fitting, repairs and servicing across Milton Keynes and the surrounding towns.</p><p><strong style="color:#fff">Call:</strong> <a href="tel:{PHONE_TEL}">{PHONE}</a></p><ul><li><a href="{url("about")}">About us</a></li><li><a href="{url("brands")}">Brands we fit</a></li><li><a href="{url("contact")}">Get a free quote</a></li><li><a href="{url("privacy")}">Privacy</a></li></ul></div>
{col("Garage doors","door")}{col("Services","service")}{col("Areas","area")}{col("Guides","guide")}
</div><div class="legal"><span>© 2026 {BRAND}. All rights reserved.</span><span>Prices on this site are guides only and are confirmed after a free survey.</span></div></div></footer>
<div class="callbar"><a href="tel:{PHONE_TEL}">📞 Call now</a><a href="{url("contact")}">Free quote</a></div>'''

FORM_JS = '''<script>
document.querySelectorAll('form.qf').forEach(function(f){f.addEventListener('submit',function(e){
  if(PREVIEW||!ENDPOINT){e.preventDefault();f.innerHTML='<div class="ok">Thanks! Online quotes are being set up — please call us on '+PHONE+' and we\'ll help straight away.</div>';}
});});
</script>'''

def page(key):
    CUR["key"] = key
    c = content[key]; m = meta[key]; sec = m["section"]
    title = c["title"]; desc = c["meta"]
    canon = DOMAIN + url(key, "abs")
    hero_points = "".join(f"<li>{esc(p)}</li>" for p in c.get("hero_points", [])[:4])
    eyebrow = {"door": "Supplied & fitted in Milton Keynes", "service": "Local garage door service", "area": f"Garage doors in {m['label']}", "guide": "Garage door guide", "brand": "Brands we supply & repair", "hub": BRAND, "util": BRAND, "home": "Local garage door specialists"}[sec]
    ctas = f'<div class="ctas"><a class="btn btn-call" href="tel:{PHONE_TEL}">Call {PHONE}</a><a class="btn btn-ghost" href="{url("contact")}">Get a free quote</a></div>'
    if sec == "guide":
        initials = "".join(w[0] for w in AUTHOR.split()[:2] + AUTHOR.split()[-1:])[:2]
        side_art = f'<div class="hero-card"><h2>Need a professional?</h2><p style="margin:0 0 14px">Our Milton Keynes engineers can survey, quote, repair or replace.</p><a class="btn btn-call" href="tel:{PHONE_TEL}">Call {PHONE}</a></div>'
        byline = f'<div class="byline"><span class="avatar">MU</span><span>By {AUTHOR} · Updated October 2026</span></div>'
        heroextra = byline
    else:
        heroextra = ctas
        if key == "home":
            side_art = f'<div class="art"><img src="{asset("photos/"+photo("home")) if photo("home") else asset("hero.svg")}" alt="{BRAND} van outside a home with a new roller garage door" width="1200" height="760"></div>'
        elif key in A.DOOR_ART or photo(key):
            side_art = f'<div class="art"><img src="{art_src(key)}" alt="{esc(m["label"])} illustration" width="480" height="360"></div>'
        elif sec == "area" or sec == "brand" or key in ("about",):
            side_art = f'<div class="art"><img src="{asset("photos/"+photo(key)) if photo(key) else asset("photos/"+photo("van")) if photo("van") else asset("van-side.svg")}" alt="{BRAND} van livery" width="1200" height="520"></div>'
        elif key == "contact":
            side_art = f'<div class="hero-card"><h2>Request a free quote</h2>{quote_form("hero")}</div>'
        else:
            side_art = f'<div class="art"><img src="{asset("hero.svg")}" alt="" width="1200" height="760"></div>'
    h1 = esc(c["h1"])
    if key == "home":
        h1 = h1.replace("Milton Keynes", "<mark>Milton Keynes</mark>", 1)
    hero = f'''<section class="hero"><div class="wrap"><div class="copy">{crumbs(key)}<span class="eyebrow">{esc(eyebrow)}</span><h1>{h1}</h1><p class="sub">{esc(c.get("hero_sub",""))}</p>{"<ul class=points>"+hero_points+"</ul>" if hero_points else ""}{heroextra if sec!="guide" else ctas.replace("btn-ghost","btn-ghost") if False else heroextra}</div>{side_art}</div></section>'''
    trust = ""
    if sec in ("home", "door", "service", "area", "brand"):
        trust = '''<section class="trust"><div class="wrap"><div><b>£0</b>Free survey &amp; written quote</div><div><b>All</b>Makes &amp; models repaired</div><div><b>17</b>Door styles, made to measure</div><div><b>MK</b>Local team covering Milton Keynes</div></div></section>'''
    body = render_body(c["body"])
    author = ""
    if sec == "guide":
        author = f'<div class="author"><span class="avatar">MU</span><div><h3>About the author</h3><p><strong>{AUTHOR}</strong>. {esc(AUTHOR_BIO)} <a href="{url("about")}">More about us</a>.</p></div></div>'
    full = sec in ("util",) and key != "about"
    main = f'''<section class="main{" full" if full else ""}"><div class="wrap"><article class="prose">{body}{author}</article>{"" if full else sidebar(key)}</div></section>'''
    if key == "contact":
        main = f'''<section class="main"><div class="wrap"><article class="prose">{body}</article><aside class="side"><div class="box quote"><h3>Prefer to talk?</h3><p style="margin:0">Call our local team:</p><a class="big" href="tel:{PHONE_TEL}">{PHONE}</a><p class="fine" style="opacity:.85">Have a photo of the door handy if you can.</p></div></aside></div></section>'''
    extra = ""
    if sec == "hub" and SECTION_CHILD.get(key):
        kids = by_section(SECTION_CHILD[key])
        extra = f'<section class="band sky"><div class="wrap"><h2>All {esc(m["label"].lower())}</h2><p class="lead">Pick a page to read more.</p><div class="cards">' + "".join(card(k) for k in kids) + '</div></div></section>'
    if key == "home":
        extra = (f'<section class="band sky"><div class="wrap"><h2>Garage doors we supply &amp; fit</h2><p class="lead">Every major door style, made to measure for your opening.</p><div class="cards">' + "".join(card(k) for k in by_section("door")[:8]) + f'</div><p style="margin-top:22px"><a class="btn btn-blue" href="{url("garage-doors")}">See all garage doors</a></p></div></section>'
                 + f'<section class="band"><div class="wrap"><h2>Repairs, servicing &amp; automation</h2><p class="lead">Keeping existing doors working safely, whatever the make.</p><div class="cards">' + "".join(card(k, thumb=False) for k in by_section("service")) + '</div></div></section>'
                 + steps_band()
                 + f'<section class="band"><div class="wrap"><h2>Garage door guides</h2><p class="lead">Researched, plain-English advice by {AUTHOR}.</p><div class="cards">' + "".join(card(k, thumb=False) for k in by_section("guide")[:6]) + f'</div><p style="margin-top:22px"><a class="btn btn-blue" href="{url("guides")}">All guides</a></p></div></section>')
    rel = ""
    if sec in ("door", "service", "area", "guide", "brand"):
        rk = related(key)
        if rk:
            rel = f'<section class="band sky"><div class="wrap"><h2>{"Popular services in " + esc(m["label"]) if sec=="area" else "Related pages"}</h2><p class="lead">Keep exploring.</p><div class="cards">' + "".join(card(k, thumb=(sec!="guide")) for k in rk) + '</div></div></section>'
    if sec in ("door", "service"): rel += steps_band()
    areas = areas_band() if sec in ("home", "door", "service", "area", "hub", "brand") else ""
    head = f'''<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{DOMAIN}/assets/van-side.png"><meta name="theme-color" content="#14213D">
<link rel="icon" href="{asset("favicon.svg")}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Figtree:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{asset("style.css")}">{schema(key)}'''
    js = f"<script>var PREVIEW={'true' if MODE=='preview' else 'false'},ENDPOINT={json.dumps(FORM_ENDPOINT)},PHONE={json.dumps(PHONE)};</script>" + FORM_JS
    bodyhtml = header(key) + "<main>" + hero + trust + main + extra + rel + faq_html(c.get("faqs")) + areas + "</main>" + footer() + js
    if MODE == "preview" and key == "home":
        return head + "\n" + bodyhtml   # artifact wraps the index page in its own skeleton
    return f'<!doctype html>\n<html lang="en-GB"><head>{head}</head><body>{bodyhtml}</body></html>'

def write_assets():
    d = f"{OUT}/assets"; os.makedirs(d, exist_ok=True)
    open(f"{d}/logo.svg", "w").write(A.logo_svg())
    open(f"{d}/logo-white.svg", "w").write(A.logo_svg(dark_text="#FFFFFF", sub=A.SUN))
    open(f"{d}/logo-stacked.svg", "w").write(A.logo_stacked())
    open(f"{d}/favicon.svg", "w").write(A.favicon())
    open(f"{d}/van-side.svg", "w").write(A.van_side(phone=PHONE))
    open(f"{d}/van-passenger.svg", "w").write(A.van_side(phone=PHONE, flip=True, uid="p"))
    open(f"{d}/van-rear.svg", "w").write(A.van_rear(phone=PHONE))
    open(f"{d}/hero.svg", "w").write(A.hero_scene(PHONE))
    for k, fn in A.DOOR_ART.items():
        open(f"{d}/door-{k}.svg", "w").write(fn())
    shutil.copy(f"{ROOT}/style.css", f"{d}/style.css")
    for src, dst in (("print/van-driver-side.png", "van-side.png"), ("print/logo-primary.png", "logo.png")):
        if os.path.exists(f"{ROOT}/{src}"): shutil.copy(f"{ROOT}/{src}", f"{d}/{dst}")
    if os.path.isdir(PHOTO_DIR):
        os.makedirs(f"{d}/photos", exist_ok=True)
        for f in os.listdir(PHOTO_DIR): shutil.copy(f"{PHOTO_DIR}/{f}", f"{d}/photos/{f}")

def main():
    os.makedirs(OUT, exist_ok=True)
    # remove only previously generated pages/assets (safe inside a git repo)
    for k in meta:
        p = f"{OUT}/{k}" if MODE == "live" else f"{OUT}/{k}.html"
        if k != "home" and os.path.isdir(p): shutil.rmtree(p)
    if os.path.isdir(f"{OUT}/assets"): shutil.rmtree(f"{OUT}/assets")
    write_assets()
    # thank-you page (generated, not in content)
    for key in LIVE:
        h = page(key)
        if MODE == "preview":
            path = f"{OUT}/{url(key)}"
        else:
            path = f"{OUT}/index.html" if key == "home" else f"{OUT}/{key}/index.html"
            os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w").write(h)
    if MODE == "live":
        sm = "".join(f"<url><loc>{DOMAIN}{url(k,'abs')}</loc><changefreq>monthly</changefreq><priority>{'1.0' if k=='home' else '0.8' if meta[k]['section'] in ('door','service','hub') else '0.6'}</priority></url>" for k in LIVE if k != "privacy")
        open(f"{OUT}/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>')
        open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    print("built", len(LIVE), "pages ->", OUT)

if __name__ == "__main__":
    main()
