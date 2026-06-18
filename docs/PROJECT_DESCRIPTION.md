# Portfolio Kit (Django) — Project Description

## What this is
Portfolio Kit is a Django web app for building professional portfolio websites.
**Right now it is intentionally scoped as a single-person portfolio** — my own portfolio — so I can learn real Django end-to-end. The longer-term vision is to grow it into a multi-tenant, themeable, SaaS-style product that anyone can use.

## Primary goal: learning
The number one goal of this project is to learn and master **Django** (and good software-engineering practice) by building something real, in small, understandable increments:
models → admin → views/urls → templates → static assets → forms/email → tests → settings/deploy.
This repo is built by hand for learning. AI is used to plan, explain, and review — not to write the application code for me.

## Audience (long-term vision)
The product is designed to eventually serve four tiers:
- **Personal** — individuals showcasing a single portfolio.
- **Professionals** — freelancers/consultants who want a polished, themed presence.
- **Teams** — small groups sharing a branded, multi-member presence.
- **Companies** — organizations with multiple members and custom domains.
We start with **Personal** only.

## Current scope (now)
- A single-person portfolio rendered with Django templates + Bootstrap 5.
- Portfolio content (profile, experience, skills, education, certifications, projects) is **database-driven** and edited through **Django Admin**.
- The data model already supports multiple profiles, but the UI deliberately exposes **one** profile for now. Multi-tenancy is deferred (see `docs/ROADMAP.md`).

## Tech stack
- Backend: Django 6 (Python 3.12+)
- UI: Django templates + Bootstrap 5 (CDN today; bundled assets later)
- Database: SQLite (development)
- Config: `django-environ` for environment-based settings (planned; see backlog)

## Current architecture
- `apps/core/` — domain models, admin, views, urls (forms/email to be added).
- `config/` — project settings, root urls, wsgi/asgi.
- `templates/` — project-level templates. The base layout lives at `templates/config/base.html`; app templates (e.g. `apps/core/templates/core/`) extend it via `{% extends 'config/base.html' %}`.
- `static/` — css/js/images (referenced in settings, **not created yet** — a short-term task).
- `db.sqlite3` — local development database.

## Theming (future, high-level)
A later phase introduces **built-in, switchable themes** based on pre-purchased templates (e.g. **Tabler** and **Litho** from ThemeForest), selectable per portfolio. This is intentionally out of scope for now and captured only as a future epic in the roadmap/backlog.

## Development workflow
1. Activate the virtual environment: `.venv\Scripts\Activate.ps1` (PowerShell on Windows).
2. Apply migrations: `python manage.py migrate`
3. Create an admin user: `python manage.py createsuperuser`
4. Run the dev server: `python manage.py runserver`
5. Edit content at `/admin/`, view the site at `/`.

## Related docs
- `docs/ROADMAP.md` — current, short-term, and long-term plans.
- `docs/AGILE_BACKLOG.md` — implementable, learning-first work items.
