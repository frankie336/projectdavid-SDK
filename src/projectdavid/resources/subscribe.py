# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import subscribe_retrieve_run_events_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["SubscribeResource", "AsyncSubscribeResource"]


class SubscribeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return SubscribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return SubscribeResourceWithStreamingResponse(self)

    def retrieve_run_events(
        self,
        run_id: str,
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
        Client connects here using Server-Sent Events (SSE) to receive real-time events
        for a specific run_id. Requires a valid API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v1/subscribe/{run_id}", run_id=run_id),
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
                    subscribe_retrieve_run_events_params.SubscribeRetrieveRunEventsParams,
                ),
            ),
            cast_to=object,
        )


class AsyncSubscribeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return AsyncSubscribeResourceWithStreamingResponse(self)

    async def retrieve_run_events(
        self,
        run_id: str,
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
        Client connects here using Server-Sent Events (SSE) to receive real-time events
        for a specific run_id. Requires a valid API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v1/subscribe/{run_id}", run_id=run_id),
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
                    subscribe_retrieve_run_events_params.SubscribeRetrieveRunEventsParams,
                ),
            ),
            cast_to=object,
        )


class SubscribeResourceWithRawResponse:
    def __init__(self, subscribe: SubscribeResource) -> None:
        self._subscribe = subscribe

        self.retrieve_run_events = to_raw_response_wrapper(
            subscribe.retrieve_run_events,
        )


class AsyncSubscribeResourceWithRawResponse:
    def __init__(self, subscribe: AsyncSubscribeResource) -> None:
        self._subscribe = subscribe

        self.retrieve_run_events = async_to_raw_response_wrapper(
            subscribe.retrieve_run_events,
        )


class SubscribeResourceWithStreamingResponse:
    def __init__(self, subscribe: SubscribeResource) -> None:
        self._subscribe = subscribe

        self.retrieve_run_events = to_streamed_response_wrapper(
            subscribe.retrieve_run_events,
        )


class AsyncSubscribeResourceWithStreamingResponse:
    def __init__(self, subscribe: AsyncSubscribeResource) -> None:
        self._subscribe = subscribe

        self.retrieve_run_events = async_to_streamed_response_wrapper(
            subscribe.retrieve_run_events,
        )
