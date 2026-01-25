# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import StatusEnum
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.status_enum import StatusEnum
from ...types.vector_stores import file_add_params, file_list_params, file_delete_params, file_update_status_params
from ...types.vector_stores.vector_store_file import VectorStoreFile
from ...types.vector_stores.file_list_response import FileListResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def list(
        self,
        vector_store_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        List Files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._get(
            f"/v1/vector-stores/{vector_store_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    def delete(
        self,
        vector_store_id: str,
        *,
        args: object,
        file_path: str,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete File

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/vector-stores/{vector_store_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "args": args,
                        "file_path": file_path,
                        "kwargs": kwargs,
                    },
                    file_delete_params.FileDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def add(
        self,
        vector_store_id: str,
        *,
        args: object,
        kwargs: object,
        file_id: str,
        file_name: str,
        file_path: str,
        meta_data: Optional[object] | Omit = omit,
        status: Optional[StatusEnum] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFile:
        """
        Add File

        Args:
          file_id: Client-assigned unique file record ID

          file_name: Original filename

          file_path: Identifier path in metadata

          meta_data: Arbitrary metadata

          status: Initial processing state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._post(
            f"/v1/vector-stores/{vector_store_id}/files",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "file_name": file_name,
                    "file_path": file_path,
                    "meta_data": meta_data,
                    "status": status,
                },
                file_add_params.FileAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                    },
                    file_add_params.FileAddParams,
                ),
            ),
            cast_to=VectorStoreFile,
        )

    def update_status(
        self,
        file_id: str,
        *,
        vector_store_id: str,
        args: object,
        kwargs: object,
        status: StatusEnum,
        error_message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFile:
        """
        Update File Status

        Args:
          status: New status for the file record

          error_message: Error message if status is 'failed'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._patch(
            f"/v1/vector-stores/{vector_store_id}/files/{file_id}",
            body=maybe_transform(
                {
                    "status": status,
                    "error_message": error_message,
                },
                file_update_status_params.FileUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                    },
                    file_update_status_params.FileUpdateStatusParams,
                ),
            ),
            cast_to=VectorStoreFile,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def list(
        self,
        vector_store_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        List Files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._get(
            f"/v1/vector-stores/{vector_store_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    async def delete(
        self,
        vector_store_id: str,
        *,
        args: object,
        file_path: str,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete File

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/vector-stores/{vector_store_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "args": args,
                        "file_path": file_path,
                        "kwargs": kwargs,
                    },
                    file_delete_params.FileDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def add(
        self,
        vector_store_id: str,
        *,
        args: object,
        kwargs: object,
        file_id: str,
        file_name: str,
        file_path: str,
        meta_data: Optional[object] | Omit = omit,
        status: Optional[StatusEnum] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFile:
        """
        Add File

        Args:
          file_id: Client-assigned unique file record ID

          file_name: Original filename

          file_path: Identifier path in metadata

          meta_data: Arbitrary metadata

          status: Initial processing state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._post(
            f"/v1/vector-stores/{vector_store_id}/files",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "file_name": file_name,
                    "file_path": file_path,
                    "meta_data": meta_data,
                    "status": status,
                },
                file_add_params.FileAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                    },
                    file_add_params.FileAddParams,
                ),
            ),
            cast_to=VectorStoreFile,
        )

    async def update_status(
        self,
        file_id: str,
        *,
        vector_store_id: str,
        args: object,
        kwargs: object,
        status: StatusEnum,
        error_message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFile:
        """
        Update File Status

        Args:
          status: New status for the file record

          error_message: Error message if status is 'failed'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._patch(
            f"/v1/vector-stores/{vector_store_id}/files/{file_id}",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "error_message": error_message,
                },
                file_update_status_params.FileUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                    },
                    file_update_status_params.FileUpdateStatusParams,
                ),
            ),
            cast_to=VectorStoreFile,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.add = to_raw_response_wrapper(
            files.add,
        )
        self.update_status = to_raw_response_wrapper(
            files.update_status,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.add = async_to_raw_response_wrapper(
            files.add,
        )
        self.update_status = async_to_raw_response_wrapper(
            files.update_status,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.add = to_streamed_response_wrapper(
            files.add,
        )
        self.update_status = to_streamed_response_wrapper(
            files.update_status,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            files.add,
        )
        self.update_status = async_to_streamed_response_wrapper(
            files.update_status,
        )
