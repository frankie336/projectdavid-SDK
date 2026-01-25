# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["VectorStoreCreateParams"]


class VectorStoreCreateParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    distance_metric: Required[str]
    """Distance metric (COSINE, EUCLID, DOT)"""

    name: Required[str]
    """Human-friendly store name"""

    shared_id: Required[str]
    """Pre-generated unique ID (also used as collection name)."""

    vector_size: Required[int]
    """Dimensionality of the vectors"""

    owner_id: Optional[str]
    """Target user-id (admin-only). If omitted, the store is created for the caller."""

    config: Optional[object]
    """Additional configuration options"""
