# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.users import assistant_associate_params, assistant_disassociate_params
from ..._base_client import make_request_options

__all__ = ["AssistantsResource", "AsyncAssistantsResource"]


class AssistantsResource(SyncAPIResource):
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

    def associate(
        self,
        assistant_id: str,
        *,
        user_id: str,
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
        Associate Assistant With User

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/assistants/{assistant_id}", user_id=user_id, assistant_id=assistant_id),
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
                    assistant_associate_params.AssistantAssociateParams,
                ),
            ),
            cast_to=object,
        )

    def disassociate(
        self,
        assistant_id: str,
        *,
        user_id: str,
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
        Disassociate Assistant From User

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/users/{user_id}/assistants/{assistant_id}", user_id=user_id, assistant_id=assistant_id),
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
                    assistant_disassociate_params.AssistantDisassociateParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncAssistantsResource(AsyncAPIResource):
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

    async def associate(
        self,
        assistant_id: str,
        *,
        user_id: str,
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
        Associate Assistant With User

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/assistants/{assistant_id}", user_id=user_id, assistant_id=assistant_id),
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
                    assistant_associate_params.AssistantAssociateParams,
                ),
            ),
            cast_to=object,
        )

    async def disassociate(
        self,
        assistant_id: str,
        *,
        user_id: str,
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
        Disassociate Assistant From User

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/users/{user_id}/assistants/{assistant_id}", user_id=user_id, assistant_id=assistant_id),
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
                    assistant_disassociate_params.AssistantDisassociateParams,
                ),
            ),
            cast_to=NoneType,
        )


class AssistantsResourceWithRawResponse:
    def __init__(self, assistants: AssistantsResource) -> None:
        self._assistants = assistants

        self.associate = to_raw_response_wrapper(
            assistants.associate,
        )
        self.disassociate = to_raw_response_wrapper(
            assistants.disassociate,
        )


class AsyncAssistantsResourceWithRawResponse:
    def __init__(self, assistants: AsyncAssistantsResource) -> None:
        self._assistants = assistants

        self.associate = async_to_raw_response_wrapper(
            assistants.associate,
        )
        self.disassociate = async_to_raw_response_wrapper(
            assistants.disassociate,
        )


class AssistantsResourceWithStreamingResponse:
    def __init__(self, assistants: AssistantsResource) -> None:
        self._assistants = assistants

        self.associate = to_streamed_response_wrapper(
            assistants.associate,
        )
        self.disassociate = to_streamed_response_wrapper(
            assistants.disassociate,
        )


class AsyncAssistantsResourceWithStreamingResponse:
    def __init__(self, assistants: AsyncAssistantsResource) -> None:
        self._assistants = assistants

        self.associate = async_to_streamed_response_wrapper(
            assistants.associate,
        )
        self.disassociate = async_to_streamed_response_wrapper(
            assistants.disassociate,
        )
