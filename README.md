# Portfolio App

A Django-based single-person portfolio application using Tabler UI.

## Tech Stack
- Python 3.12+
- Django 6
- Tabler UI (admin dashboard framework, repurposed for portfolio)
- SQLite (development)

## Project Structure
- `apps/core/` — portfolio domain models, views, templates, admin, tests
- `config/` — Django project settings and root URL config
- `templates/` — project-level templates (including `base.html`)
- `static/` — Tabler assets and project-specific CSS/JS
- `docs/` — project notes, roadmap, and backlog

## Quick Start
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the dev server: `python manage.py runserver`
6. Visit `http://127.0.0.1:8000/` to see your portfolio
7. Edit content at `http://127.0.0.1:8000/admin/`

## Features
- **Single-person portfolio:** one profile, multiple content sections
- **Responsive design:** works on desktop, tablet, and mobile
- **All sections visible:** About, Experience, Skills, Education, Certifications, Projects
- **Smooth navigation:** sticky navbar with section links
- **Admin-managed content:** all data edited through Django Admin

## How to Add Content
1. Log in to `/admin/`
2. Create/edit your Profile (name, email, bio)
3. Add Experience, Skills, Education, Certifications, Projects
4. They appear automatically on the public site