# Jacky Liao — academic homepage

A build-free HTML, CSS, and JavaScript website. No Jekyll, Ruby, npm, or package installation is required.

## Preview

```sh
python3 -m http.server 8000 --directory public
```

Open http://localhost:8000.

## Edit

- `public/index.html`: introduction, news, selected projects, experience, honors, and funding.
- `public/assets/academic-home/home.css`: homepage styles, including the compact spacing rules at the end.
- `public/assets/academic-home/home.js`: publication filters.
- `public/data/publications.json`: publication records.
- `public/assets/academic-home/images/`: research figures and portrait.
- `public/assets/pdf/CV.pdf`: CV download.

After editing publication data, run `python3 tools/update_publications.py` to refresh its static HTML. This optional maintenance script is not needed to serve or deploy the site. Validate local links with `python3 tools/check_site.py`.

## Existing pages

The existing project pages, Japanese page (`/jp.html`), news, and blog URLs are retained as static HTML with their supporting assets. They are snapshots of the previous site and can be edited directly; they no longer depend on Jekyll or Liquid. The homepage uses its own styles, preserving the appearance of those pages.

## Deployment

GitHub Actions validates and publishes `public/` to the existing `gh-pages` branch on pushes to `main` or `master`. This retains the previous deployment method without the Jekyll build. Pull requests validate without deploying. The `.nojekyll` file prevents GitHub Pages from processing the output with Jekyll.

## Migration backup

The previous working tree, including uncommitted homepage edits and local development files, is preserved outside this repository at:
`/Users/koike19/Desktop/Progress/repository-backups/liaochenchieh-before-static-20261118`

Git history remains in this repository. No commit or push was made during migration.

## English / 日本語

The language switch links `/` and `/jp.html` and preserves the current section. Both are static pages and work without JavaScript; JavaScript handles filters and section preservation. Paper titles and author names retain their original published language.

Edit Japanese introduction text in `public/data/intro-ja.html`, and interface/section translations in `public/data/ja.json`. After editing English content or translations, run `python3 tools/update_japanese.py`. Updating publication records with `tools/update_publications.py` also refreshes the Japanese page. No build is required for serving or deployment.
