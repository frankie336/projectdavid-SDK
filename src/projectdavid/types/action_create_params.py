# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ActionCreateParams"]


class ActionCreateParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    run_id: Required[str]

    id: Optional[str]

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    function_args: Optional[object]

    status: Optional[str]

    tool_call_id: Optional[str]

    tool_name: Optional[str]

    turn_index: Optional[int]
