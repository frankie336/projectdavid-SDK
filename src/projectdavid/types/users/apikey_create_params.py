# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ApikeyCreateParams"]


class ApikeyCreateParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    expires_in_days: Optional[int]
    """Optional number of days from now until the key automatically expires.

    Minimum value is 1.
    """

    key_name: Optional[str]
    """An optional user-friendly name for the key (e.g., 'My Production Key')."""
