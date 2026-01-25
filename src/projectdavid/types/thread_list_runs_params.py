# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ThreadListRunsParams"]


class ThreadListRunsParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    limit: int

    order: Literal["asc", "desc"]
