# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["APIKeyDetails"]


class APIKeyDetails(BaseModel):
    """
    Schema representing the public details of an API key.
    This schema does *not* include the secret key itself.
    It's designed to be created from the ApiKey ORM model.
    """

    created_at: datetime
    """The timestamp (UTC) when the key was created."""

    is_active: bool
    """Indicates if the key is currently active and usable for authentication."""

    prefix: str
    """The non-secret unique prefix of the key (e.g., 'ea_abc123').

    Used for identification.
    """

    user_id: str
    """The ID of the user who owns this key."""

    expires_at: Optional[datetime] = None
    """The timestamp (UTC) when the key will expire, if an expiration was set."""

    key_name: Optional[str] = None
    """The user-friendly name assigned to the key, if any."""

    last_used_at: Optional[datetime] = None
    """
    The timestamp (UTC) when the key was last successfully used for authentication
    (if tracked).
    """
