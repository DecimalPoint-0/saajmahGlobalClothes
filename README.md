# Saajmah — Costume Rental (Django monolith)

This repository contains a simple Django monolith for Saajmah — a child-friendly costume rental showcase and booking platform.

Quick start (development):

1. Create a virtualenv and activate it

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
```

2. Apply migrations and create a superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

3. (Optional) Add costumes via the admin or create fixtures.

4. Run the development server

```bash
python manage.py runserver
```

Deployment notes:
- `whitenoise` is configured for static file serving.
- Run `python manage.py collectstatic` before deploying.
- Use an actual `SECRET_KEY` and set `DEBUG=False` and proper `ALLOWED_HOSTS` in production.
