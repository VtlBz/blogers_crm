from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

WSGI_APPLICATION = "config.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
