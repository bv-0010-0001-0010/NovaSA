# Nova Construction Solutions SA

Static, responsive website for Nova Construction Solutions SA Pty Ltd. The
project uses plain HTML, CSS and JavaScript and is configured for Vercel.

## Project files

- `index.html` — home page
- `services.html`, `industries.html`, `about.html`, `for-workers.html`,
  `contact.html` — main site pages
- `privacy.html`, `terms.html`, `404.html` — supporting pages
- `css/style.css` — responsive styles and brand tokens
- `js/main.js` — mobile navigation, scroll reveals and enquiry form
- `apps-script/` — optional Google Apps Script enquiry-form backend
- `build.py` — regenerates the HTML from shared templates
- `vercel.json`, `robots.txt`, `sitemap.xml` — hosting and search configuration

The header, footer and page content are generated from `build.py`. After
changing the templates, regenerate the pages with:

```bash
python3 build.py
```

## Local preview

From the project directory, run:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploying to Vercel

Create a **new GitHub repository** for this site and push this project to it.
Do not use the reference site's repository as the deployment target. Import the
new repository into Vercel with the **Other** framework preset; no build command
or output directory is required.

Once the domain purchase is complete, add `novaconstructions.com.au` and
`www.novaconstructions.com.au` to the Vercel project. Use the DNS records Vercel
provides in Hostinger, and make the chosen primary domain consistent with the
canonical URLs in `build.py`.

## Contact form

The form is not live until the Apps Script endpoint is configured. Follow
`apps-script/SETUP.md`, then replace the placeholder `FORM_ENDPOINT` in
`js/main.js` with the deployed endpoint URL. Test that submissions reach the
Google Sheet and the `admin@novaconstructions.com.au` inbox before launch.

## Launch checklist

- [ ] Confirm the final service descriptions and South Australia coverage.
- [x] Add the supplied company logo.
- [ ] Add approved project photography.
- [ ] Confirm business registration details, including ABN, before publishing.
- [ ] Configure and test the enquiry form and confirmation email.
- [ ] Connect the purchased domain to Vercel and verify HTTPS.
- [ ] Have the privacy policy and terms reviewed for the actual business.
- [ ] Submit the sitemap to Google Search Console after launch.

The registered office address and service area currently shown were supplied
for development. Legal and service claims should be checked by the client before
publication.

The header and footer use the supplied transparent SVG logo, with the PNG as a
fallback.
