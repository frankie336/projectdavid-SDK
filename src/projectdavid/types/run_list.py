# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .run import Run
from .._models import BaseModel

__all__ = ["RunList"]


class RunList(BaseModel):
    data: List[Run]

    first_id: Optional[str] = None

    has_more: Optional[bool] = None

    last_id: Optional[str] = None

    object: Optional[Literal["list"]] = None
