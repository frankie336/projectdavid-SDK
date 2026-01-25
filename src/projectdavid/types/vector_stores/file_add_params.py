# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..status_enum import StatusEnum

__all__ = ["FileAddParams"]


class FileAddParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    file_id: Required[str]
    """Client-assigned unique file record ID"""

    file_name: Required[str]
    """Original filename"""

    file_path: Required[str]
    """Identifier path in metadata"""

    meta_data: Optional[object]
    """Arbitrary metadata"""

    status: Optional[StatusEnum]
    """Initial processing state"""
