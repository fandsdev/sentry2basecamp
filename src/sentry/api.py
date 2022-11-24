from fastapi.requests import Request
from fastapi.responses import Response

from fastapi import status
from fastapi import APIRouter

from sentry.types import Webhook


api_router = APIRouter()


@api_router.post("/api/sentry/webhook", status_code=status.HTTP_200_OK)
async def sentry_webhook(webhook: Webhook, request: Request):
    if request.headers.get('sentry-hook-resource') == 'issue':

        #todo send webhook.data.get('title') to the Basecamp

        return 'ok!'

    elif request.headers.get('sentry-hook-resource') == 'event-alert':

        return 'ok!'

    else:

        return Response(status_code=status.HTTP_400_BAD_REQUEST)
