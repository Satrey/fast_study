from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    db_name: str
    db_user: str
    db_password: SecretStr
    db_host: str
    db_port: int
    db_echo: bool

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf8", extra="ignore"
    )

    @property
    def get_db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password.get_secret_value()}@{self.db_host}:{self.db_port}/{self.db_name}"


class Settings(BaseSettings):
    db_settings: DBSettings = DBSettings()  # Экземпляр класса DBSettings
    secret_key: SecretStr

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf8',
        extra='ignore'
    )


# Инициализация переменной settings
settings = Settings()
