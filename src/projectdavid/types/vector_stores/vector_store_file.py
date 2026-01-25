# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..status_enum import StatusEnum

__all__ = ["VectorStoreFile"]


class VectorStoreFile(BaseModel):
    id: str
    """File record ID"""

    file_name: str
    """Original file name"""

    file_path: str
    """Metadata path identifier"""

    status: StatusEnum
    """Current processing state"""

    vector_store_id: str
    """Owning vector-store ID"""

    error_message: Optional[str] = None
    """Failure reason, if any"""

    meta_data: Optional[object] = None
    """Metadata dict"""

    object: Optional[str] = None
    """Object type identifier"""

    processed_at: Optional[int] = None
    """Unix timestamp of last processing change"""
