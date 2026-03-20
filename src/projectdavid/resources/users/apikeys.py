# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

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
from ...types.users import apikey_list_params, apikey_create_params, apikey_revoke_params, apikey_retrieve_params
from ..._base_client import make_request_options
from ...types.users.api_key_details import APIKeyDetails
from ...types.users.apikey_list_response import ApikeyListResponse
from ...types.users.api_key_create_response import APIKeyCreateResponse

__all__ = ["ApikeysResource", "AsyncApikeysResource"]


class ApikeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ApikeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return ApikeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApikeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return ApikeysResourceWithStreamingResponse(self)

    def create(
        self,
        user_id: str,
        *,
        args: object,
        kwargs: object,
        expires_in_days: Optional[int] | Omit = omit,
        key_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyCreateResponse:
        """Generates a new API key for the specified user.

        The plain key is returned only
        once.

        Args:
          expires_in_days: Optional number of days from now until the key automatically expires. Minimum
              value is 1.

          key_name: An optional user-friendly name for the key (e.g., 'My Production Key').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/apikeys", user_id=user_id),
            body=maybe_transform(
                {
                    "expires_in_days": expires_in_days,
                    "key_name": key_name,
                },
                apikey_create_params.ApikeyCreateParams,
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
                    apikey_create_params.ApikeyCreateParams,
                ),
            ),
            cast_to=APIKeyCreateResponse,
        )

    def retrieve(
        self,
        key_prefix: str,
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
    ) -> APIKeyDetails:
        """
        Retrieves details for a specific API key using its prefix.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not key_prefix:
            raise ValueError(f"Expected a non-empty value for `key_prefix` but received {key_prefix!r}")
        return self._get(
            path_template("/v1/users/{user_id}/apikeys/{key_prefix}", user_id=user_id, key_prefix=key_prefix),
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
                    apikey_retrieve_params.ApikeyRetrieveParams,
                ),
            ),
            cast_to=APIKeyDetails,
        )

    def list(
        self,
        user_id: str,
        *,
        args: object,
        kwargs: object,
        include_inactive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApikeyListResponse:
        """
        Retrieves a list of API keys for the specified user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{user_id}/apikeys", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "include_inactive": include_inactive,
                    },
                    apikey_list_params.ApikeyListParams,
                ),
            ),
            cast_to=ApikeyListResponse,
        )

    def revoke(
        self,
        key_prefix: str,
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
        Revokes (deactivates) a specific API key using its prefix.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not key_prefix:
            raise ValueError(f"Expected a non-empty value for `key_prefix` but received {key_prefix!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/users/{user_id}/apikeys/{key_prefix}", user_id=user_id, key_prefix=key_prefix),
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
                    apikey_revoke_params.ApikeyRevokeParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncApikeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncApikeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncApikeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApikeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/frankie336/projectdavid-SDK#with_streaming_response
        """
        return AsyncApikeysResourceWithStreamingResponse(self)

    async def create(
        self,
        user_id: str,
        *,
        args: object,
        kwargs: object,
        expires_in_days: Optional[int] | Omit = omit,
        key_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyCreateResponse:
        """Generates a new API key for the specified user.

        The plain key is returned only
        once.

        Args:
          expires_in_days: Optional number of days from now until the key automatically expires. Minimum
              value is 1.

          key_name: An optional user-friendly name for the key (e.g., 'My Production Key').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/apikeys", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "expires_in_days": expires_in_days,
                    "key_name": key_name,
                },
                apikey_create_params.ApikeyCreateParams,
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
                    apikey_create_params.ApikeyCreateParams,
                ),
            ),
            cast_to=APIKeyCreateResponse,
        )

    async def retrieve(
        self,
        key_prefix: str,
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
    ) -> APIKeyDetails:
        """
        Retrieves details for a specific API key using its prefix.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not key_prefix:
            raise ValueError(f"Expected a non-empty value for `key_prefix` but received {key_prefix!r}")
        return await self._get(
            path_template("/v1/users/{user_id}/apikeys/{key_prefix}", user_id=user_id, key_prefix=key_prefix),
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
                    apikey_retrieve_params.ApikeyRetrieveParams,
                ),
            ),
            cast_to=APIKeyDetails,
        )

    async def list(
        self,
        user_id: str,
        *,
        args: object,
        kwargs: object,
        include_inactive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApikeyListResponse:
        """
        Retrieves a list of API keys for the specified user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{user_id}/apikeys", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "include_inactive": include_inactive,
                    },
                    apikey_list_params.ApikeyListParams,
                ),
            ),
            cast_to=ApikeyListResponse,
        )

    async def revoke(
        self,
        key_prefix: str,
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
        Revokes (deactivates) a specific API key using its prefix.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not key_prefix:
            raise ValueError(f"Expected a non-empty value for `key_prefix` but received {key_prefix!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/users/{user_id}/apikeys/{key_prefix}", user_id=user_id, key_prefix=key_prefix),
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
                    apikey_revoke_params.ApikeyRevokeParams,
                ),
            ),
            cast_to=NoneType,
        )


class ApikeysResourceWithRawResponse:
    def __init__(self, apikeys: ApikeysResource) -> None:
        self._apikeys = apikeys

        self.create = to_raw_response_wrapper(
            apikeys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            apikeys.retrieve,
        )
        self.list = to_raw_response_wrapper(
            apikeys.list,
        )
        self.revoke = to_raw_response_wrapper(
            apikeys.revoke,
        )


class AsyncApikeysResourceWithRawResponse:
    def __init__(self, apikeys: AsyncApikeysResource) -> None:
        self._apikeys = apikeys

        self.create = async_to_raw_response_wrapper(
            apikeys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            apikeys.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            apikeys.list,
        )
        self.revoke = async_to_raw_response_wrapper(
            apikeys.revoke,
        )


class ApikeysResourceWithStreamingResponse:
    def __init__(self, apikeys: ApikeysResource) -> None:
        self._apikeys = apikeys

        self.create = to_streamed_response_wrapper(
            apikeys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            apikeys.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            apikeys.list,
        )
        self.revoke = to_streamed_response_wrapper(
            apikeys.revoke,
        )


class AsyncApikeysResourceWithStreamingResponse:
    def __init__(self, apikeys: AsyncApikeysResource) -> None:
        self._apikeys = apikeys

        self.create = async_to_streamed_response_wrapper(
            apikeys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            apikeys.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            apikeys.list,
        )
        self.revoke = async_to_streamed_response_wrapper(
            apikeys.revoke,
        )
