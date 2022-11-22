from typing import Any, Literal, Mapping
from uuid import UUID

from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()


class Installation(BaseModel):
    uuid: UUID


class Request(BaseModel):
    action: str
    data: Mapping[str, Any]
    actor: Mapping[str, Any]
    installation: Installation


SentryHookResource = Literal['installation', 'event_alert', 'issue', 'metric_alert', 'error', 'comment']


@app.post("/api/sentry/webhook")
async def root(request: Request):
    return request
