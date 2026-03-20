# Solomon's MRI Lab Website

This repository contains the source code for **Solomon's MRI Lab** website, built on top of the [Jekyll](https://jekyllrb.com/) + al-folio stack.

The site is focused on:
- Presenting the lab mission and research directions
- Highlighting publications and featured work
- Sharing team profiles, news, and opportunities
- Keeping a clean light/dark user experience

## What We Are Building

The website is a lab-facing communication platform that combines:
- A strong visual homepage and hero-driven layout
- Dedicated pages for research areas (Computational MRI, Motion Correction, Smart Sensors)
- Publications powered by BibTeX (`_bibliography/papers.bib`)
- Team and profile pages under `_pages/team/`

This repo is also structured so content updates are simple: most edits happen in Markdown and YAML, while layout/styling lives in Liquid and SCSS.

## Quick Start (Recommended: Docker)

### 1. Start locally

```bash
docker compose pull
docker compose up
```

Then open: `http://localhost:8080`

### 2. Stop the local server

Press `Ctrl+C` in the running terminal, then:

```bash
docker compose down
```

## Main Files You Will Edit Often

- `_config.yml`: site-wide settings (title, nav behavior, feature flags)
- `_pages/home.md`: homepage content
- `_pages/*.md`: static pages
- `_pages/team/*.md`: team profiles
- `_bibliography/papers.bib`: publications
- `_data/featured_publications.yml`: featured/latest publication cards
- `_includes/header.liquid`: navbar
- `_includes/hero.liquid`: hero banner markup
- `_sass/_navbar.scss`: navbar styling
- `_sass/_layout.scss`: layout and hero styling

## Typical Update Workflows

### A) Update text/content

1. Edit the relevant markdown file in `_pages/`.
2. Save and reload `http://localhost:8080`.
3. Verify both light and dark modes.

### B) Add or update publications

1. Edit `_bibliography/papers.bib`.
2. Keep valid BibTeX format.
3. Reload `/publications/` and confirm entries render.

### C) Update navigation/menu

1. Edit page frontmatter (`nav`, `nav_order`, dropdown structure in page metadata).
2. If needed, adjust `_includes/header.liquid`.
3. Verify desktop and mobile navigation in both themes.

### D) Update visual styling

1. Edit SCSS under `_sass/`.
2. Reload and verify responsive behavior.
3. Validate dark mode parity for changed components.

## Light/Dark Theme Notes

The site supports both light and dark mode based on user preference and toggle state.

When modifying UI components:
- Always test in both themes
- Ensure menus, dropdowns, overlays, and text contrast are consistent
- Avoid hardcoded colors unless they are intentionally themed

## Quality Checks Before Commit

Run these before committing:

```bash
npx prettier . --write
```

Then run local site check:

```bash
docker compose up
```

Manual checks:
- Home page renders correctly
- Navbar works on desktop/mobile
- Dropdowns look correct in dark mode
- Hero banners and page headers render correctly
- Publications page loads without BibTeX errors

## Deployment

Deployment is handled by GitHub Actions workflows in `.github/workflows/`.

For successful deploys:
- Keep `_config.yml` valid YAML
- Avoid broken Liquid syntax
- Keep frontmatter valid in Markdown files

## Project Structure (High Level)

```text
_config.yml
_bibliography/        # BibTeX publications
_data/                # YAML data files
_includes/            # Reusable Liquid components
_layouts/             # Page layout templates
_pages/               # Main site pages
_posts/               # Blog posts
_projects/            # Project entries
_sass/                # SCSS styles
assets/img/           # Images
```

## Troubleshooting

- If `8080` is busy: run `docker compose down` and restart.
- If styles/scripts look stale: hard refresh browser.
- If build fails on YAML/Liquid: check indentation, quotes, and frontmatter blocks.

For deeper details, see:
- `CUSTOMIZE.md`
- `TROUBLESHOOTING.md`
- `INSTALL.md`
