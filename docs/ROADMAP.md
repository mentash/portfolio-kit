# Portfolio Kit — Roadmap

This roadmap tracks where the project is **now**, what's **next (short-term)**, and the **long-term** vision. It is deliberately incremental so each step is a focused Django learning exercise. Detailed, implementable work items live in `docs/AGILE_BACKLOG.md`.

Guiding principles:
- Start with the **simplest single-person portfolio** and make it genuinely good.
- Defer multi-tenancy, custom domains, themes, and SaaS concerns until the core is solid.
- Every phase has a clear **learning objective** — the point is to master Django, not just ship features.

---

## Current state (as of now)
A working but minimal Django project.

**Implemented**
- Django 6 project (`config/`) with the `apps.core` app installed.
- Models (`apps/core/models.py`): `Profile` (name, email, bio), `Education`, `Certification`, `Experience`, `Skill` (proficiency 1–10), `Project`, and `ProjectExperience` (a many-to-many "through" table linking projects and experiences). Everything is linked to `Profile` by a ForeignKey.
- Admin (`apps/core/admin.py`): `Profile` editing with inline `Education`, `Experience`, and `Skill`; `Certification` and `Project` registered separately.
- Views/URLs (`apps/core/views.py`, `apps/core/urls.py`): `/` lists **all** profiles; `/profile/<pk>/` shows one profile's experience and skills.
- Templates: project-level base at `templates/config/base.html` (Bootstrap 5 via CDN); `core/home.html` (profile list) and `core/profile_detail.html` (name, email, bio, experience, skills).
- SQLite database with the initial migration applied.

**Known gaps / inaccuracies to fix**
- The site currently behaves like a multi-profile directory, not a single-person portfolio.
- `profile_detail.html` renders Experience and Skills only — **Education, Certifications, and Projects are not shown yet**.
- No Hero/About/Contact sections.
- No contact form, `ContactMessage` model, or email sending.
- `STATICFILES_DIRS` points to a `static/` folder that **does not exist yet**.
- `SECRET_KEY`/`DEBUG`/email are hard-coded in `settings.py` (no `.env`), even though `django-environ` is installed.
- `requirements.txt` contains many unrelated packages (FastAPI, google-adk, uvicorn, …) from a shared environment and should be trimmed.
- `README.md` referenced `config/templates`, but templates actually live under the project-level `templates/` directory.

---

## Short-term (now → next): a polished single-person portfolio
**Goal:** turn the current multi-profile prototype into the simplest, good-looking, single-person portfolio with a real UI — still treating this as *my own* portfolio, not a product.

**Outcomes**
1. **Single-profile homepage.** `/` renders my one portfolio directly (no list). Keep the multi-profile model under the hood for future multi-tenancy.
2. **Complete the content sections.** Render all existing data: About/Bio, Experience, Skills, Education, Certifications, and Projects (with project ↔ experience links).
3. **Real UI & static assets.** Create the `static/` folder, add custom CSS/JS, a responsive navbar, section anchors, and smooth scrolling. Make it look intentional.
4. **Contact form.** A working contact section that validates input, saves a `ContactMessage` to the DB, and emails me (console backend in dev). Use POST → redirect → GET with the messages framework for success feedback.
5. **Config & dependency hygiene.** Move secrets/config to `.env` via `django-environ`, add `.env.example`, create the missing `static/` dir, and trim `requirements.txt` to what the project actually uses.
6. **First tests.** Basic tests for model `__str__`, view responses, and contact-form validation.

**Django you'll learn:** the request/response cycle, the ORM and related managers, `get_object_or_404`, template inheritance and tags, the staticfiles app, `ModelForm` and validation, CSRF, the messages framework, email backends, 12-factor settings, and the Django test client.

---

## Long-term (later): from personal portfolio to themeable SaaS
Pursue these **only after** the single-person portfolio is solid. Each is a substantial epic.

1. **Multi-tenancy / accounts.** User registration and login; each user owns and edits their own profile; a per-user dashboard; ownership/permission checks. (The data model already anticipates this.)
2. **Audience tiers.** Introduce Teams and Companies (organizations, memberships, roles) on top of Personal/Professional, with the right access control.
3. **Custom domains & subdomains.** Map each portfolio to a subdomain or custom domain (e.g. via the Sites framework + host-based routing/middleware).
4. **Built-in switchable themes.** Per-portfolio theme selection using pre-purchased templates such as **Tabler** and **Litho** (ThemeForest). Kept high-level for now; design details deferred to a future phase.
5. **SaaS productization.** Subscription plans/billing, feature/theme gating by plan, onboarding flows, and admin/operations tooling.
6. **API & decoupled frontend.** A public REST API (Django REST Framework) and optionally a React/Vue frontend consuming it.
7. **Media & production readiness.** Image/avatar uploads, Postgres, static/media hosting, security hardening, and CI/CD.

**Django you'll learn:** authentication & authorization, multi-tenant data modeling, the Sites framework and middleware, class-based views, DRF, file/media handling, caching, and deployment.
