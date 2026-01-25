# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .tool_function_param import ToolFunctionParam

__all__ = ["ToolParam"]


class ToolParam(TypedDict, total=False):
    id: Required[str]

    type: Required[str]

    function: Optional[ToolFunctionParam]

    name: Optional[str]
