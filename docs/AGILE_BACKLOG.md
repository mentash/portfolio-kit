# Agile Backlog — Portfolio Kit

Implementable, learning-first work items. The backlog is ordered so each item is a small Django lesson you can build by hand. It is aligned with `docs/ROADMAP.md`.

How to use this:
- Work top to bottom. Finish and verify one feature before starting the next.
- For each feature, read the **Django concepts** first, then attempt the **tasks** yourself.
- "Done" means the acceptance criteria pass and you can explain *why* it works.

Legend: **[Now]** = short-term (current focus), **[Later]** = long-term (do not start yet).

---

## Epic: Single-person portfolio [Now]
Turn the current multi-profile prototype into a clean, single-person portfolio with a real UI.

### Feature 1 — Single-profile homepage
**User story**
- As a visitor, I land on `/` and immediately see *the* portfolio (not a list of people).

**Acceptance criteria**
- `/` renders one profile's content directly.
- If no profile exists, the page shows a friendly empty state instead of erroring.
- The old "list of profiles" behavior is removed from the home page (the multi-profile model stays in place).

**Tasks**
- Decide how to select the single profile (e.g. the first profile, or one flagged active).
- Update the `home` view to fetch that one profile and pass it to the template.
- Update `home.html` to render the profile (or reuse the detail layout).

**Django concepts you'll learn:** querysets and `.first()`, view → template context, handling the empty/`None` case, `{% if %}` in templates.

---

### Feature 2 — Complete the content sections
**User story**
- As a visitor, I can see the full portfolio: About, Experience, Skills, Education, Certifications, and Projects.

**Acceptance criteria**
- All six sections render from the database.
- Education, Certifications, and Projects (currently missing in the template) are displayed.
- Projects show their linked experiences where relevant.
- Sensible ordering (e.g. most recent experience first).

**Tasks**
- Extend the template to loop over the `education`, `certifications`, and `projects` related managers.
- Add `Meta.ordering` to models where ordering matters, or order in the view.
- Add `{% empty %}` fallbacks for each list.

**Django concepts you'll learn:** reverse relations / related managers, `ManyToMany` traversal, template `for`/`empty`, model `Meta.ordering`.

---

### Feature 3 — Real UI & static assets
**User story**
- As a visitor, the portfolio looks polished and works on mobile.

**Acceptance criteria**
- A `static/` directory exists and is loaded via `{% static %}` (the current settings warning is gone).
- There is a responsive navbar with anchor links to each section and smooth scrolling.
- Custom CSS provides intentional spacing, typography, and a hero section.

**Tasks**
- Create `static/css/`, `static/js/`, `static/images/` with a small `style.css` and `main.js`.
- Add `{% load static %}` in the base template and wire the assets.
- Build a hero/about block and section navigation.

**Django concepts you'll learn:** the staticfiles app, `STATICFILES_DIRS` vs `STATIC_ROOT`, `{% static %}`, `collectstatic` (for later).

---

### Feature 4 — Contact form (persistence + email)
**User story**
- As a visitor, I can send a message; as the owner, I receive it by email and it's saved.

**Acceptance criteria**
- A `#contact` section with a CSRF-protected form.
- On valid submit: a `ContactMessage` row is saved **and** an email is sent (console backend in dev) to the owner and the official contact address.
- After submit, the user is redirected back and sees a success message; invalid submits show field errors.

**Tasks**
- Model: `ContactMessage` (name, email, subject, message, created_at, is_read).
- Form: `ContactForm` (a `ModelForm`) with validation.
- View: handle POST, save, send email, then redirect (POST → redirect → GET).
- Settings: email configuration + console email backend for development.
- Template: render fields, errors, and the success message.

**Django concepts you'll learn:** `ModelForm` and validation, CSRF, the messages framework, `send_mail`/email backends, redirect-after-post.

---

### Feature 5 — Config & dependency hygiene
**User story**
- As the developer, secrets and config live outside code and dependencies are honest.

**Acceptance criteria**
- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and email settings are read from the environment via `django-environ`.
- An `.env.example` documents required variables (no real secrets committed).
- `requirements.txt` lists only packages this project actually uses.

**Tasks**
- Introduce `environ.Env()` in `settings.py` and read values from `.env`.
- Create `.env` (gitignored) and `.env.example` (committed).
- Regenerate `requirements.txt` from the project's real imports (start from `Django`, `django-environ`).

**Django concepts you'll learn:** 12-factor settings, environment configuration, dependency management.

---

### Feature 6 — First tests
**User story**
- As the developer, I can refactor with confidence.

**Acceptance criteria**
- Tests cover model `__str__`, the home view (200 + expected content), and contact-form validation (valid + invalid).
- `python manage.py test` passes.

**Tasks**
- Add tests in `apps/core/tests.py` using `TestCase` and the test `Client`.
- Create test objects in `setUp`.

**Django concepts you'll learn:** `TestCase`, the test client, assertions, test isolation.

---

## Epic: Foundation / project wiring [Now, ongoing]
Keep the project structure clean as you go.
- `apps.core` stays in `INSTALLED_APPS`; the project-level `templates/` directory is discovered; `static/` is served in dev.
- Root `config/urls.py` includes `apps.core.urls`; the core app keeps its `app_name = 'core'` namespace.
- Keep `README.md` accurate (templates live at `templates/config/base.html`, not `config/templates`).

---

## Long-term epics [Later — do not start yet]
Captured for direction only; each becomes its own backlog once the single-person portfolio is solid. See `docs/ROADMAP.md`.
- **Accounts & multi-tenancy:** registration/login, per-user ownership, dashboards, permissions.
- **Audience tiers:** Teams and Companies (organizations, memberships, roles).
- **Custom domains/subdomains:** Sites framework + host-based routing.
- **Built-in switchable themes:** per-portfolio selection using Tabler/Litho (high-level only for now).
- **SaaS:** subscription plans, billing, feature/theme gating, onboarding.
- **API & frontend:** Django REST Framework API; optional React/Vue client.
- **Media & production:** uploads, Postgres, hosting, security hardening, CI/CD.
