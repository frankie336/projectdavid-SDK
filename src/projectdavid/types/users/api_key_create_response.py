# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .api_key_details import APIKeyDetails

__all__ = ["APIKeyCreateResponse"]


class APIKeyCreateResponse(BaseModel):
    """
    Schema for the response after successfully creating an API key.
    Crucially includes the plain text key which should be stored securely by the client.
    """

    details: APIKeyDetails
    """The details of the API key record that was created in the database."""

    plain_key: str
    """The generated API key.

    This is the ONLY time this key will be shown. Store it securely immediately.
    """
