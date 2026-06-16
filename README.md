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

## Before going live — two things to replace

1. **Google Form link.** Search both `index.html` and `sr.html` for
   `REPLACE_WITH_GOOGLE_FORM_LINK` and paste your form URL.
2. **Domain.** All SEO URLs use the placeholder
   `https://lazy-language-club-belgrade.netlify.app`. If your Netlify site name (or custom
   domain) is different, find-and-replace that string across `index.html`, `sr.html`,
   `robots.txt`, and `sitemap.xml`.

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
