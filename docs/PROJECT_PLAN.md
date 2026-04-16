# Portfolio Kit: Master Project Plan

This document acts as the single source of truth for the development of the **Django & Wagtail Portfolio Kit**. It combines the architectural blueprint with an actionable Agile Kanban execution board.

---

## 🏗️ 1. Architecture & Core Concepts

In Wagtail, content is structured around **Pages**, **Snippets**, **StreamFields**, and **Site Settings**. We are isolating specific logic into independent Django apps to keep the code scalable.

### Apps Structure

**Internal Grouped Apps (`apps/` folder):**
- **`apps.core`**: The structural blueprint. Contains abstract page models (like `BasePage` and `SEOMixin`) that other pages inherit from. It also houses your reusable Wagtail StreamBlocks (`HeroBlock`, `ImageGalleryBlock`) so you can visually construct page layouts anywhere.
- **`apps.images`**: Custom model handling for images. Allows you to add extra fields (like 'alt text' or 'caption') universally to all image uploads.
- **`apps.documents`**: Custom model handling for documents. Manages the storage and metadata of uploaded PDFs, spreadsheets, and CVs.
- **`apps.projects`**: The portfolio showcase engine. Responsible for project directory listings, rich-text case study pages, and taxonomy categorizations.
- **`apps.blog`**: The technical article system. Contains list views for blog posts and integrates with `taggit` for keyword browsing.
- **`apps.settings`**: Global Front-End variables. It unlocks Wagtail's `SiteSetting` dashboard to allow site owners to change copyright text, social media links, and contact parameters without touching a single line of code.

**Root-Level Apps (Default/Core Integrations):**
- **`config`**: The main Django engine configuration. This dictates the back-end system setup (database variables, installed apps, security keys, primary URL routes) via `settings/base.py`.
- **`home`**: Wagtail's default app for handling the root `HomePage` and basic site entry routing.
- **`search`**: Wagtail's default integration for indexing content and executing site-wide queries.

---

## 📋 2. Agile Kanban execution Plan

Below is the execution mapped out in an Agile methodology (Epic > Feature > User Story > Tasks/Tests). *Track these Epics using GitHub Projects!*

### 🚢 [EPIC-1] Core Architecture & Base Configuration
**Goal:** Establish the foundational mechanics for Wagtail CMS.

- **[FEAT-1.1] Master Base App (`apps.core`)**
  - **[US-1.1.1]** As a developer, I want a central `BasePage` and SEO mixins so all pages are automatically optimized for search engines and social sharing without rewriting code.
  - **Tasks:**
    - `[ ]` **[TASK]** Setup `apps.core` directory.
    - `[ ]` **[TASK]** Implement `SEOMixin` (`seo_title`, `og_image`, `search_description`).
    - `[ ]` **[TASK]** Create abstract `BasePage(Page, SEOMixin)`.
    - `[ ]` **[TEST]** Apply base migrations perfectly.

- **[FEAT-1.2] Media and Documents Handling**
  - **[US-1.2.1]** As an administrator, I need to upload and manage custom media (like my CV as a PDF, or custom images) securely using specialized models.
  - **Tasks:**
    - `[ ]` **[TASK]** Setup `apps.documents` app.
    - `[ ]` **[TASK]** Implement `CustomDocument` model and configure Wagtail to use it globally.

- **[FEAT-1.3] Reusable UI Blocks (StreamBlocks)**
  - **[US-1.3.1]** As an editor, I want to construct flexible, dynamic page layouts using Lego-like structural blocks.
  - **Tasks:**
    - `[ ]` **[TASK]** Setup `apps.core/blocks.py`.
    - `[ ]` **[TASK]** Define `HeroBlock`, `ImageGalleryBlock`, and `RichTextContentBlock`.


### 🚢 [EPIC-2] Projects & Portfolio Showcase
**Goal:** Build the engine that displays your work, case studies, and skills.

- **[FEAT-2.1] Project Listings**
  - **[US-2.1.1]** As a visitor, I want to see a sleek grid of your past work so I can assess your expertise at a glance.
  - **Tasks:**
    - `[ ]` **[TASK]** Create `ProjectIndexPage` model and template.
    - `[ ]` **[TASK]** Create `ProjectCategory` (Snippet) to classify projects.
    - `[ ]` **[TEST]** Verify index aggregates and dynamically loops over child projects.

- **[FEAT-2.2] Detailed Case Studies**
  - **[US-2.2.1]** As a hiring manager, I want to read a deep-dive case study with code snippets, architecture diagrams, and high-res images.
  - **Tasks:**
    - `[ ]` **[TASK]** Create `ProjectPage` model using `StreamField` for dynamic body content.
    - `[ ]` **[TASK]** Assign ManyToMany relationships for `ProjectCategory`.


### 🚢 [EPIC-3] Technical Blog
**Goal:** Establish an internal blog to share knowledge and boost organic traffic.

- **[FEAT-3.1] Blog Engine**
  - **[US-3.1.1]** As a reader, I want to filter technical articles by tags and see beautifully formatted code syntax.
  - **Tasks:**
    - `[ ]` **[TASK]** Create `BlogIndexPage` (with pagination).
    - `[ ]` **[TASK]** Create `BlogPage` and integrate `taggit`.


### 🚢 [EPIC-4] Front-End Design & Interface
**Goal:** Implement a "wow-factor" premium aesthetic.

- **[FEAT-4.1] CSS System & Interactivity**
  - **[US-4.1.1]** As a UI developer, I want a clean `index.css` acting as my design token system to maintain visual consistency across themes.
  - **Tasks:**
    - `[ ]` **[TASK]** Establish CSS custom properties (colors, typography via Inter/Outfit).
    - `[ ]` **[TASK]** Create micro-animations (scale-up shadows on hover).
    - `[ ]` **[TASK]** Integrate dark mode (`prefers-color-scheme`).


### 🚢 [EPIC-5] Global Site Settings
**Goal:** Setup system-wide elements spanning the entire website.

- **[FEAT-5.1] Global Component Data**
  - **[US-5.1.1]** As an admin, I want to change my social links or footer text directly from the CMS without a code redeploy.
  - **Tasks:**
    - `[ ]` **[TASK]** Setup `apps.settings`.
    - `[ ]` **[TASK]** Register `SocialSiteSetting` and `FooterSiteSetting`.


### 🚢 [EPIC-6] Production & Deployment
**Goal:** Prepare the Django/Wagtail app for a robust, secure public launch.

- **[FEAT-6.1] Environment Hardening**
  - **[US-6.1.1]** As a systems architect, I want securely managed database credentials and cloud storage for user uploads.
  - **Tasks:**
    - `[ ]` **[TASK]** Enforce `DEBUG=False` checks.
    - `[ ]` **[TASK]** Implement WhiteNoise for static assets and AWS S3/Cloudinary configuration for `MEDIA_ROOT`.
    - `[ ]` **[TASK]** Finalize `Dockerfile` rendering.

### 🚢 [EPIC-7] Headless CMS Evolution (Future Scope)
**Goal:** Decouple the frontend from the Django backend to serve a React/TypeScript application.

- **[FEAT-7.1] RESTful API Integration**
  - **[US-7.1.1]** As a UI engineer, I want a robust JSON REST API to consume the portfolio content so that I can construct a blazing-fast React/TypeScript single-page application.
  - **Tasks:**
    - `[ ]` **[TASK]** Expose Wagtail's built-in `PagesAPIViewSet` and `ImagesAPIViewSet` natively.
    - `[ ]` **[TASK]** (Optional) Build custom Django Rest Framework (DRF) endpoints for any complex form handling (e.g. capturing leads).
    - `[ ]` **[TASK]** Configure CORS headers to allow requests from the React frontend domains.
