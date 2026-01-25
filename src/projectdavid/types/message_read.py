# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["MessageRead"]


class MessageRead(BaseModel):
    id: str

    assistant_id: Optional[str] = None

    attachments: List[object]

    completed_at: Optional[int] = None

    content: str

    created_at: int

    incomplete_at: Optional[int] = None

    incomplete_details: Optional[object] = None

    meta_data: object

    object: str

    role: str

    run_id: Optional[str] = None

    status: Optional[str] = None

    thread_id: str

    sender_id: Optional[str] = None

    tool_call_id: Optional[str] = None

    tool_id: Optional[str] = None
