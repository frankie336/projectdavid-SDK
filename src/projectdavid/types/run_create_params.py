# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .run_status import RunStatus
from .tool_param import ToolParam
from .truncation_strategy import TruncationStrategy

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    id: Required[str]

    assistant_id: Required[str]

    created_at: Required[int]

    expires_at: Required[int]

    instructions: Required[str]

    thread_id: Required[str]

    cancelled_at: Optional[int]

    completed_at: Optional[int]

    failed_at: Optional[int]

    incomplete_details: Optional[object]

    last_error: Optional[str]

    max_completion_tokens: Optional[int]

    max_prompt_tokens: Optional[int]

    meta_data: object

    model: str

    object: str

    parallel_tool_calls: bool

    required_action: Optional[str]

    response_format: str

    started_at: Optional[int]

    status: RunStatus

    temperature: float

    tool_choice: str

    tool_resources: builtins.object

    tools: Iterable[ToolParam]

    top_p: float

    truncation_strategy: Optional[TruncationStrategy]

    usage: builtins.object
