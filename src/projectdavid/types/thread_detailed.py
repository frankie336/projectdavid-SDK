# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Optional

from .._models import BaseModel

__all__ = ["ThreadDetailed", "Participant"]


class Participant(BaseModel):
    """Base schema, potentially used for embedding user info minimally."""

    id: str

    email: Optional[str] = None

    full_name: Optional[str] = None


class ThreadDetailed(BaseModel):
    id: str

    created_at: int

    meta_data: object

    object: str

    participants: List[Participant]

    tool_resources: builtins.object
