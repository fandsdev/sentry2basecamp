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
