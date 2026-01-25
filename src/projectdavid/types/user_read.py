# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["UserRead"]


class UserRead(BaseModel):
    """Schema for reading user details from the API."""

    id: str

    created_at: datetime

    updated_at: datetime

    email: Optional[str] = None

    email_verified: Optional[bool] = None

    family_name: Optional[str] = None

    full_name: Optional[str] = None

    given_name: Optional[str] = None

    oauth_provider: Optional[str] = None

    picture_url: Optional[str] = None
