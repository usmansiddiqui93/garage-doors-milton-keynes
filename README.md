# garage-doors-milton-keynes.co.uk

Rank & rent website for **Garage Doors Milton Keynes**: 72 static pages, all linked to each other.

| Section | Pages |
|---|---|
| Home + hubs | Home, Garage Doors, Services, Areas, Guides, Brands |
| Door types | 17 (roller, sectional, up & over, side hinged, electric, insulated, wooden, steel, GRP, aluminium, composite, double, bespoke, side doors, with windows, modern & colours, secure) |
| Services | 8 (repairs, electric repairs, springs & cables, servicing, replacement, installation, automation, prices) |
| Brands | 6 (Hörmann, Garador, Cardale, Novoferm, SWS, Henderson) |
| Areas | 14 (Bletchley, Newport Pagnell, Olney, Wolverton, Stony Stratford, Buckingham, Leighton Buzzard, Towcester, Woburn Sands, Cranfield, Winslow, Bedford, Northampton, Aylesbury) |
| Guides | 17 topical-authority articles by Muhammad Usman Siddiqui |

Each page includes schema markup (LocalBusiness, Service, Article, FAQPage, BreadcrumbList), a canonical URL, breadcrumbs, related-page cards, area links, a sitemap.xml entry and a quote form.

## Before going live
Edit the settings at the top of `_src/build.py`, then rebuild:
- `PHONE` / `PHONE_TEL`: your call-tracking number (currently the placeholder 01908 000000)
- `FORM_ENDPOINT`: a Formspree (or similar) form URL so quote requests reach your inbox. Until you set it, the form asks visitors to call.
- `_src/content/privacy.json`: fill in the [bracketed] placeholders.

## Rebuild
```bash
cd _src && python3 build.py live ..
```
Page copy lives in `_src/content/<slug>.json` and the site structure in `_src/plan.py`. Links are relative, so the site works on GitHub Pages and on a custom domain.

**Photos:** put a photo named after a page's slug (for example `_src/photos/roller-garage-doors.jpg`, `_src/photos/van.jpg` or `_src/photos/home.jpg`) and rebuild. It replaces that page's illustration.

## Custom domain
In Settings → Pages, add `www.garage-doors-milton-keynes.co.uk`. At your registrar, add a CNAME record from `www` to `usmansiddiqui93.github.io`.

## Print pack
`print-pack/` holds the van livery PDF (driver side, passenger side, rear, logo set, business card) plus high-res PNG and SVG files.
