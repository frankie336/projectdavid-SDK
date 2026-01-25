# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AssistantUpdateParams"]


class AssistantUpdateParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    description: Optional[str]

    instructions: Optional[str]

    meta_data: Optional[object]

    model: Optional[str]

    name: Optional[str]

    response_format: Optional[str]

    temperature: Optional[float]

    tool_resources: Optional[Dict[str, object]]

    tools: Optional[SequenceNotStr[str]]

    top_p: Optional[float]

    users: Optional[SequenceNotStr[str]]

    vector_stores: Optional[SequenceNotStr[str]]

    webhook_secret: Optional[str]

    webhook_url: Optional[str]
