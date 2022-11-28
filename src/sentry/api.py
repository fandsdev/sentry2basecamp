from fastapi.requests import Request
from fastapi.responses import Response

from fastapi import status
from fastapi import APIRouter

from src.basecamp.campfire_bot import CampfireBot
from src.sentry.models import Webhook

api_router = APIRouter()


@api_router.post("/api/sentry/webhook")
async def sentry_webhook(webhook: Webhook, request: Request) -> Response:
    sentry_hook_resource = request.headers.get('sentry-hook-resource')

    if sentry_hook_resource in ['issue', 'event-alert']:
        message = webhook.dispatch_webhook_title(sentry_hook_resource)  # type: ignore
        CampfireBot.send_message(message)
        return Response(status_code=status.HTTP_200_OK)
    else:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
