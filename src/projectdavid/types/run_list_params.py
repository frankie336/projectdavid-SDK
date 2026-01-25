# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    limit: int

    order: Literal["asc", "desc"]

    thread_id: Optional[str]
