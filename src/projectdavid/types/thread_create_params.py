# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ThreadCreateParams"]


class ThreadCreateParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    meta_data: Optional[object]
    """Optional metadata for the thread"""

    participant_ids: Optional[SequenceNotStr[str]]
    """List of participant IDs. Omit to default to the authenticated user."""
