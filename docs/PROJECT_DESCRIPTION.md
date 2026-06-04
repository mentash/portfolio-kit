# Portfolio App (Django) — Project Description

## Goal
Build a personal portfolio web app to learn **real Django workflow** end-to-end: models → admin → views/urls → templates → static assets.

## Phase 1 Scope (Single-page portfolio)
- One public page (`/`) with sections: **Hero, About, Skills, Projects, Experience, Education, Contact**
- Content is **database-driven** and managed through **Django Admin**
- Contact form:
  - Saves messages to DB
  - Sends email notification to:
    1) your personal email, and
    2) the portfolio official contact email (configured in settings)

## Tech Stack
- Backend: Django 6
- UI: Django Templates + Bootstrap 5 (CDN) + small custom CSS/JS
- DB: SQLite (dev)

## High-Level Architecture
- `apps/core/` — domain models, views, forms, urls, admin
- `templates/` — base layout + core page
- `static/` — css/js/images

## Development Workflow
1. Activate venv: `.venv\Scripts\Activate.ps1`
2. Run migrations: `python manage.py migrate`
3. Create admin user: `python manage.py createsuperuser`
4. Start server: `python manage.py runserver`
5. Manage content at: `/admin/`

## Future Phases (not in Phase 1)
- Company portfolios (multi-tenant or organization profiles)
- Public API with Django REST Framework
- React/Vue frontend consuming the API
