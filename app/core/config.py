from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: Optional[str] = "projects-api"
    DETA_PROJECT_KEY: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
