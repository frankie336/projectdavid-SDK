# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileGenerateSignedURLParams"]


class FileGenerateSignedURLParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    expires_in: int
    """Seconds until link expires"""

    use_real_filename: bool
