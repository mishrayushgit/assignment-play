from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    model_config = ConfigDict(extra="ignore", env_file=".env")

    DATABASE_URL: str
    API_KEY: str


settings = Settings()
