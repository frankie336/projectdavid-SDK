# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..status_enum import StatusEnum

__all__ = ["FileUpdateStatusParams"]


class FileUpdateStatusParams(TypedDict, total=False):
    vector_store_id: Required[str]

    args: Required[object]

    kwargs: Required[object]

    status: Required[StatusEnum]
    """New status for the file record"""

    error_message: Optional[str]
    """Error message if status is 'failed'"""
