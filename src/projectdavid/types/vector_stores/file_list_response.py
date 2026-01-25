# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .vector_store_file import VectorStoreFile

__all__ = ["FileListResponse"]

FileListResponse: TypeAlias = List[VectorStoreFile]
