# Portfolio Kit - Technical Implementation Plan

## Goal Description

Build a highly customizable, fast-to-deploy Portfolio Kit using Django and Wagtail. The system will support multiple users, dynamic theming (Tabler, ThemeForest), and flexible content blocks (StreamFields). It aims to provide an "Elementor-like" experience for backend admins while maintaining clean, vendor-specific frontend asset organization.

## User Review Required

> [!IMPORTANT]
> **Multi-Theme Strategy**: We need to decide strictly on how themes are loaded. The proposed approach is using Django's template loaders or a custom middleware to switch template directories based on site settings or user configuration.
> **Asset Organization**: Static files for different vendors will be isolated to prevent CSS conflicts.

## Proposed Architecture

### 1. Project Structure

Standard best-practice Django layout with valid separation of concerns.

```text
portfolio-kit/
├── manage.py
├── pyproject.toml / requirements.txt
├── config/ (Settings)
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── core/ (User model, Global utilities)
│   ├── themes/ (Theme management logic)
│   ├── portfolio/ (Projects, Case studies)
│   ├── resume/ (Education, Experience, Skills)
│   └── blocks/ (Reusable StreamField components)
├── templates/
│   ├── base.html
│   ├── themes/
│   │   ├── tabler/
│   │   └── creative_tim/
│   └── components/
└── static/
    ├── css/
    ├── js/
    └── vendors/ (Isolated vendor assets)
```

### 2. Apps Breakdown

#### Core App

- **Custom User Model**: Essential for future-proofing (e.g., `AbstractUser`).
- **Base Page Models**: Abstract/Base pages that other pages inherit from to share common fields (SEO, Cover Image).

#### Themes App

- **Theme Model**: Database-driven theme selection (possibly using Wagtail Settings).
- **Context Processors**: To inject theme-specific variables into templates.

#### Blocks (Components) App

- **Atomic Blocks**: Heading, Text, Image, Button.
- **Molecule/Organism Blocks**: Hero Section, Feature Grid, Testimonial Carousel, detailed Project Card.
- **Wagtail StreamField**: The core engine for the "page builder" experience.

### 3. Best Practices Compliance

- **12-Factor App**: Config separation, stateless processes.
- **Access Control**: Django Groups/Permissions for Editor vs Admin roles.
- **Performance**:
  - Image optimization via Wagtail Images.
  - Caching strategies (Memcached/Redis) - _Future Scope_.
- **SEO**: Built-in Wagtail SEO plus extended metadata fields.

## Verification Plan

### Automated Tests

- `pytest` for unit testing models and views.
- basic `selenium` or Wagtail's built-in testing helpers for Admin UI checks.

### Manual Verification

- Verify Theme Switcher: Change theme in settings, check if frontend updates without code changes.
- Verify Block Rendering: Create a page with all available blocks and check responsiveness.
