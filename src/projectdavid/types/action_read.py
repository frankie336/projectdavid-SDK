# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ActionRead"]


class ActionRead(BaseModel):
    id: str

    expires_at: Optional[str] = None

    function_args: Optional[object] = None

    is_processed: Optional[bool] = None

    processed_at: Optional[str] = None

    result: Optional[object] = None

    run_id: Optional[str] = None

    status: Optional[str] = None

    tool_call_id: Optional[str] = None

    tool_id: Optional[str] = None

    tool_name: Optional[str] = None

    triggered_at: Optional[str] = None

    turn_index: Optional[int] = None
