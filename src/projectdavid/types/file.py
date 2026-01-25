# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str
    """Unique identifier of the file"""

    bytes: int
    """Size of the file in bytes"""

    created_at: Union[datetime, str]
    """ISO‑8601 timestamp when the file was created (datetime or ISO string accepted)"""

    filename: str
    """Original filename supplied by the user"""

    purpose: str
    """Purpose associated with the file"""

    expires_at: Union[datetime, str, None] = None
    """Optional ISO‑8601 expiry timestamp"""

    object: Optional[Literal["file"]] = None
    """Always the string 'file'"""

    status: Optional[str] = None
    """Current status of the file"""
