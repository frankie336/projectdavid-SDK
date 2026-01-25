# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CompletionCreateParams"]


class CompletionCreateParams(TypedDict, total=False):
    api_key: Required[Optional[str]]

    assistant_id: Required[str]

    message_id: Required[str]

    model: Required[str]

    provider: Required[str]

    run_id: Required[str]

    thread_id: Required[str]

    content: Optional[str]
