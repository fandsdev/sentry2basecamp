import os
from functools import lru_cache

from pydantic import BaseSettings

from src.helpers import str_to_bool


class Settings(BaseSettings):
    DEBUG: bool = bool(str_to_bool(os.getenv('DEBUG', 'False')))

    BASECAMP_ACCOUNT_ID: str = 'bc-acc-id'
    BASECAMP_CHATBOT_KEY: str = 'bc-bot-key'
    BASECAMP_PROJECT_ID: int = 111
    BASECAMP_CHAT_ID: int = 111

    class Config:
        env_file = 'src/.env'


@lru_cache()
def get_settings() -> Settings:
    return Settings()
