from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: Optional[str] = "projects-api"
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    DETA_PROJECT_KEY: str

    # @validator("BACKEND_CORS_ORIGINS", pre=True)
    # def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
    #     if isinstance(v, str) and not v.startswith("["):
    #         return [i.strip() for i in v.split(",")]
    #     elif isinstance(v, (list, str)):
    #         return v
    #     raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
