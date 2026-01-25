# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AssistantCreateParams"]


class AssistantCreateParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    model: Required[str]
    """LLM model ID"""

    name: Required[str]
    """Assistant name"""

    id: Optional[str]
    """Optional pre-generated assistant ID."""

    description: str
    """Brief description"""

    instructions: str
    """System instructions"""

    meta_data: Optional[object]

    response_format: str

    temperature: float

    tool_resources: Optional[Dict[str, object]]

    tools: Optional[Iterable[object]]
    """OpenAI-style tool specs (dicts)."""

    top_p: float

    webhook_secret: Optional[str]

    webhook_url: Optional[str]
