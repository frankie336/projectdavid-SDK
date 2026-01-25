# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .tool_function import ToolFunction

__all__ = ["Tool"]


class Tool(BaseModel):
    id: str

    type: str

    function: Optional[ToolFunction] = None

    name: Optional[str] = None
