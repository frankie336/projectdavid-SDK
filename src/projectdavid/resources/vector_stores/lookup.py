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
from ...types.vector_store import VectorStore
from ...types.vector_stores import lookup_by_collection_name_params

__all__ = ["LookupResource", "AsyncLookupResource"]


class LookupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#accessing-raw-response-data-eg-headers
        """
        return LookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#with_streaming_response
        """
        return LookupResourceWithStreamingResponse(self)

    def by_collection_name(
        self,
        *,
        args: object,
        kwargs: object,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStore:
        """
        Retrieves vector-store metadata using its unique collection name.

        Args:
          name: Collection name to look up

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/vector-stores/lookup/collection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "name": name,
                    },
                    lookup_by_collection_name_params.LookupByCollectionNameParams,
                ),
            ),
            cast_to=VectorStore,
        )


class AsyncLookupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#with_streaming_response
        """
        return AsyncLookupResourceWithStreamingResponse(self)

    async def by_collection_name(
        self,
        *,
        args: object,
        kwargs: object,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStore:
        """
        Retrieves vector-store metadata using its unique collection name.

        Args:
          name: Collection name to look up

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/vector-stores/lookup/collection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "name": name,
                    },
                    lookup_by_collection_name_params.LookupByCollectionNameParams,
                ),
            ),
            cast_to=VectorStore,
        )


class LookupResourceWithRawResponse:
    def __init__(self, lookup: LookupResource) -> None:
        self._lookup = lookup

        self.by_collection_name = to_raw_response_wrapper(
            lookup.by_collection_name,
        )


class AsyncLookupResourceWithRawResponse:
    def __init__(self, lookup: AsyncLookupResource) -> None:
        self._lookup = lookup

        self.by_collection_name = async_to_raw_response_wrapper(
            lookup.by_collection_name,
        )


class LookupResourceWithStreamingResponse:
    def __init__(self, lookup: LookupResource) -> None:
        self._lookup = lookup

        self.by_collection_name = to_streamed_response_wrapper(
            lookup.by_collection_name,
        )


class AsyncLookupResourceWithStreamingResponse:
    def __init__(self, lookup: AsyncLookupResource) -> None:
        self._lookup = lookup

        self.by_collection_name = async_to_streamed_response_wrapper(
            lookup.by_collection_name,
        )
