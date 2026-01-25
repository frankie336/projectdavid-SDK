# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Optional

from .tool import Tool
from .._models import BaseModel
from .run_status import RunStatus
from .truncation_strategy import TruncationStrategy

__all__ = ["Run"]


class Run(BaseModel):
    id: str

    assistant_id: str

    cancelled_at: Optional[int] = None

    completed_at: Optional[int] = None

    created_at: int

    expires_at: int

    failed_at: Optional[int] = None

    incomplete_details: Optional[str] = None

    instructions: str

    last_error: Optional[str] = None

    max_completion_tokens: Optional[int] = None

    max_prompt_tokens: Optional[int] = None

    meta_data: object

    model: str

    object: str

    parallel_tool_calls: bool

    required_action: Optional[str] = None

    response_format: str

    started_at: Optional[int] = None

    status: RunStatus

    temperature: float

    thread_id: str

    tool_choice: str

    tool_resources: builtins.object

    tools: List[Tool]

    top_p: float

    usage: builtins.object

    truncation_strategy: Optional[TruncationStrategy] = None

    user_id: Optional[str] = None
    """Filled in by the server from the caller’s API-key.

    Clients MAY omit or set to None.
    """
