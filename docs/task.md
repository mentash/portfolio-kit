# Tasks

## 🚢 [EPIC-1] Core Architecture & Base Configuration

- `[ ]` **[FEAT-1.1] Master Base App (`apps.core`)**
  - `[ ]` **[TASK]** Setup `apps.core` directory.
  - `[ ]` **[TASK]** Implement `SEOMixin` (`seo_title`, `og_image`, `search_description`).
  - `[ ]` **[TASK]** Create abstract `BasePage(Page, SEOMixin)`.
  - `[ ]` **[TEST]** Apply base migrations perfectly.

- `[ ]` **[FEAT-1.2] Media and Documents Handling**
  - `[ ]` **[TASK]** Setup `apps.documents` app.
  - `[ ]` **[TASK]** Implement `CustomDocument` model and configure settings.

- `[ ]` **[FEAT-1.3] Reusable UI Blocks (StreamBlocks)**
  - `[ ]` **[TASK]** Setup `apps.core/blocks.py`.
  - `[ ]` **[TASK]** Define `HeroBlock`, `ImageGalleryBlock`, and `RichTextContentBlock`.
