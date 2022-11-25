from fastapi.requests import Request
from fastapi.responses import Response

from fastapi import status
from fastapi import APIRouter

from basecamp.campfire_bot import CampfireBot
from sentry.models import Webhook

api_router = APIRouter()


@api_router.post("/api/sentry/webhook", status_code=status.HTTP_200_OK)
async def sentry_webhook(webhook: Webhook, request: Request):
    sentry_hook_resource = request.headers.get('sentry-hook-resource')

    if sentry_hook_resource in ['issue', 'event-alert']:
        message = webhook.dispatch_webhook_title(sentry_hook_resource)
        CampfireBot.send_message(message)
    else:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
