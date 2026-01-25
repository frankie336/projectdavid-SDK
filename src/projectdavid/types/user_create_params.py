# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    email: Optional[str]
    """User's email address."""

    email_verified: Optional[bool]
    """Email verification status."""

    family_name: Optional[str]
    """User's last name."""

    full_name: Optional[str]
    """User's full display name."""

    given_name: Optional[str]
    """User's first name."""

    oauth_provider: Optional[str]
    """Authentication provider (e.g., 'google', 'local')."""

    picture_url: Optional[str]
    """URL to profile picture."""

    provider_user_id: Optional[str]
    """User ID from the OAuth provider."""
