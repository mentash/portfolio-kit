# Agile Backlog — Portfolio App

This backlog is written to be implementable in small increments while learning Django.

---

## Epic: Core App
Deliver the first working, database-driven portfolio site using Django templates + Bootstrap.

### Feature: Portfolio Home Page (Single Page)
**User story**
- As a visitor, I need to view a single-page portfolio so that I can quickly understand the professional’s profile.

**Acceptance criteria**
- Home page loads at `/`.
- Page includes sections: Hero, About, Skills, Projects, Experience, Education, Contact.
- All section data is rendered from the database.

**Tasks**
- Create models: Profile, Skill, Project, Experience, Education.
- Create view `portfolio_view` that queries data and renders `templates/core/index.html`.
- Create template layout (`base.html` + `index.html`) using Bootstrap 5.

---

### Feature: Content Management via Django Admin
**User story**
- As the site owner, I need to edit my profile content in an admin UI so that I can update my portfolio without changing code.

**Acceptance criteria**
- Admin lists and edits all portfolio models.
- Profile behaves like a singleton (only one active profile).

**Tasks**
- Register models in `apps/core/admin.py` with useful list/search/filter settings.
- Add ordering fields where needed (skills/projects/experience/education).

---

### Feature: Create Contact Page/Form (Email Notifications + Persistence)
**User story**
- As a visitor, I need to submit a contact form that sends email notification to both my email address and the portfolio's official contact address coded in the form.

**Acceptance criteria**
- Contact section exists on `/` (anchor `#contact`).
- Form is protected by CSRF.
- On valid submit:
  - A `ContactMessage` row is created in DB.
  - An email is sent to:
    - `OWNER_NOTIFICATION_EMAIL` (your email)
    - `PORTFOLIO_CONTACT_EMAIL` (official contact)
  - User is redirected back to `/#contact?success=1` (or equivalent) and sees a success alert.
- On invalid submit: validation errors are shown on the page.

**Tasks**
- Model: `ContactMessage` (name, email, subject, message, created_at, is_read).
- Form: `ContactForm` with validation.
- View: `contact_view` (POST) that saves message + sends email.
- Settings:
  - Add email configuration variables.
  - Use console email backend in dev.
- Template: render form fields and errors in Contact section.

---

### Feature: Static Assets & Theme
**User story**
- As a visitor, I need a clean, responsive design so the portfolio is readable on desktop and mobile.

**Acceptance criteria**
- Bootstrap 5 theme is applied consistently.
- Custom CSS/JS loaded via `{% static %}`.
- Smooth scroll to sections works.

**Tasks**
- Add `static/css/style.css` (small overrides).
- Add `static/js/main.js` (smooth scroll, active nav link).
- Add `static/images/` and wire an avatar placeholder.

---

## Epic: Foundation / Project Wiring
Ensure Django settings, URLs, templates, and static files are wired correctly.

### Feature: App Wiring (settings + urls)
**User story**
- As a developer, I need a clean Django project structure so I can iterate safely.

**Acceptance criteria**
- `apps.core` is in `INSTALLED_APPS`.
- `templates/` directory is discovered.
- `static/` directory is served in dev.

**Tasks**
- Update `config/settings.py`: INSTALLED_APPS, TEMPLATES DIRS, STATICFILES_DIRS, DEFAULT_AUTO_FIELD.
- Update `config/urls.py` to include `apps.core.urls`.
- Create `apps/core/urls.py`.
