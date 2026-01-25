# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .status_enum import StatusEnum

__all__ = ["VectorStore"]


class VectorStore(BaseModel):
    """Metadata returned from the API for an existing vector-store."""

    id: str
    """Unique identifier for the vector store"""

    collection_name: str
    """Qdrant collection name (== id)"""

    created_at: int
    """Unix timestamp (sec) when created"""

    distance_metric: str
    """Metric used for comparison"""

    file_count: int
    """Number of files associated"""

    name: str
    """Vector store name"""

    status: StatusEnum
    """Vector store status"""

    user_id: str
    """Owner user ID (server-side filled)"""

    vector_size: int
    """Vector dimensionality"""

    config: Optional[object] = None
    """Optional config dict"""

    object: Optional[str] = None
    """Object type identifier"""

    updated_at: Optional[int] = None
    """Last modified timestamp"""
