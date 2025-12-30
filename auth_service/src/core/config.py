import os

from pydantic import computed_field
from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )

    # Common
    debug: bool = False
    project_name: str = "Wishlist API"
    base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Postgres
    postgres_user: str
    postgres_password: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str

    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_password: str | None = None

    # JWT
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_hours: int = 48

    @computed_field
    @property
    def database_url(self) -> str:
        return f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

    @computed_field
    @property
    def redis_url(self) -> str:
        auth = f"default:{self.redis_password}" if self.redis_password else ""
        return f"redis://{auth}@{self.redis_host}:{self.redis_port}/0"


settings = Settings()
