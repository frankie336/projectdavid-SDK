# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    message_create_params,
    message_delete_params,
    message_retrieve_params,
    message_submit_tool_response_params,
    message_save_assistant_message_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.message_read import MessageRead
from ..types.message_delete_response import MessageDeleteResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        args: object,
        kwargs: object,
        assistant_id: str,
        content: str,
        role: str,
        thread_id: str,
        is_last_chunk: bool | Omit = omit,
        meta_data: Optional[object] | Omit = omit,
        sender_id: Optional[str] | Omit = omit,
        tool_call_id: Optional[str] | Omit = omit,
        tool_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRead:
        """
        Create Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages",
            body=maybe_transform(
                {
                    "assistant_id": assistant_id,
                    "content": content,
                    "role": role,
                    "thread_id": thread_id,
                    "is_last_chunk": is_last_chunk,
                    "meta_data": meta_data,
                    "sender_id": sender_id,
                    "tool_call_id": tool_call_id,
                    "tool_id": tool_id,
                },
                message_create_params.MessageCreateParams,
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
                    message_create_params.MessageCreateParams,
                ),
            ),
            cast_to=MessageRead,
        )

    def retrieve(
        self,
        message_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRead:
        """
        Get Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template("/v1/messages/{message_id}", message_id=message_id),
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
                    message_retrieve_params.MessageRetrieveParams,
                ),
            ),
            cast_to=MessageRead,
        )

    def delete(
        self,
        message_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageDeleteResponse:
        """
        Delete Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            path_template("/v1/messages/{message_id}", message_id=message_id),
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
                    message_delete_params.MessageDeleteParams,
                ),
            ),
            cast_to=MessageDeleteResponse,
        )

    def save_assistant_message(
        self,
        *,
        args: object,
        kwargs: object,
        assistant_id: str,
        content: str,
        role: str,
        thread_id: str,
        is_last_chunk: bool | Omit = omit,
        meta_data: Optional[object] | Omit = omit,
        sender_id: Optional[str] | Omit = omit,
        tool_call_id: Optional[str] | Omit = omit,
        tool_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRead:
        """
        Save Assistant Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages/assistant",
            body=maybe_transform(
                {
                    "assistant_id": assistant_id,
                    "content": content,
                    "role": role,
                    "thread_id": thread_id,
                    "is_last_chunk": is_last_chunk,
                    "meta_data": meta_data,
                    "sender_id": sender_id,
                    "tool_call_id": tool_call_id,
                    "tool_id": tool_id,
                },
                message_save_assistant_message_params.MessageSaveAssistantMessageParams,
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
                    message_save_assistant_message_params.MessageSaveAssistantMessageParams,
                ),
            ),
            cast_to=MessageRead,
        )

    def submit_tool_response(
        self,
        *,
        args: object,
        kwargs: object,
        assistant_id: str,
        content: str,
        role: str,
        thread_id: str,
        is_last_chunk: bool | Omit = omit,
        meta_data: Optional[object] | Omit = omit,
        sender_id: Optional[str] | Omit = omit,
        tool_call_id: Optional[str] | Omit = omit,
        tool_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRead:
        """
        Submit Tool Response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages/tools",
            body=maybe_transform(
                {
                    "assistant_id": assistant_id,
                    "content": content,
                    "role": role,
                    "thread_id": thread_id,
                    "is_last_chunk": is_last_chunk,
                    "meta_data": meta_data,
                    "sender_id": sender_id,
                    "tool_call_id": tool_call_id,
                    "tool_id": tool_id,
                },
                message_submit_tool_response_params.MessageSubmitToolResponseParams,
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
                    message_submit_tool_response_params.MessageSubmitToolResponseParams,
                ),
            ),
            cast_to=MessageRead,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        args: object,
        kwargs: object,
        assistant_id: str,
        content: str,
        role: str,
        thread_id: str,
        is_last_chunk: bool | Omit = omit,
        meta_data: Optional[object] | Omit = omit,
        sender_id: Optional[str] | Omit = omit,
        tool_call_id: Optional[str] | Omit = omit,
        tool_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRead:
        """
        Create Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages",
            body=await async_maybe_transform(
                {
                    "assistant_id": assistant_id,
                    "content": content,
                    "role": role,
                    "thread_id": thread_id,
                    "is_last_chunk": is_last_chunk,
                    "meta_data": meta_data,
                    "sender_id": sender_id,
                    "tool_call_id": tool_call_id,
                    "tool_id": tool_id,
                },
                message_create_params.MessageCreateParams,
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
                    message_create_params.MessageCreateParams,
                ),
            ),
            cast_to=MessageRead,
        )

    async def retrieve(
        self,
        message_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRead:
        """
        Get Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template("/v1/messages/{message_id}", message_id=message_id),
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
                    message_retrieve_params.MessageRetrieveParams,
                ),
            ),
            cast_to=MessageRead,
        )

    async def delete(
        self,
        message_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageDeleteResponse:
        """
        Delete Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            path_template("/v1/messages/{message_id}", message_id=message_id),
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
                    message_delete_params.MessageDeleteParams,
                ),
            ),
            cast_to=MessageDeleteResponse,
        )

    async def save_assistant_message(
        self,
        *,
        args: object,
        kwargs: object,
        assistant_id: str,
        content: str,
        role: str,
        thread_id: str,
        is_last_chunk: bool | Omit = omit,
        meta_data: Optional[object] | Omit = omit,
        sender_id: Optional[str] | Omit = omit,
        tool_call_id: Optional[str] | Omit = omit,
        tool_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRead:
        """
        Save Assistant Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages/assistant",
            body=await async_maybe_transform(
                {
                    "assistant_id": assistant_id,
                    "content": content,
                    "role": role,
                    "thread_id": thread_id,
                    "is_last_chunk": is_last_chunk,
                    "meta_data": meta_data,
                    "sender_id": sender_id,
                    "tool_call_id": tool_call_id,
                    "tool_id": tool_id,
                },
                message_save_assistant_message_params.MessageSaveAssistantMessageParams,
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
                    message_save_assistant_message_params.MessageSaveAssistantMessageParams,
                ),
            ),
            cast_to=MessageRead,
        )

    async def submit_tool_response(
        self,
        *,
        args: object,
        kwargs: object,
        assistant_id: str,
        content: str,
        role: str,
        thread_id: str,
        is_last_chunk: bool | Omit = omit,
        meta_data: Optional[object] | Omit = omit,
        sender_id: Optional[str] | Omit = omit,
        tool_call_id: Optional[str] | Omit = omit,
        tool_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRead:
        """
        Submit Tool Response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages/tools",
            body=await async_maybe_transform(
                {
                    "assistant_id": assistant_id,
                    "content": content,
                    "role": role,
                    "thread_id": thread_id,
                    "is_last_chunk": is_last_chunk,
                    "meta_data": meta_data,
                    "sender_id": sender_id,
                    "tool_call_id": tool_call_id,
                    "tool_id": tool_id,
                },
                message_submit_tool_response_params.MessageSubmitToolResponseParams,
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
                    message_submit_tool_response_params.MessageSubmitToolResponseParams,
                ),
            ),
            cast_to=MessageRead,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_raw_response_wrapper(
            messages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            messages.delete,
        )
        self.save_assistant_message = to_raw_response_wrapper(
            messages.save_assistant_message,
        )
        self.submit_tool_response = to_raw_response_wrapper(
            messages.submit_tool_response,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_raw_response_wrapper(
            messages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            messages.delete,
        )
        self.save_assistant_message = async_to_raw_response_wrapper(
            messages.save_assistant_message,
        )
        self.submit_tool_response = async_to_raw_response_wrapper(
            messages.submit_tool_response,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_streamed_response_wrapper(
            messages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            messages.delete,
        )
        self.save_assistant_message = to_streamed_response_wrapper(
            messages.save_assistant_message,
        )
        self.submit_tool_response = to_streamed_response_wrapper(
            messages.submit_tool_response,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_streamed_response_wrapper(
            messages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            messages.delete,
        )
        self.save_assistant_message = async_to_streamed_response_wrapper(
            messages.save_assistant_message,
        )
        self.submit_tool_response = async_to_streamed_response_wrapper(
            messages.submit_tool_response,
        )
