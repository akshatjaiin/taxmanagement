 
# backend/app/core/settings.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_uri: str
    jwt_secret: str
    google_cloud_credentials: str
    taxjar_api_key: str
    
    class Config:
        env_file = ".env"

settings = Settings()