# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RunStatus"]

RunStatus: TypeAlias = Literal[
    "queued",
    "in_progress",
    "action_required",
    "completed",
    "failed",
    "cancelled",
    "pending",
    "processing",
    "expired",
    "retrying",
]
