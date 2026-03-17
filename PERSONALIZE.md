# Personalize This Academic Site

This repo is already a good base for a personal academic homepage. The main files you will usually edit are:

- `_config.yml`: site title, name, URL, layout width, and global options
- `_pages/about.md`: homepage biography and profile image block
- `_data/socials.yml`: email, GitHub, LinkedIn, Google Scholar, ORCID, and similar links
- `_bibliography/papers.bib`: publications shown on the publications page
- `assets/json/resume.json`: CV data used by the CV page
- `assets/img/prof_pic.jpg`: profile photo on the homepage

## Common Changes

### 1. Make the site wider

Edit `_config.yml`:

```yml
max_width: 1100px
```

Increase this further if you want, for example `1200px`.

### 2. Remove the left sidebar table of contents

The sidebar with entries like `Work`, `Education`, `Grants`, and `Publications` comes from page front matter such as:

```yml
toc:
  sidebar: left
```

Remove that block from a page to disable the sidebar for that page.

### 3. Update the homepage

Edit `_pages/about.md`:

- biography text
- profile image filename
- location / affiliation block
- whether to show selected papers and social links

### 4. Update the CV page

Edit `assets/json/resume.json` for:

- work experience
- education
- grants
- languages

If you prefer the YAML CV format instead, delete `assets/json/resume.json` and the site will fall back to `_data/cv.yml`.

### 5. Update publications

Edit `_bibliography/papers.bib` and keep one BibTeX entry per publication.

### 6. Add your PDF CV

Put your PDF in `assets/pdf/`, for example:

`assets/pdf/cv.pdf`

Then uncomment this line in `_pages/cv.md`:

```yml
cv_pdf: cv.pdf
```

## Good Next Cleanups

If you want the site to feel less like the original template, the next things to trim are:

- sample blog posts in `_posts/`
- sample projects in `_projects/`
- sample announcements in `_news/`
- pages you do not want in `_pages/`

You can either delete them or exclude them in `_config.yml`.
