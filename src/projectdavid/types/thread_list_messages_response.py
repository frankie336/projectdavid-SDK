# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .message_read import MessageRead

__all__ = ["ThreadListMessagesResponse"]


class ThreadListMessagesResponse(BaseModel):
    data: List[MessageRead]

    first_id: Optional[str] = None

    has_more: Optional[bool] = None

    last_id: Optional[str] = None

    object: Optional[str] = None
