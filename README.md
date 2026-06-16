# Lazy Language Club — landing page

Static landing page for **Lazy Language Club** — a "language tasting": 4 evenings in a
small Belgrade art gallery, group of up to 10, shadowing method (listen to a native via
QR → headphones, then speak with a partner). Goal: collect applications for the founding
cohort via a Google Form.

Plain HTML + CSS + a sprinkle of native JS. No framework, no build step — so it loads fast
and Google indexes it cleanly.

## Files

| File | What it is |
|------|------------|
| `index.html` | English landing page (entry point) |
| `sr.html` | Serbian version (SEO + local audience) |
| `404.html` | Branded not-found page |
| `favicon.svg` | Mascot favicon |
| `og-image.png` | Social-share image (1200×630), generated from `og-image.svg` |
| `og-image.svg` | Editable source for the social image |
| `robots.txt` | Allows crawling, points to the sitemap |
| `sitemap.xml` | Both pages, with hreflang alternates |
| `netlify.toml` | Netlify config (no build, security headers) |
| `nelli.jpg` | _(optional)_ guide photo — drop it in and it appears automatically |

## Status

- ✅ **Google Form** is wired into the "Apply" buttons on both pages (opens in a new tab).
- ✅ **Domain** is set to `https://lazy-language-club-belgrade.netlify.app`. If that ever
  changes, find-and-replace it across `index.html`, `sr.html`, `robots.txt`, `sitemap.xml`.
- ✅ **Guide photo** `nelli.jpg` is in place.

## Ads & analytics

Tracking is staged but **inactive**. To turn it on:

1. In the `<head>` of `index.html` **and** `sr.html`, find the `ADS / ANALYTICS` comment
   block, uncomment the snippet(s) you need, and replace `G-XXXXXXXXXX` (GA4 / Google Ads)
   or `YOUR_PIXEL_ID` (Meta/Instagram Pixel) with your real IDs.
2. The "Apply" buttons carry `data-cta="apply"`. A small script at the bottom of `<body>`
   automatically fires a conversion event (`apply_click` for GA4, `Lead` for Meta) the moment
   any tag is live — no extra wiring needed.
3. **Consent:** the audience is partly EU/Serbia, so the lawful approach is to load the
   tags only after the visitor accepts cookies. A consent banner isn't included yet — ask
   for one when you pick your ad platform, or load tags via Google Consent Mode.

`privacy.html` (linked in both footers) is required for Google Ads approval and covers the
Google Form + tracking. The Serbian half is a draft — have a native speaker review it.

## Reviews block

A styled, ready-to-go testimonials section is included **commented out** in both pages
(search for `REVIEWS` / `RECENZIJE`). When you have real quotes, uncomment it and drop them
in. Don't invent quotes.

## Local preview

Open `index.html` in a browser, or run a tiny server:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Deploy

Connected to Netlify via GitHub — pushing to `main` redeploys automatically.

## Regenerating the social image (macOS)

```bash
qlmanage -t -s 1200 -o . og-image.svg && mv og-image.svg.png og-image.png
sips -c 630 1200 og-image.png
```
