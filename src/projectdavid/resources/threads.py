# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    thread_create_params,
    thread_delete_params,
    thread_update_params,
    thread_retrieve_params,
    thread_list_runs_params,
    thread_list_messages_params,
    thread_update_metadata_params,
    thread_list_user_threads_params,
    thread_get_formatted_messages_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.run_list import RunList
from ..types.thread_detailed import ThreadDetailed
from ..types.thread_delete_response import ThreadDeleteResponse
from ..types.thread_list_messages_response import ThreadListMessagesResponse
from ..types.thread_list_user_threads_response import ThreadListUserThreadsResponse
from ..types.thread_get_formatted_messages_response import ThreadGetFormattedMessagesResponse

__all__ = ["ThreadsResource", "AsyncThreadsResource"]


class ThreadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return ThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return ThreadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        args: object,
        kwargs: object,
        meta_data: Optional[object] | Omit = omit,
        participant_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadDetailed:
        """Create a thread.

        If `participant_ids` are absent in the payload, we infer the
        caller from the authenticated API‑key.

        Args:
          meta_data: Optional metadata for the thread

          participant_ids: List of participant IDs. Omit to default to the authenticated user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/threads",
            body=maybe_transform(
                {
                    "meta_data": meta_data,
                    "participant_ids": participant_ids,
                },
                thread_create_params.ThreadCreateParams,
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
                    thread_create_params.ThreadCreateParams,
                ),
            ),
            cast_to=ThreadDetailed,
        )

    def retrieve(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadDetailed:
        """
        Get Thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/v1/threads/{thread_id}", thread_id=thread_id),
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
                    thread_retrieve_params.ThreadRetrieveParams,
                ),
            ),
            cast_to=ThreadDetailed,
        )

    def update(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        meta_data: Optional[object] | Omit = omit,
        participant_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_resources: Optional[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadDetailed:
        """
        Update Thread

        Args:
          meta_data: Updated metadata

          participant_ids: Updated list of participant IDs

          tool_resources: Updated tool resources for the thread

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._put(
            path_template("/v1/threads/{thread_id}", thread_id=thread_id),
            body=maybe_transform(
                {
                    "meta_data": meta_data,
                    "participant_ids": participant_ids,
                    "tool_resources": tool_resources,
                },
                thread_update_params.ThreadUpdateParams,
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
                    thread_update_params.ThreadUpdateParams,
                ),
            ),
            cast_to=ThreadDetailed,
        )

    def delete(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadDeleteResponse:
        """
        Delete Thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._delete(
            path_template("/v1/threads/{thread_id}", thread_id=thread_id),
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
                    thread_delete_params.ThreadDeleteParams,
                ),
            ),
            cast_to=ThreadDeleteResponse,
        )

    def get_formatted_messages(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetFormattedMessagesResponse:
        """
        Get Formatted Messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/v1/threads/{thread_id}/formatted_messages", thread_id=thread_id),
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
                    thread_get_formatted_messages_params.ThreadGetFormattedMessagesParams,
                ),
            ),
            cast_to=ThreadGetFormattedMessagesResponse,
        )

    def list_messages(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        limit: int | Omit = omit,
        order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadListMessagesResponse:
        """
        List Messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/v1/threads/{thread_id}/messages", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "limit": limit,
                        "order": order,
                    },
                    thread_list_messages_params.ThreadListMessagesParams,
                ),
            ),
            cast_to=ThreadListMessagesResponse,
        )

    def list_runs(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunList:
        """
        List Runs For Thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/v1/threads/{thread_id}/runs", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "limit": limit,
                        "order": order,
                    },
                    thread_list_runs_params.ThreadListRunsParams,
                ),
            ),
            cast_to=RunList,
        )

    def list_user_threads(
        self,
        user_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadListUserThreadsResponse:
        """
        List User Threads

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/threads/user/{user_id}", user_id=user_id),
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
                    thread_list_user_threads_params.ThreadListUserThreadsParams,
                ),
            ),
            cast_to=ThreadListUserThreadsResponse,
        )

    def update_metadata(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadDetailed:
        """
        Update Thread Metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._put(
            path_template("/v1/threads/{thread_id}/metadata", thread_id=thread_id),
            body=maybe_transform(body, thread_update_metadata_params.ThreadUpdateMetadataParams),
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
                    thread_update_metadata_params.ThreadUpdateMetadataParams,
                ),
            ),
            cast_to=ThreadDetailed,
        )


class AsyncThreadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return AsyncThreadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        args: object,
        kwargs: object,
        meta_data: Optional[object] | Omit = omit,
        participant_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadDetailed:
        """Create a thread.

        If `participant_ids` are absent in the payload, we infer the
        caller from the authenticated API‑key.

        Args:
          meta_data: Optional metadata for the thread

          participant_ids: List of participant IDs. Omit to default to the authenticated user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/threads",
            body=await async_maybe_transform(
                {
                    "meta_data": meta_data,
                    "participant_ids": participant_ids,
                },
                thread_create_params.ThreadCreateParams,
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
                    thread_create_params.ThreadCreateParams,
                ),
            ),
            cast_to=ThreadDetailed,
        )

    async def retrieve(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadDetailed:
        """
        Get Thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/v1/threads/{thread_id}", thread_id=thread_id),
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
                    thread_retrieve_params.ThreadRetrieveParams,
                ),
            ),
            cast_to=ThreadDetailed,
        )

    async def update(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        meta_data: Optional[object] | Omit = omit,
        participant_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tool_resources: Optional[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadDetailed:
        """
        Update Thread

        Args:
          meta_data: Updated metadata

          participant_ids: Updated list of participant IDs

          tool_resources: Updated tool resources for the thread

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._put(
            path_template("/v1/threads/{thread_id}", thread_id=thread_id),
            body=await async_maybe_transform(
                {
                    "meta_data": meta_data,
                    "participant_ids": participant_ids,
                    "tool_resources": tool_resources,
                },
                thread_update_params.ThreadUpdateParams,
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
                    thread_update_params.ThreadUpdateParams,
                ),
            ),
            cast_to=ThreadDetailed,
        )

    async def delete(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadDeleteResponse:
        """
        Delete Thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._delete(
            path_template("/v1/threads/{thread_id}", thread_id=thread_id),
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
                    thread_delete_params.ThreadDeleteParams,
                ),
            ),
            cast_to=ThreadDeleteResponse,
        )

    async def get_formatted_messages(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetFormattedMessagesResponse:
        """
        Get Formatted Messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/v1/threads/{thread_id}/formatted_messages", thread_id=thread_id),
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
                    thread_get_formatted_messages_params.ThreadGetFormattedMessagesParams,
                ),
            ),
            cast_to=ThreadGetFormattedMessagesResponse,
        )

    async def list_messages(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        limit: int | Omit = omit,
        order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadListMessagesResponse:
        """
        List Messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/v1/threads/{thread_id}/messages", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "limit": limit,
                        "order": order,
                    },
                    thread_list_messages_params.ThreadListMessagesParams,
                ),
            ),
            cast_to=ThreadListMessagesResponse,
        )

    async def list_runs(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunList:
        """
        List Runs For Thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/v1/threads/{thread_id}/runs", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "limit": limit,
                        "order": order,
                    },
                    thread_list_runs_params.ThreadListRunsParams,
                ),
            ),
            cast_to=RunList,
        )

    async def list_user_threads(
        self,
        user_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadListUserThreadsResponse:
        """
        List User Threads

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/threads/user/{user_id}", user_id=user_id),
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
                    thread_list_user_threads_params.ThreadListUserThreadsParams,
                ),
            ),
            cast_to=ThreadListUserThreadsResponse,
        )

    async def update_metadata(
        self,
        thread_id: str,
        *,
        args: object,
        kwargs: object,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadDetailed:
        """
        Update Thread Metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._put(
            path_template("/v1/threads/{thread_id}/metadata", thread_id=thread_id),
            body=await async_maybe_transform(body, thread_update_metadata_params.ThreadUpdateMetadataParams),
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
                    thread_update_metadata_params.ThreadUpdateMetadataParams,
                ),
            ),
            cast_to=ThreadDetailed,
        )


class ThreadsResourceWithRawResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.create = to_raw_response_wrapper(
            threads.create,
        )
        self.retrieve = to_raw_response_wrapper(
            threads.retrieve,
        )
        self.update = to_raw_response_wrapper(
            threads.update,
        )
        self.delete = to_raw_response_wrapper(
            threads.delete,
        )
        self.get_formatted_messages = to_raw_response_wrapper(
            threads.get_formatted_messages,
        )
        self.list_messages = to_raw_response_wrapper(
            threads.list_messages,
        )
        self.list_runs = to_raw_response_wrapper(
            threads.list_runs,
        )
        self.list_user_threads = to_raw_response_wrapper(
            threads.list_user_threads,
        )
        self.update_metadata = to_raw_response_wrapper(
            threads.update_metadata,
        )


class AsyncThreadsResourceWithRawResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.create = async_to_raw_response_wrapper(
            threads.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            threads.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            threads.update,
        )
        self.delete = async_to_raw_response_wrapper(
            threads.delete,
        )
        self.get_formatted_messages = async_to_raw_response_wrapper(
            threads.get_formatted_messages,
        )
        self.list_messages = async_to_raw_response_wrapper(
            threads.list_messages,
        )
        self.list_runs = async_to_raw_response_wrapper(
            threads.list_runs,
        )
        self.list_user_threads = async_to_raw_response_wrapper(
            threads.list_user_threads,
        )
        self.update_metadata = async_to_raw_response_wrapper(
            threads.update_metadata,
        )


class ThreadsResourceWithStreamingResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.create = to_streamed_response_wrapper(
            threads.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            threads.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            threads.update,
        )
        self.delete = to_streamed_response_wrapper(
            threads.delete,
        )
        self.get_formatted_messages = to_streamed_response_wrapper(
            threads.get_formatted_messages,
        )
        self.list_messages = to_streamed_response_wrapper(
            threads.list_messages,
        )
        self.list_runs = to_streamed_response_wrapper(
            threads.list_runs,
        )
        self.list_user_threads = to_streamed_response_wrapper(
            threads.list_user_threads,
        )
        self.update_metadata = to_streamed_response_wrapper(
            threads.update_metadata,
        )


class AsyncThreadsResourceWithStreamingResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.create = async_to_streamed_response_wrapper(
            threads.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            threads.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            threads.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            threads.delete,
        )
        self.get_formatted_messages = async_to_streamed_response_wrapper(
            threads.get_formatted_messages,
        )
        self.list_messages = async_to_streamed_response_wrapper(
            threads.list_messages,
        )
        self.list_runs = async_to_streamed_response_wrapper(
            threads.list_runs,
        )
        self.list_user_threads = async_to_streamed_response_wrapper(
            threads.list_user_threads,
        )
        self.update_metadata = async_to_streamed_response_wrapper(
            threads.update_metadata,
        )
