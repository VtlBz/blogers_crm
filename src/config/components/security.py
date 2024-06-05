import os

from config.utils import InternalNetworks

DEFAULT_TOKEN: str = "DEFAULT_SECRET_KEY"
DEFAULT_HOSTS: str = "127.0.0.1 localhost [::1]"

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", DEFAULT_TOKEN)

DEBUG = os.getenv("DJANGO_DEBUG_STATE", "False").lower() in {"true", "1", "on"}

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", DEFAULT_HOSTS).split()

internal_addresses = os.getenv("DJANGO_INTERNAL_ADDRESSES", "").split()

INTERNAL_IPS = InternalNetworks(internal_addresses)

CSRF_TRUSTED_ORIGINS = [f"http://{host}:8000" for host in ALLOWED_HOSTS]
