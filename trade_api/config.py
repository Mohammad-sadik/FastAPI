from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Security
    SECRET_KEY: str = "change-this-secret-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # AI
    GEMINI_API_KEY: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
