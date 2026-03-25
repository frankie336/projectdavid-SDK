# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import user_create_params, user_delete_params, user_update_params, user_retrieve_params
from .apikeys import (
    ApikeysResource,
    AsyncApikeysResource,
    ApikeysResourceWithRawResponse,
    AsyncApikeysResourceWithRawResponse,
    ApikeysResourceWithStreamingResponse,
    AsyncApikeysResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .assistants import (
    AssistantsResource,
    AsyncAssistantsResource,
    AssistantsResourceWithRawResponse,
    AsyncAssistantsResourceWithRawResponse,
    AssistantsResourceWithStreamingResponse,
    AsyncAssistantsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.user_read import UserRead

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def assistants(self) -> AssistantsResource:
        return AssistantsResource(self._client)

    @cached_property
    def apikeys(self) -> ApikeysResource:
        return ApikeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        args: object,
        kwargs: object,
        email: Optional[str] | Omit = omit,
        email_verified: Optional[bool] | Omit = omit,
        family_name: Optional[str] | Omit = omit,
        full_name: Optional[str] | Omit = omit,
        given_name: Optional[str] | Omit = omit,
        oauth_provider: Optional[str] | Omit = omit,
        picture_url: Optional[str] | Omit = omit,
        provider_user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRead:
        """Creates a new user.

        Requires **Admin** authentication via API Key.

        Args:
          email: User's email address.

          email_verified: Email verification status.

          family_name: User's last name.

          full_name: User's full display name.

          given_name: User's first name.

          oauth_provider: Authentication provider (e.g., 'google', 'local').

          picture_url: URL to profile picture.

          provider_user_id: User ID from the OAuth provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users",
            body=maybe_transform(
                {
                    "email": email,
                    "email_verified": email_verified,
                    "family_name": family_name,
                    "full_name": full_name,
                    "given_name": given_name,
                    "oauth_provider": oauth_provider,
                    "picture_url": picture_url,
                    "provider_user_id": provider_user_id,
                },
                user_create_params.UserCreateParams,
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
                    user_create_params.UserCreateParams,
                ),
            ),
            cast_to=UserRead,
        )

    def retrieve(
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
    ) -> UserRead:
        """
        Retrieves details for a specific user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{user_id}", user_id=user_id),
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
                    user_retrieve_params.UserRetrieveParams,
                ),
            ),
            cast_to=UserRead,
        )

    def update(
        self,
        user_id: str,
        *,
        args: object,
        kwargs: object,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRead:
        """
        Updates details for a specific user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            path_template("/v1/users/{user_id}", user_id=user_id),
            body=maybe_transform({"name": name}, user_update_params.UserUpdateParams),
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
                    user_update_params.UserUpdateParams,
                ),
            ),
            cast_to=UserRead,
        )

    def delete(
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
    ) -> None:
        """Deletes a specific user.

        Requires **Admin** authentication.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/users/{user_id}", user_id=user_id),
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
                    user_delete_params.UserDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def assistants(self) -> AsyncAssistantsResource:
        return AsyncAssistantsResource(self._client)

    @cached_property
    def apikeys(self) -> AsyncApikeysResource:
        return AsyncApikeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        args: object,
        kwargs: object,
        email: Optional[str] | Omit = omit,
        email_verified: Optional[bool] | Omit = omit,
        family_name: Optional[str] | Omit = omit,
        full_name: Optional[str] | Omit = omit,
        given_name: Optional[str] | Omit = omit,
        oauth_provider: Optional[str] | Omit = omit,
        picture_url: Optional[str] | Omit = omit,
        provider_user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRead:
        """Creates a new user.

        Requires **Admin** authentication via API Key.

        Args:
          email: User's email address.

          email_verified: Email verification status.

          family_name: User's last name.

          full_name: User's full display name.

          given_name: User's first name.

          oauth_provider: Authentication provider (e.g., 'google', 'local').

          picture_url: URL to profile picture.

          provider_user_id: User ID from the OAuth provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "email_verified": email_verified,
                    "family_name": family_name,
                    "full_name": full_name,
                    "given_name": given_name,
                    "oauth_provider": oauth_provider,
                    "picture_url": picture_url,
                    "provider_user_id": provider_user_id,
                },
                user_create_params.UserCreateParams,
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
                    user_create_params.UserCreateParams,
                ),
            ),
            cast_to=UserRead,
        )

    async def retrieve(
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
    ) -> UserRead:
        """
        Retrieves details for a specific user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{user_id}", user_id=user_id),
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
                    user_retrieve_params.UserRetrieveParams,
                ),
            ),
            cast_to=UserRead,
        )

    async def update(
        self,
        user_id: str,
        *,
        args: object,
        kwargs: object,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRead:
        """
        Updates details for a specific user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            path_template("/v1/users/{user_id}", user_id=user_id),
            body=await async_maybe_transform({"name": name}, user_update_params.UserUpdateParams),
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
                    user_update_params.UserUpdateParams,
                ),
            ),
            cast_to=UserRead,
        )

    async def delete(
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
    ) -> None:
        """Deletes a specific user.

        Requires **Admin** authentication.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/users/{user_id}", user_id=user_id),
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
                    user_delete_params.UserDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )

    @cached_property
    def assistants(self) -> AssistantsResourceWithRawResponse:
        return AssistantsResourceWithRawResponse(self._users.assistants)

    @cached_property
    def apikeys(self) -> ApikeysResourceWithRawResponse:
        return ApikeysResourceWithRawResponse(self._users.apikeys)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )

    @cached_property
    def assistants(self) -> AsyncAssistantsResourceWithRawResponse:
        return AsyncAssistantsResourceWithRawResponse(self._users.assistants)

    @cached_property
    def apikeys(self) -> AsyncApikeysResourceWithRawResponse:
        return AsyncApikeysResourceWithRawResponse(self._users.apikeys)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )

    @cached_property
    def assistants(self) -> AssistantsResourceWithStreamingResponse:
        return AssistantsResourceWithStreamingResponse(self._users.assistants)

    @cached_property
    def apikeys(self) -> ApikeysResourceWithStreamingResponse:
        return ApikeysResourceWithStreamingResponse(self._users.apikeys)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )

    @cached_property
    def assistants(self) -> AsyncAssistantsResourceWithStreamingResponse:
        return AsyncAssistantsResourceWithStreamingResponse(self._users.assistants)

    @cached_property
    def apikeys(self) -> AsyncApikeysResourceWithStreamingResponse:
        return AsyncApikeysResourceWithStreamingResponse(self._users.apikeys)
