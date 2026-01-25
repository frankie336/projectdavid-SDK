# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["StatusEnum"]

StatusEnum: TypeAlias = Literal[
    "deleted",
    "active",
    "queued",
    "in_progress",
    "action_required",
    "completed",
    "failed",
    "cancelling",
    "cancelled",
    "pending",
    "processing",
    "expired",
    "retrying",
]
