from typing import Any, Mapping
from fastapi.requests import Request
from fastapi.responses import Response
from uuid import UUID

from fastapi import FastAPI
from fastapi import status
from pydantic.config import Extra
from pydantic.main import BaseModel

app = FastAPI()


class Installation(BaseModel):
    uuid: UUID


class Webhook(BaseModel, extra=Extra.allow):
    action: str
    data: Mapping[str, Any]
    installation: Installation


@app.post("/api/sentry/webhook", status_code=status.HTTP_200_OK)
async def sentry_webhook(webhook: Webhook, request: Request):
    if request.headers.get('sentry-hook-resource') == 'issue':

        #todo send webhook.data.get('title') to the Basecamp

        return 'ok!'

    elif request.headers.get('sentry-hook-resource') == 'event-alert':

        return 'ok!'

    else:

        return Response(status_code=status.HTTP_400_BAD_REQUEST)
