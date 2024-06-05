from dotenv import find_dotenv, load_dotenv
from split_settings.tools import include

dotenv_path = find_dotenv(filename="infra/.env")
load_dotenv(dotenv_path, override=True)

include(
    "components/security.py",
    "components/common.py",
    "components/installed_apps.py",
    "components/middleware.py",
    "components/auth_password_validators.py",
    "components/database.py",
    "components/internationalization.py",
    "components/templates.py",
    "components/url_settings.py",
    "components/project_settings.py",
    "components/debug_settings.py",
)
