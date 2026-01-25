# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ThreadUpdateParams"]


class ThreadUpdateParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    meta_data: Optional[object]
    """Updated metadata"""

    participant_ids: Optional[SequenceNotStr[str]]
    """Updated list of participant IDs"""

    tool_resources: Optional[object]
    """Updated tool resources for the thread"""
