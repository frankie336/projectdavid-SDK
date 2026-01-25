# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageSaveAssistantMessageParams"]


class MessageSaveAssistantMessageParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    assistant_id: Required[str]

    content: Required[str]

    role: Required[str]

    thread_id: Required[str]

    is_last_chunk: bool

    meta_data: Optional[object]

    sender_id: Optional[str]

    tool_call_id: Optional[str]

    tool_id: Optional[str]
