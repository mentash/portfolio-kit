# Portfolio App

A Django-based portfolio application.

## Tech Stack
- Python 3.12+
- Django 6
- SQLite (development)

## Project Structure
- apps/core: Domain app (views, models, templates, urls)
- config: Django project settings and root URL config
- docs: Project notes and backlog

## Quick Start
1. Create and activate a virtual environment.
2. Install dependencies:

   pip install django

3. Run migrations:

   python manage.py migrate

4. Start the development server:

   python manage.py runserver

5. Open:

   http://127.0.0.1:8000/

## Useful Commands
- Create migrations:

  python manage.py makemigrations

- Apply migrations:

  python manage.py migrate

- Create superuser:

  python manage.py createsuperuser

## Templates
The project-level template directory is configured under:
- config/templates

Example namespaced base template:
- config/templates/config/base.html

App templates can extend it using:

{% extends 'config/base.html' %}

## Git Notes
This repository ignores local-only and sensitive files by default:
- .venv/
- db.sqlite3
- .env
- generated static/media output

If you need to share environment variable names, add an .env.example file with placeholders.
