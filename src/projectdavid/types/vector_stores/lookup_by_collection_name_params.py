# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LookupByCollectionNameParams"]


class LookupByCollectionNameParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    name: Required[str]
    """Collection name to look up"""
