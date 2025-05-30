import secrets
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from {{ package_name }} import __version__

Environment = Literal["development", "staging", "production"]
LoggingLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Settings(BaseSettings):
    """
    Application settings.
    """
    # App settings.
    project_name: str = Field(default="{{ project_name }}", description="Project name")
    version: str = Field(default=__version__, description="API version")
    description: str = Field(default="{{ project_description }}", description="API description")
    environment: Environment = Field(default="development", description="Project environment")
    port: int = Field(default=8000, description="Port on which the API will be available")

    # Security.
    secret_key: str = Field(default=secrets.token_urlsafe(), description="Secret key for JWT")
    access_token_lifetime: int | float = Field(30 * 60, description="Access token expire seconds")

    # CORS.
    allowed_hosts: list[str] = Field(default=["*"], description="Allowed hosts for CORS")

    # Database.
    database_user: str = Field(default=..., description="Database username")
    database_password: str = Field(default=..., description="Database password")
    database_host: str = Field(default=..., description="Database host")
    database_port: str = Field(default=..., description="Database port")
    database_name: str = Field(default=..., description="Database name")

    # Logging.
    log_level: LoggingLevel = Field(default="INFO", description="Logging level")

    model_config = SettingsConfigDict(env_file=".env")


config = Settings()
