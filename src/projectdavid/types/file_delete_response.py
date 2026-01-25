# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileDeleteResponse"]


class FileDeleteResponse(BaseModel):
    id: str
    """Unique identifier of the file"""

    deleted: bool
    """True if the file was deleted successfully"""

    object: Optional[Literal["file"]] = None
    """Always the string 'file'"""
