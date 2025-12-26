# Personal Website (Django + Tailwind CDN)

A simple personal website with admin-managed **Projects** and **Blog** plus a **Contact** form.

## Features
- Django 5
- Tailwind via CDN (no build step)
- Projects app (admin-managed)
- Blog app (admin-managed)
- Contact form (email via SMTP env vars; stores messages in DB)
- `robots.txt` and `sitemap.xml` endpoints

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Configure env vars (see below)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit:
- Home: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Environment Variables
Create a `.env` file (optional) or set environment variables.

### Django
- `DJANGO_SECRET_KEY` (required in production)
- `DJANGO_DEBUG` (default `true`)
- `DJANGO_ALLOWED_HOSTS` (comma-separated; default `*`)

### Database (MySQL)
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST` (default `127.0.0.1`)
- `DB_PORT` (default `3306`)

If `DB_NAME` is not set, the project falls back to SQLite for local dev.

### Email (for Contact form)
- `EMAIL_HOST`
- `EMAIL_PORT` (default `587`)
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `EMAIL_USE_TLS` (default `true`)
- `CONTACT_TO_EMAIL` (where form submissions go)

## Apps
- `projects` – project cards/listing
- `blog` – posts with a slug and published flag
- `core` – pages (home/about/contact) + SEO endpoints

---
Generated on 2025-12-26
