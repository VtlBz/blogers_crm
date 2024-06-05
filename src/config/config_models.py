from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresConfig(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(
        extra="ignore",
        env_prefix="POSTGRES_",
        validate_assignment=True,
    )

    dbname: str = Field(default="postgres", validation_alias="POSTGRES_DB")
    user: str = Field(default="postgres")
    password: str = Field(default="postgres")
    host: str = Field(default="localhost")
    port: int = Field(default=5432)
    schemas: str = Field(
        default="public", description="Comma-separated list of schemas"
    )


class InstagramLoginCreditentials(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(
        extra="ignore",
        env_prefix="INSTAGRAM_USER_",
        validate_assignment=True,
    )

    username: str = Field(...)
    password: str = Field(...)
