# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MonitorRegisterRunParams"]


class MonitorRegisterRunParams(TypedDict, total=False):
    args: Required[object]

    kwargs: Required[object]

    run_id: Required[str]
