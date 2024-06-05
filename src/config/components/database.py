from config.config_models import PostgresConfig

PG_CONFIG = PostgresConfig()  # type: ignore

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": PG_CONFIG.dbname,
        "USER": PG_CONFIG.user,
        "PASSWORD": PG_CONFIG.password,
        "HOST": PG_CONFIG.host,
        "PORT": PG_CONFIG.port,
        "OPTIONS": {
            "options": f"-c search_path={PG_CONFIG.schemas}",
        },
        "CONN_MAX_AGE": 300,
    },
}
