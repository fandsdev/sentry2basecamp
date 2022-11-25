from typing import Any, Mapping
from uuid import UUID

from pydantic import BaseModel
from pydantic.config import Extra


class Installation(BaseModel):
    uuid: UUID


class Webhook(BaseModel, extra=Extra.allow):
    action: str
    data: Mapping[str, Any]
    installation: Installation

    def dispatch_webhook_title(self, sentry_hook_resource: str) -> str:
        hook_title = {
            'issue': lambda: self.data['issue']['title'],
            'event-alert': lambda: self.data['event']['title'],
        }

        return hook_title.get(sentry_hook_resource)()
