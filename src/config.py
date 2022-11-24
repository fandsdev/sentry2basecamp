import os
from distutils.util import strtobool
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = bool(strtobool(os.getenv('DEBUG', 'False')))

    BASECAMP_ACCOUNT_ID: str = 'bc-acc-id'
    BASECAMP_CHATBOT_KEY: str = 'bc-bot-key'

    class Config:
        env_file = 'src/.env'


@lru_cache()
def get_settings():
    return Settings()
