# Content brief — garage-doors-milton-keynes.co.uk

A rank-and-rent local lead-generation website for **Garage Doors Milton Keynes** — a local garage door supply, fitting, repair and servicing service covering Milton Keynes and surrounding towns (Bletchley, Newport Pagnell, Olney, Wolverton, Stony Stratford, Buckingham, Leighton Buzzard, Towcester, Woburn Sands, Cranfield, Winslow, Bedford, Northampton, Aylesbury). The business is written in the first person plural ("we", "our fitters"). Every page should push towards a phone call or free quote.

## Files
- `plan.py` — full list of pages (slug, section, label, primary keyword, related slugs). ONLY link to slugs that exist there.
- `keywords.json` — per-page keyword lists from Ahrefs (volume in brackets). Use the primary keyword in the title, H1, first paragraph and one H2. Weave the other keywords naturally into H2s/H3s/body/FAQs (no stuffing; natural UK English). Ignore obviously irrelevant keywords (US places like "bedford county", "winslow township").

## Output format
Write one JSON file per page to `/home/claude/site/content/<slug>.json` (home page slug = `home`). UTF-8, valid JSON (validate with `python3 -c "import json;json.load(open(f))"` for every file you write).

```json
{
  "slug": "roller-garage-doors",
  "title": "Roller Garage Doors Milton Keynes | Supplied & Fitted",   // ≤ 60 chars
  "meta": "…",              // 140–158 chars, includes primary keyword + call to action
  "h1": "Roller Garage Doors in Milton Keynes",
  "hero_sub": "…",          // 1–2 sentences under the H1
  "hero_points": ["…","…","…"],   // 3 short benefit bullets (≤ 6 words each)
  "summary": "…",           // ≤ 150 chars, used on cards in hubs/related sections
  "body": "<h2>…</h2><p>…</p>…",  // main content HTML, see rules
  "faqs": [{"q":"…","a":"…"}]     // 4–6 FAQs, answers 40–90 words, plain text (may include <a> links)
}
```

### Body HTML rules
- Allowed tags: `h2 h3 p ul ol li strong em a table thead tbody tr th td blockquote`, plus `<div class="callout">…</div>` (tip/notice box) and `<div class="cta-inline"></div>` (empty — the template fills it with a quote/call banner; put ONE roughly mid-body on money pages).
- No `h1`, no images, no inline styles, no scripts.
- Internal links are root-relative with a trailing slash: `<a href="/sectional-garage-doors/">sectional garage doors</a>`. Home = `/`. Contact/quote = `/contact/`. Brand pages use slugs like `/brand-hormann/`.
- Each page needs 6–12 contextual internal links with descriptive, varied anchor text (not "click here"), including: its hub (`/garage-doors/`, `/services/`, `/areas/`, `/guides/` or `/brands/`), at least 2 sibling pages in the same section, at least 1 page in another section (e.g. a guide links to a money page; a money page links to a guide), and `/contact/`.
- Phone number: write `{{PHONE}}` wherever a number appears (template swaps it).
- Price tables: use `<table>` with columns like Door type | Typical fitted price | Notes. Prices are **indicative UK guide ranges** (e.g. "from £…", "£900–£1,600") and must be labelled as a guide confirmed after a free survey. Keep them realistic for the UK in 2026.

### Word counts (body only)
- Door type & service pages: 1,000–1,400 words
- Guides: 1,200–1,700 words (genuinely helpful, answers the question in the first paragraph, then depth)
- Brand pages: 700–1,000 words
- Area pages: 650–900 words, each **genuinely unique** (local estates/villages/postcodes, housing stock, typical door jobs there, travel/coverage). Link to 4+ door/service pages and the 2 nearest other area pages.
- Hubs: 400–700 words (the template also auto-lists every child page as cards)
- Home: 1,100–1,500 words

### Tone & accuracy rules (important)
- British English spelling (colour, aluminium, metres, organise). Friendly, expert, plain-speaking tradesperson voice. Short paragraphs, scannable H2/H3s, lists where useful.
- **Do not invent**: customer reviews/testimonials, star ratings, review counts, named customers, years in business ("established 1998"), numbers of doors fitted, staff names, street addresses, company numbers, awards, or accreditations/memberships (no "Hörmann approved", "Which? Trusted Trader", "Checkatrade", "Secured by Design certified installer", etc.). You may say we supply and fit doors from leading manufacturers and explain what standards like LPS 1175, PAS 24 or Secured by Design mean as general information.
- Service promises should be modest and believable: "free, no-obligation quotes", "we aim to get to repairs quickly — often the same or next day", "all major makes repaired", "clear written quotes", "guarantee details provided with your quote".
- Do not disparage named competitors (e.g. Garolla). Brand pages describe the manufacturer's product range factually and what we can do (supply, fit, repair, service, automate) — no claim of official dealer status.
- Local facts must be accurate. If unsure about a local detail, keep it general rather than inventing it.
- Guides are authored by **Muhammad Usman Siddiqui** (the template adds the author box). Write guides in a helpful editorial voice; it's fine for them to mention "our engineers in Milton Keynes" occasionally and end with a soft CTA.
- Safety: for spring/cable guidance, say tensioned springs and cables are dangerous and should be handled by a professional — don't give step-by-step DIY spring tensioning instructions.
