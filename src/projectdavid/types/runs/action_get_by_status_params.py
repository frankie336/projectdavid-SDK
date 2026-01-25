# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ActionGetByStatusParams"]


class ActionGetByStatusParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    status: Optional[str]
