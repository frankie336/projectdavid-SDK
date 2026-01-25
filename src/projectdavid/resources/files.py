# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import file_delete_params, file_retrieve_params, file_get_base64_params, file_generate_signed_url_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.file import File
from .._base_client import make_request_options
from ..types.file_delete_response import FileDeleteResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        file_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Retrieve file metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/v1/files/{file_id}",
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
                    file_retrieve_params.FileRetrieveParams,
                ),
            ),
            cast_to=File,
        )

    def delete(
        self,
        file_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileDeleteResponse:
        """
        Delete a file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._delete(
            f"/v1/files/{file_id}",
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
                    file_delete_params.FileDeleteParams,
                ),
            ),
            cast_to=FileDeleteResponse,
        )

    def generate_signed_url(
        self,
        file_id: str,
        *,
        args: object,
        kwargs: object,
        expires_in: int | Omit = omit,
        use_real_filename: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Returns {'signed_url': ...}

        Args:
          expires_in: Seconds until link expires

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/v1/files/{file_id}/signed-url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "expires_in": expires_in,
                        "use_real_filename": use_real_filename,
                    },
                    file_generate_signed_url_params.FileGenerateSignedURLParams,
                ),
            ),
            cast_to=object,
        )

    def get_base64(
        self,
        file_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get file as Base64

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/v1/files/{file_id}/base64",
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
                    file_get_base64_params.FileGetBase64Params,
                ),
            ),
            cast_to=object,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        file_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Retrieve file metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/v1/files/{file_id}",
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
                    file_retrieve_params.FileRetrieveParams,
                ),
            ),
            cast_to=File,
        )

    async def delete(
        self,
        file_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileDeleteResponse:
        """
        Delete a file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._delete(
            f"/v1/files/{file_id}",
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
                    file_delete_params.FileDeleteParams,
                ),
            ),
            cast_to=FileDeleteResponse,
        )

    async def generate_signed_url(
        self,
        file_id: str,
        *,
        args: object,
        kwargs: object,
        expires_in: int | Omit = omit,
        use_real_filename: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Returns {'signed_url': ...}

        Args:
          expires_in: Seconds until link expires

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/v1/files/{file_id}/signed-url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "expires_in": expires_in,
                        "use_real_filename": use_real_filename,
                    },
                    file_generate_signed_url_params.FileGenerateSignedURLParams,
                ),
            ),
            cast_to=object,
        )

    async def get_base64(
        self,
        file_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get file as Base64

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/v1/files/{file_id}/base64",
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
                    file_get_base64_params.FileGetBase64Params,
                ),
            ),
            cast_to=object,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.retrieve = to_raw_response_wrapper(
            files.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.generate_signed_url = to_raw_response_wrapper(
            files.generate_signed_url,
        )
        self.get_base64 = to_raw_response_wrapper(
            files.get_base64,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.retrieve = async_to_raw_response_wrapper(
            files.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.generate_signed_url = async_to_raw_response_wrapper(
            files.generate_signed_url,
        )
        self.get_base64 = async_to_raw_response_wrapper(
            files.get_base64,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.retrieve = to_streamed_response_wrapper(
            files.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.generate_signed_url = to_streamed_response_wrapper(
            files.generate_signed_url,
        )
        self.get_base64 = to_streamed_response_wrapper(
            files.get_base64,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.retrieve = async_to_streamed_response_wrapper(
            files.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.generate_signed_url = async_to_streamed_response_wrapper(
            files.generate_signed_url,
        )
        self.get_base64 = async_to_streamed_response_wrapper(
            files.get_base64,
        )
