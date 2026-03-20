# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ...types import assistant_list_params, assistant_create_params, assistant_update_params, assistant_retrieve_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .vector_stores import (
    VectorStoresResource,
    AsyncVectorStoresResource,
    VectorStoresResourceWithRawResponse,
    AsyncVectorStoresResourceWithRawResponse,
    VectorStoresResourceWithStreamingResponse,
    AsyncVectorStoresResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.assistant_read import AssistantRead
from ...types.assistant_list_response import AssistantListResponse

__all__ = ["AssistantsResource", "AsyncAssistantsResource"]


class AssistantsResource(SyncAPIResource):
    @cached_property
    def vector_stores(self) -> VectorStoresResource:
        return VectorStoresResource(self._client)

    @cached_property
    def with_raw_response(self) -> AssistantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return AssistantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssistantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return AssistantsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        args: object,
        kwargs: object,
        model: str,
        name: str,
        id: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        instructions: str | Omit = omit,
        meta_data: Optional[object] | Omit = omit,
        response_format: str | Omit = omit,
        temperature: float | Omit = omit,
        tool_resources: Optional[Dict[str, object]] | Omit = omit,
        tools: Optional[Iterable[object]] | Omit = omit,
        top_p: float | Omit = omit,
        webhook_secret: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantRead:
        """
        Create a new assistant.

        Args:
          model: LLM model ID

          name: Assistant name

          id: Optional pre-generated assistant ID.

          description: Brief description

          instructions: System instructions

          tools: OpenAI-style tool specs (dicts).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/assistants",
            body=maybe_transform(
                {
                    "model": model,
                    "name": name,
                    "id": id,
                    "description": description,
                    "instructions": instructions,
                    "meta_data": meta_data,
                    "response_format": response_format,
                    "temperature": temperature,
                    "tool_resources": tool_resources,
                    "tools": tools,
                    "top_p": top_p,
                    "webhook_secret": webhook_secret,
                    "webhook_url": webhook_url,
                },
                assistant_create_params.AssistantCreateParams,
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
                    assistant_create_params.AssistantCreateParams,
                ),
            ),
            cast_to=AssistantRead,
        )

    def retrieve(
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
    ) -> AssistantRead:
        """
        Get Assistant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._get(
            path_template("/v1/assistants/{assistant_id}", assistant_id=assistant_id),
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
                    assistant_retrieve_params.AssistantRetrieveParams,
                ),
            ),
            cast_to=AssistantRead,
        )

    def update(
        self,
        assistant_id: str,
        *,
        args: object,
        kwargs: object,
        description: Optional[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        meta_data: Optional[object] | Omit = omit,
        model: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        response_format: Optional[str] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_resources: Optional[Dict[str, object]] | Omit = omit,
        tools: Optional[SequenceNotStr[str]] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        users: Optional[SequenceNotStr[str]] | Omit = omit,
        vector_stores: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_secret: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantRead:
        """
        Update any mutable assistant fields – including `tool_resources`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._put(
            path_template("/v1/assistants/{assistant_id}", assistant_id=assistant_id),
            body=maybe_transform(
                {
                    "description": description,
                    "instructions": instructions,
                    "meta_data": meta_data,
                    "model": model,
                    "name": name,
                    "response_format": response_format,
                    "temperature": temperature,
                    "tool_resources": tool_resources,
                    "tools": tools,
                    "top_p": top_p,
                    "users": users,
                    "vector_stores": vector_stores,
                    "webhook_secret": webhook_secret,
                    "webhook_url": webhook_url,
                },
                assistant_update_params.AssistantUpdateParams,
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
                    assistant_update_params.AssistantUpdateParams,
                ),
            ),
            cast_to=AssistantRead,
        )

    def list(
        self,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantListResponse:
        """
        List assistants for the caller (derived from API-key).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/assistants",
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
                    assistant_list_params.AssistantListParams,
                ),
            ),
            cast_to=AssistantListResponse,
        )


class AsyncAssistantsResource(AsyncAPIResource):
    @cached_property
    def vector_stores(self) -> AsyncVectorStoresResource:
        return AsyncVectorStoresResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssistantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncAssistantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssistantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return AsyncAssistantsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        args: object,
        kwargs: object,
        model: str,
        name: str,
        id: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        instructions: str | Omit = omit,
        meta_data: Optional[object] | Omit = omit,
        response_format: str | Omit = omit,
        temperature: float | Omit = omit,
        tool_resources: Optional[Dict[str, object]] | Omit = omit,
        tools: Optional[Iterable[object]] | Omit = omit,
        top_p: float | Omit = omit,
        webhook_secret: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantRead:
        """
        Create a new assistant.

        Args:
          model: LLM model ID

          name: Assistant name

          id: Optional pre-generated assistant ID.

          description: Brief description

          instructions: System instructions

          tools: OpenAI-style tool specs (dicts).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/assistants",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "name": name,
                    "id": id,
                    "description": description,
                    "instructions": instructions,
                    "meta_data": meta_data,
                    "response_format": response_format,
                    "temperature": temperature,
                    "tool_resources": tool_resources,
                    "tools": tools,
                    "top_p": top_p,
                    "webhook_secret": webhook_secret,
                    "webhook_url": webhook_url,
                },
                assistant_create_params.AssistantCreateParams,
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
                    assistant_create_params.AssistantCreateParams,
                ),
            ),
            cast_to=AssistantRead,
        )

    async def retrieve(
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
    ) -> AssistantRead:
        """
        Get Assistant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._get(
            path_template("/v1/assistants/{assistant_id}", assistant_id=assistant_id),
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
                    assistant_retrieve_params.AssistantRetrieveParams,
                ),
            ),
            cast_to=AssistantRead,
        )

    async def update(
        self,
        assistant_id: str,
        *,
        args: object,
        kwargs: object,
        description: Optional[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        meta_data: Optional[object] | Omit = omit,
        model: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        response_format: Optional[str] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_resources: Optional[Dict[str, object]] | Omit = omit,
        tools: Optional[SequenceNotStr[str]] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        users: Optional[SequenceNotStr[str]] | Omit = omit,
        vector_stores: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_secret: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantRead:
        """
        Update any mutable assistant fields – including `tool_resources`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._put(
            path_template("/v1/assistants/{assistant_id}", assistant_id=assistant_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "instructions": instructions,
                    "meta_data": meta_data,
                    "model": model,
                    "name": name,
                    "response_format": response_format,
                    "temperature": temperature,
                    "tool_resources": tool_resources,
                    "tools": tools,
                    "top_p": top_p,
                    "users": users,
                    "vector_stores": vector_stores,
                    "webhook_secret": webhook_secret,
                    "webhook_url": webhook_url,
                },
                assistant_update_params.AssistantUpdateParams,
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
                    assistant_update_params.AssistantUpdateParams,
                ),
            ),
            cast_to=AssistantRead,
        )

    async def list(
        self,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantListResponse:
        """
        List assistants for the caller (derived from API-key).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/assistants",
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
                    assistant_list_params.AssistantListParams,
                ),
            ),
            cast_to=AssistantListResponse,
        )


class AssistantsResourceWithRawResponse:
    def __init__(self, assistants: AssistantsResource) -> None:
        self._assistants = assistants

        self.create = to_raw_response_wrapper(
            assistants.create,
        )
        self.retrieve = to_raw_response_wrapper(
            assistants.retrieve,
        )
        self.update = to_raw_response_wrapper(
            assistants.update,
        )
        self.list = to_raw_response_wrapper(
            assistants.list,
        )

    @cached_property
    def vector_stores(self) -> VectorStoresResourceWithRawResponse:
        return VectorStoresResourceWithRawResponse(self._assistants.vector_stores)


class AsyncAssistantsResourceWithRawResponse:
    def __init__(self, assistants: AsyncAssistantsResource) -> None:
        self._assistants = assistants

        self.create = async_to_raw_response_wrapper(
            assistants.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            assistants.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            assistants.update,
        )
        self.list = async_to_raw_response_wrapper(
            assistants.list,
        )

    @cached_property
    def vector_stores(self) -> AsyncVectorStoresResourceWithRawResponse:
        return AsyncVectorStoresResourceWithRawResponse(self._assistants.vector_stores)


class AssistantsResourceWithStreamingResponse:
    def __init__(self, assistants: AssistantsResource) -> None:
        self._assistants = assistants

        self.create = to_streamed_response_wrapper(
            assistants.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            assistants.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            assistants.update,
        )
        self.list = to_streamed_response_wrapper(
            assistants.list,
        )

    @cached_property
    def vector_stores(self) -> VectorStoresResourceWithStreamingResponse:
        return VectorStoresResourceWithStreamingResponse(self._assistants.vector_stores)


class AsyncAssistantsResourceWithStreamingResponse:
    def __init__(self, assistants: AsyncAssistantsResource) -> None:
        self._assistants = assistants

        self.create = async_to_streamed_response_wrapper(
            assistants.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            assistants.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            assistants.update,
        )
        self.list = async_to_streamed_response_wrapper(
            assistants.list,
        )

    @cached_property
    def vector_stores(self) -> AsyncVectorStoresResourceWithStreamingResponse:
        return AsyncVectorStoresResourceWithStreamingResponse(self._assistants.vector_stores)
