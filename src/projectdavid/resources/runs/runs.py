# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    RunStatus,
    TruncationStrategy,
    run_list_params,
    run_cancel_params,
    run_create_params,
    run_retrieve_params,
    run_stream_events_params,
    run_update_status_params,
    run_update_metadata_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.run import Run
from ..._base_client import make_request_options
from ...types.run_list import RunList
from ...types.run_status import RunStatus
from ...types.tool_param import ToolParam
from ...types.truncation_strategy import TruncationStrategy
from ...types.run_retrieve_response import RunRetrieveResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        args: object,
        kwargs: object,
        id: str,
        assistant_id: str,
        created_at: int,
        expires_at: int,
        instructions: str,
        thread_id: str,
        cancelled_at: Optional[int] | Omit = omit,
        completed_at: Optional[int] | Omit = omit,
        failed_at: Optional[int] | Omit = omit,
        incomplete_details: Optional[object] | Omit = omit,
        last_error: Optional[str] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_prompt_tokens: Optional[int] | Omit = omit,
        meta_data: object | Omit = omit,
        model: str | Omit = omit,
        object: str | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        required_action: Optional[str] | Omit = omit,
        response_format: str | Omit = omit,
        started_at: Optional[int] | Omit = omit,
        status: RunStatus | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: str | Omit = omit,
        tool_resources: object | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        truncation_strategy: Optional[TruncationStrategy] | Omit = omit,
        usage: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Run:
        """
        Create Run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/runs",
            body=maybe_transform(
                {
                    "id": id,
                    "assistant_id": assistant_id,
                    "created_at": created_at,
                    "expires_at": expires_at,
                    "instructions": instructions,
                    "thread_id": thread_id,
                    "cancelled_at": cancelled_at,
                    "completed_at": completed_at,
                    "failed_at": failed_at,
                    "incomplete_details": incomplete_details,
                    "last_error": last_error,
                    "max_completion_tokens": max_completion_tokens,
                    "max_prompt_tokens": max_prompt_tokens,
                    "meta_data": meta_data,
                    "model": model,
                    "object": object,
                    "parallel_tool_calls": parallel_tool_calls,
                    "required_action": required_action,
                    "response_format": response_format,
                    "started_at": started_at,
                    "status": status,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tool_resources": tool_resources,
                    "tools": tools,
                    "top_p": top_p,
                    "truncation_strategy": truncation_strategy,
                    "usage": usage,
                },
                run_create_params.RunCreateParams,
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
                    run_create_params.RunCreateParams,
                ),
            ),
            cast_to=Run,
        )

    def retrieve(
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
    ) -> RunRetrieveResponse:
        """
        Retrieve Run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v1/runs/{run_id}", run_id=run_id),
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
                    run_retrieve_params.RunRetrieveParams,
                ),
            ),
            cast_to=RunRetrieveResponse,
        )

    def list(
        self,
        *,
        args: object,
        kwargs: object,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunList:
        """
        List Runs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/runs",
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
                        "thread_id": thread_id,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunList,
        )

    def cancel(
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
    ) -> Run:
        """
        Cancel Run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            path_template("/v1/runs/{run_id}/cancel", run_id=run_id),
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
                    run_cancel_params.RunCancelParams,
                ),
            ),
            cast_to=Run,
        )

    def stream_events(
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
    ) -> None:
        """
        Stream run‑lifecycle events (SSE)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/v1/runs/{run_id}/events", run_id=run_id),
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
                    run_stream_events_params.RunStreamEventsParams,
                ),
            ),
            cast_to=NoneType,
        )

    def update_metadata(
        self,
        run_id: str,
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
    ) -> Run:
        """
        Update Run Metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._put(
            path_template("/v1/runs/{run_id}/metadata", run_id=run_id),
            body=maybe_transform(body, run_update_metadata_params.RunUpdateMetadataParams),
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
                    run_update_metadata_params.RunUpdateMetadataParams,
                ),
            ),
            cast_to=Run,
        )

    def update_status(
        self,
        run_id: str,
        *,
        args: object,
        kwargs: object,
        status: RunStatus,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Run:
        """
        Update Run Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._put(
            path_template("/v1/runs/{run_id}/status", run_id=run_id),
            body=maybe_transform({"status": status}, run_update_status_params.RunUpdateStatusParams),
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
                    run_update_status_params.RunUpdateStatusParams,
                ),
            ),
            cast_to=Run,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        args: object,
        kwargs: object,
        id: str,
        assistant_id: str,
        created_at: int,
        expires_at: int,
        instructions: str,
        thread_id: str,
        cancelled_at: Optional[int] | Omit = omit,
        completed_at: Optional[int] | Omit = omit,
        failed_at: Optional[int] | Omit = omit,
        incomplete_details: Optional[object] | Omit = omit,
        last_error: Optional[str] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_prompt_tokens: Optional[int] | Omit = omit,
        meta_data: object | Omit = omit,
        model: str | Omit = omit,
        object: str | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        required_action: Optional[str] | Omit = omit,
        response_format: str | Omit = omit,
        started_at: Optional[int] | Omit = omit,
        status: RunStatus | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: str | Omit = omit,
        tool_resources: object | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        truncation_strategy: Optional[TruncationStrategy] | Omit = omit,
        usage: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Run:
        """
        Create Run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/runs",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "assistant_id": assistant_id,
                    "created_at": created_at,
                    "expires_at": expires_at,
                    "instructions": instructions,
                    "thread_id": thread_id,
                    "cancelled_at": cancelled_at,
                    "completed_at": completed_at,
                    "failed_at": failed_at,
                    "incomplete_details": incomplete_details,
                    "last_error": last_error,
                    "max_completion_tokens": max_completion_tokens,
                    "max_prompt_tokens": max_prompt_tokens,
                    "meta_data": meta_data,
                    "model": model,
                    "object": object,
                    "parallel_tool_calls": parallel_tool_calls,
                    "required_action": required_action,
                    "response_format": response_format,
                    "started_at": started_at,
                    "status": status,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tool_resources": tool_resources,
                    "tools": tools,
                    "top_p": top_p,
                    "truncation_strategy": truncation_strategy,
                    "usage": usage,
                },
                run_create_params.RunCreateParams,
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
                    run_create_params.RunCreateParams,
                ),
            ),
            cast_to=Run,
        )

    async def retrieve(
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
    ) -> RunRetrieveResponse:
        """
        Retrieve Run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v1/runs/{run_id}", run_id=run_id),
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
                    run_retrieve_params.RunRetrieveParams,
                ),
            ),
            cast_to=RunRetrieveResponse,
        )

    async def list(
        self,
        *,
        args: object,
        kwargs: object,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunList:
        """
        List Runs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/runs",
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
                        "thread_id": thread_id,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunList,
        )

    async def cancel(
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
    ) -> Run:
        """
        Cancel Run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            path_template("/v1/runs/{run_id}/cancel", run_id=run_id),
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
                    run_cancel_params.RunCancelParams,
                ),
            ),
            cast_to=Run,
        )

    async def stream_events(
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
    ) -> None:
        """
        Stream run‑lifecycle events (SSE)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/runs/{run_id}/events", run_id=run_id),
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
                    run_stream_events_params.RunStreamEventsParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def update_metadata(
        self,
        run_id: str,
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
    ) -> Run:
        """
        Update Run Metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._put(
            path_template("/v1/runs/{run_id}/metadata", run_id=run_id),
            body=await async_maybe_transform(body, run_update_metadata_params.RunUpdateMetadataParams),
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
                    run_update_metadata_params.RunUpdateMetadataParams,
                ),
            ),
            cast_to=Run,
        )

    async def update_status(
        self,
        run_id: str,
        *,
        args: object,
        kwargs: object,
        status: RunStatus,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Run:
        """
        Update Run Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._put(
            path_template("/v1/runs/{run_id}/status", run_id=run_id),
            body=await async_maybe_transform({"status": status}, run_update_status_params.RunUpdateStatusParams),
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
                    run_update_status_params.RunUpdateStatusParams,
                ),
            ),
            cast_to=Run,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_raw_response_wrapper(
            runs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.cancel = to_raw_response_wrapper(
            runs.cancel,
        )
        self.stream_events = to_raw_response_wrapper(
            runs.stream_events,
        )
        self.update_metadata = to_raw_response_wrapper(
            runs.update_metadata,
        )
        self.update_status = to_raw_response_wrapper(
            runs.update_status,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._runs.actions)


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_raw_response_wrapper(
            runs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            runs.cancel,
        )
        self.stream_events = async_to_raw_response_wrapper(
            runs.stream_events,
        )
        self.update_metadata = async_to_raw_response_wrapper(
            runs.update_metadata,
        )
        self.update_status = async_to_raw_response_wrapper(
            runs.update_status,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._runs.actions)


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_streamed_response_wrapper(
            runs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.cancel = to_streamed_response_wrapper(
            runs.cancel,
        )
        self.stream_events = to_streamed_response_wrapper(
            runs.stream_events,
        )
        self.update_metadata = to_streamed_response_wrapper(
            runs.update_metadata,
        )
        self.update_status = to_streamed_response_wrapper(
            runs.update_status,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._runs.actions)


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_streamed_response_wrapper(
            runs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            runs.cancel,
        )
        self.stream_events = async_to_streamed_response_wrapper(
            runs.stream_events,
        )
        self.update_metadata = async_to_streamed_response_wrapper(
            runs.update_metadata,
        )
        self.update_status = async_to_streamed_response_wrapper(
            runs.update_status,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._runs.actions)
