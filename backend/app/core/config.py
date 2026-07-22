from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    app_name: str = "api_inbox"
    app_version: str = "0.1.0"
    
    # database_user: str = "sqlite"
    # database_password: str = "sqlite"
    # database_db: str = "sqlite"
    # database_host: str = "localhost"
    # database_port: int = 5432
    
    database_url: str | None = None
    
    
    
    model_config = SettingsConfigDict(
        case_sensitive=False,
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8",
    )
    
def get_settings() -> Settings:
    return Settings()
