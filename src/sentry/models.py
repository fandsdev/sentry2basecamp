from typing import Any, Callable, Literal, Mapping
from uuid import UUID

from pydantic import BaseModel
from pydantic.config import Extra


SentryHookResourceHeader = Literal['issue', 'event-alert']


class Installation(BaseModel):
    uuid: UUID


class Webhook(BaseModel, extra=Extra.allow):
    action: str
    data: Mapping[str, Any]
    installation: Installation

    def dispatch_webhook_title(self, sentry_hook_resource: SentryHookResourceHeader) -> str:
        hook_title: dict[str, Callable[..., str]] = {
            'issue': lambda: self.data['issue']['title'],
            'event-alert': lambda: self.data['event']['title'],
        }

        return hook_title[sentry_hook_resource]()
