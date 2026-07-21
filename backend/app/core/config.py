from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    app_name: str = "api_inbox"
    app_version: str = "0.1.0"
    
    database_user: str
    database_password: str
    database_db: str
    database_host: str
    database_port: int
    
    database_url: str | None = None
    
    
    
    model_config = SettingsConfigDict(
        case_sensitive=True,
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8",
    )
    
settings = Settings()