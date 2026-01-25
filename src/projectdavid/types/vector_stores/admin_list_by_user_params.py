# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AdminListByUserParams"]


class AdminListByUserParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    owner_id: Required[str]
    """Target user-id"""
