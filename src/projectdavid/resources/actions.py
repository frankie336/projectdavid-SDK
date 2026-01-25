# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    action_create_params,
    action_delete_params,
    action_update_params,
    action_retrieve_params,
    action_list_pending_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.action_read import ActionRead
from ..types.action_list_pending_response import ActionListPendingResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        args: object,
        kwargs: object,
        run_id: str,
        id: Optional[str] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        function_args: Optional[object] | Omit = omit,
        status: Optional[str] | Omit = omit,
        tool_call_id: Optional[str] | Omit = omit,
        tool_name: Optional[str] | Omit = omit,
        turn_index: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRead:
        """
        Create Action

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/actions",
            body=maybe_transform(
                {
                    "run_id": run_id,
                    "id": id,
                    "expires_at": expires_at,
                    "function_args": function_args,
                    "status": status,
                    "tool_call_id": tool_call_id,
                    "tool_name": tool_name,
                    "turn_index": turn_index,
                },
                action_create_params.ActionCreateParams,
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
                    action_create_params.ActionCreateParams,
                ),
            ),
            cast_to=ActionRead,
        )

    def retrieve(
        self,
        action_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRead:
        """
        Get Action

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        return self._get(
            f"/v1/actions/{action_id}",
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
                    action_retrieve_params.ActionRetrieveParams,
                ),
            ),
            cast_to=ActionRead,
        )

    def update(
        self,
        action_id: str,
        *,
        args: object,
        kwargs: object,
        status: Literal["pending", "processing", "completed", "failed", "expired", "cancelled", "retrying"],
        result: Optional[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRead:
        """
        Update Action Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        return self._put(
            f"/v1/actions/{action_id}",
            body=maybe_transform(
                {
                    "status": status,
                    "result": result,
                },
                action_update_params.ActionUpdateParams,
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
                    action_update_params.ActionUpdateParams,
                ),
            ),
            cast_to=ActionRead,
        )

    def delete(
        self,
        action_id: str,
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
        Delete Action

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/actions/{action_id}",
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
                    action_delete_params.ActionDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def list_pending(
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
    ) -> ActionListPendingResponse:
        """
        Retrieve all pending actions with their function arguments, tool names, and run
        details. Filter by run_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            f"/v1/actions/pending/{run_id}",
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
                    action_list_pending_params.ActionListPendingParams,
                ),
            ),
            cast_to=ActionListPendingResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        args: object,
        kwargs: object,
        run_id: str,
        id: Optional[str] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        function_args: Optional[object] | Omit = omit,
        status: Optional[str] | Omit = omit,
        tool_call_id: Optional[str] | Omit = omit,
        tool_name: Optional[str] | Omit = omit,
        turn_index: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRead:
        """
        Create Action

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/actions",
            body=await async_maybe_transform(
                {
                    "run_id": run_id,
                    "id": id,
                    "expires_at": expires_at,
                    "function_args": function_args,
                    "status": status,
                    "tool_call_id": tool_call_id,
                    "tool_name": tool_name,
                    "turn_index": turn_index,
                },
                action_create_params.ActionCreateParams,
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
                    action_create_params.ActionCreateParams,
                ),
            ),
            cast_to=ActionRead,
        )

    async def retrieve(
        self,
        action_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRead:
        """
        Get Action

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        return await self._get(
            f"/v1/actions/{action_id}",
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
                    action_retrieve_params.ActionRetrieveParams,
                ),
            ),
            cast_to=ActionRead,
        )

    async def update(
        self,
        action_id: str,
        *,
        args: object,
        kwargs: object,
        status: Literal["pending", "processing", "completed", "failed", "expired", "cancelled", "retrying"],
        result: Optional[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRead:
        """
        Update Action Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        return await self._put(
            f"/v1/actions/{action_id}",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "result": result,
                },
                action_update_params.ActionUpdateParams,
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
                    action_update_params.ActionUpdateParams,
                ),
            ),
            cast_to=ActionRead,
        )

    async def delete(
        self,
        action_id: str,
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
        Delete Action

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/actions/{action_id}",
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
                    action_delete_params.ActionDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def list_pending(
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
    ) -> ActionListPendingResponse:
        """
        Retrieve all pending actions with their function arguments, tool names, and run
        details. Filter by run_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            f"/v1/actions/pending/{run_id}",
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
                    action_list_pending_params.ActionListPendingParams,
                ),
            ),
            cast_to=ActionListPendingResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.create = to_raw_response_wrapper(
            actions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            actions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            actions.update,
        )
        self.delete = to_raw_response_wrapper(
            actions.delete,
        )
        self.list_pending = to_raw_response_wrapper(
            actions.list_pending,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.create = async_to_raw_response_wrapper(
            actions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            actions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            actions.update,
        )
        self.delete = async_to_raw_response_wrapper(
            actions.delete,
        )
        self.list_pending = async_to_raw_response_wrapper(
            actions.list_pending,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.create = to_streamed_response_wrapper(
            actions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            actions.update,
        )
        self.delete = to_streamed_response_wrapper(
            actions.delete,
        )
        self.list_pending = to_streamed_response_wrapper(
            actions.list_pending,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.create = async_to_streamed_response_wrapper(
            actions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            actions.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            actions.delete,
        )
        self.list_pending = async_to_streamed_response_wrapper(
            actions.list_pending,
        )
