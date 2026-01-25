# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileDeleteParams"]


class FileDeleteParams(TypedDict, total=False):
    args: Required[object]

    file_path: Required[str]

    kwargs: Required[object]
