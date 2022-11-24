from fastapi import FastAPI

from config import get_settings
from sentry.api import api_router


settings = get_settings()

app = FastAPI(
    debug=settings.DEBUG,
)

app.include_router(api_router)
