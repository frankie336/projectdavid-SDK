# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .api_key_details import APIKeyDetails

__all__ = ["ApikeyListResponse"]


class ApikeyListResponse(BaseModel):
    """
    Schema for the response when listing API keys for a user.
    Contains a list of key details.
    """

    keys: List[APIKeyDetails]
    """A list containing the details of the API keys associated with the user."""
