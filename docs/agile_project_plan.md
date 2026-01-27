# Agile Project Management Plan - Portfolio Kit

## Overview

This document outlines the Agile roadmap to build a Django/Wagtail-based Portfolio Kit.

## 🚀 Epic 1: Core Platform Foundation

**Goal**: Establish a robust, scalable backend infrastructure capable of handling multiple themes and extendable content models.

### Feature 1.1: Project Skeleton & Environment

- **User Story 1.1.1**: As a Developer, I want to set up a reproducible virtual environment so that dependencies are managed cleanly.
- **User Story 1.1.2**: As a Developer, I want to initialize a Django project with a custom `User` model to allow future-proof authentication extensibility.
- **Task**: Configure `poetry` or `pip-tools` for dependency management.
- **Task**: Set up `config` settings structure (base/dev/prod).

### Feature 1.2: Theme Management System

- **User Story 1.2.1**: As an Administrator, I want to switch the specific "Theme" of the site from the backend so that I can change the look and feel without code deployment.
- **User Story 1.2.2**: As a Developer, I want to organize static assets by vendor (e.g., `static/vendors/tabler/`) so that styles don't conflict.
- **Task**: create `ThemeSettings` in Wagtail Site Settings.
- **Task**: Implement custom middleware or template loader to switch template paths based on active theme.

## 🎨 Epic 2: Content & Component Engine

**Goal**: Create an "Elementor-like" editing experience using Wagtail StreamFields.

### Feature 2.1: Atomic Block Library

- **User Story 2.1.1**: As an Editor, I want to add basic elements (Headings, Text, Images, Buttons) to any page so that I can build custom layouts.
- **User Story 2.1.2**: As an Editor, I want to choose color/style variants for blocks (e.g., Primary vs Secondary button) defined by the active theme.

### Feature 2.2: Compound Blocks (Organisms)

- **User Story 2.2.1**: As an Editor, I want to add a "Hero Section" with a background image and CTA button users can instantly see on the landing page.
- **User Story 2.2.2**: As an Editor, I want a "Testimonials Slider" that I can populate with client quotes.

## 🧩 Epic 3: Portfolio Specialized Apps

**Goal**: Implement domain-specific models for a portfolio.

### Feature 3.1: Resume/CV App

- **User Story 3.1.1**: As a User, I want to efficiently input my Education and Work Experience data into structured fields (not just rich text) so that it can be styled consistently.
- **User Story 3.1.2**: As a Visitor, I want to download the resume as a generated PDF (Future scope).

### Feature 3.2: Projects/Case Studies

- **User Story 3.2.1**: As a User, I want to create Project pages with a "Gallery" block to showcase screenshots.
- **User Story 3.2.2**: As a User, I want to tag projects with "Skills" (e.g., Python, React) so visitors can filter by technology.

## 🧪 Quality Assurance & Standards

- **Bug**: Verify that switching themes does not break hardcoded static paths.
- **Test Case**: Create a page with _every_ available block type to ensure rendering resilience.
- **Constraint**: All frontend libraries must be self-hosted in `static/` (avoid CDNs for privacy/reliability unless configured otherwise).

## 📝 Mentorship & Documentation

- **Goal**: User execution is prioritized.
- **Rule**: Antigravity provides the _Snippets_ and _Architecture_, User types the code.
- ** deliverable**: Inline docstrings for every major class and function.
