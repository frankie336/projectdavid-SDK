# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional

from .._models import BaseModel
from .vector_store import VectorStore

__all__ = ["AssistantRead"]


class AssistantRead(BaseModel):
    id: str

    created_at: int

    model: str

    name: str

    object: str

    response_format: str

    temperature: float

    top_p: float

    description: Optional[str] = None

    instructions: Optional[str] = None

    meta_data: Optional[builtins.object] = None

    tool_resources: Optional[Dict[str, builtins.object]] = None

    tools: Optional[List[builtins.object]] = None

    user_id: Optional[str] = None

    vector_stores: Optional[List[VectorStore]] = None

    webhook_url: Optional[str] = None
