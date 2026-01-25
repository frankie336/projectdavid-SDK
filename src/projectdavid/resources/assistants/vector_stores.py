# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.assistants import vector_store_list_params, vector_store_attach_params, vector_store_detach_params
from ...types.assistants.vector_store_list_response import VectorStoreListResponse
from ...types.assistants.vector_store_attach_response import VectorStoreAttachResponse
from ...types.assistants.vector_store_detach_response import VectorStoreDetachResponse

__all__ = ["VectorStoresResource", "AsyncVectorStoresResource"]


class VectorStoresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VectorStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#accessing-raw-response-data-eg-headers
        """
        return VectorStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#with_streaming_response
        """
        return VectorStoresResourceWithStreamingResponse(self)

    def list(
        self,
        assistant_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreListResponse:
        """
        List Assistant Stores

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._get(
            f"/v1/assistants/{assistant_id}/vector-stores",
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
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            cast_to=VectorStoreListResponse,
        )

    def attach(
        self,
        vector_store_id: str,
        *,
        assistant_id: str,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreAttachResponse:
        """
        Attach Store

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._post(
            f"/v1/assistants/{assistant_id}/vector-stores/{vector_store_id}/attach",
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
                    vector_store_attach_params.VectorStoreAttachParams,
                ),
            ),
            cast_to=VectorStoreAttachResponse,
        )

    def detach(
        self,
        vector_store_id: str,
        *,
        assistant_id: str,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreDetachResponse:
        """
        Detach Store

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._delete(
            f"/v1/assistants/{assistant_id}/vector-stores/{vector_store_id}/detach",
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
                    vector_store_detach_params.VectorStoreDetachParams,
                ),
            ),
            cast_to=VectorStoreDetachResponse,
        )


class AsyncVectorStoresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVectorStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#with_streaming_response
        """
        return AsyncVectorStoresResourceWithStreamingResponse(self)

    async def list(
        self,
        assistant_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreListResponse:
        """
        List Assistant Stores

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._get(
            f"/v1/assistants/{assistant_id}/vector-stores",
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
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            cast_to=VectorStoreListResponse,
        )

    async def attach(
        self,
        vector_store_id: str,
        *,
        assistant_id: str,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreAttachResponse:
        """
        Attach Store

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._post(
            f"/v1/assistants/{assistant_id}/vector-stores/{vector_store_id}/attach",
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
                    vector_store_attach_params.VectorStoreAttachParams,
                ),
            ),
            cast_to=VectorStoreAttachResponse,
        )

    async def detach(
        self,
        vector_store_id: str,
        *,
        assistant_id: str,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreDetachResponse:
        """
        Detach Store

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._delete(
            f"/v1/assistants/{assistant_id}/vector-stores/{vector_store_id}/detach",
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
                    vector_store_detach_params.VectorStoreDetachParams,
                ),
            ),
            cast_to=VectorStoreDetachResponse,
        )


class VectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.list = to_raw_response_wrapper(
            vector_stores.list,
        )
        self.attach = to_raw_response_wrapper(
            vector_stores.attach,
        )
        self.detach = to_raw_response_wrapper(
            vector_stores.detach,
        )


class AsyncVectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.list = async_to_raw_response_wrapper(
            vector_stores.list,
        )
        self.attach = async_to_raw_response_wrapper(
            vector_stores.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            vector_stores.detach,
        )


class VectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.list = to_streamed_response_wrapper(
            vector_stores.list,
        )
        self.attach = to_streamed_response_wrapper(
            vector_stores.attach,
        )
        self.detach = to_streamed_response_wrapper(
            vector_stores.detach,
        )


class AsyncVectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.list = async_to_streamed_response_wrapper(
            vector_stores.list,
        )
        self.attach = async_to_streamed_response_wrapper(
            vector_stores.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            vector_stores.detach,
        )
