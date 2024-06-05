import os

from config.components.common import BASE_DIR

root_directory = os.path.abspath(os.sep)


ROOT_URLCONF = "config.urls"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
