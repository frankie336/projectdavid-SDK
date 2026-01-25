# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Optional

from .._models import BaseModel
from .run_status import RunStatus
from .action_read import ActionRead
from .tool_function import ToolFunction
from .truncation_strategy import TruncationStrategy

__all__ = ["RunRetrieveResponse", "Tool"]


class Tool(BaseModel):
    id: str

    type: str

    function: Optional[ToolFunction] = None

    name: Optional[str] = None


class RunRetrieveResponse(BaseModel):
    id: str

    assistant_id: str

    created_at: int

    instructions: str

    meta_data: object

    model: str

    object: str

    parallel_tool_calls: bool

    response_format: str

    status: RunStatus

    temperature: float

    thread_id: str

    tool_resources: builtins.object

    tools: List[Tool]

    top_p: float

    user_id: str

    actions: Optional[List[ActionRead]] = None

    cancelled_at: Optional[int] = None

    completed_at: Optional[int] = None

    expires_at: Optional[int] = None

    failed_at: Optional[int] = None

    incomplete_details: Optional[str] = None

    last_error: Optional[str] = None

    max_completion_tokens: Optional[int] = None

    max_prompt_tokens: Optional[int] = None

    required_action: Optional[str] = None

    started_at: Optional[int] = None

    tool_choice: Optional[str] = None

    truncation_strategy: Optional[TruncationStrategy] = None

    usage: Optional[builtins.object] = None
