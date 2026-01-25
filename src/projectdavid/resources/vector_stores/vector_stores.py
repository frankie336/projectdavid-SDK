# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .admin import (
    AdminResource,
    AsyncAdminResource,
    AdminResourceWithRawResponse,
    AsyncAdminResourceWithRawResponse,
    AdminResourceWithStreamingResponse,
    AsyncAdminResourceWithStreamingResponse,
)
from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .lookup import (
    LookupResource,
    AsyncLookupResource,
    LookupResourceWithRawResponse,
    AsyncLookupResourceWithRawResponse,
    LookupResourceWithStreamingResponse,
    AsyncLookupResourceWithStreamingResponse,
)
from ...types import (
    vector_store_list_params,
    vector_store_create_params,
    vector_store_delete_params,
    vector_store_retrieve_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.vector_store_list_response import VectorStoreListResponse

__all__ = ["VectorStoresResource", "AsyncVectorStoresResource"]


class VectorStoresResource(SyncAPIResource):
    @cached_property
    def admin(self) -> AdminResource:
        return AdminResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def lookup(self) -> LookupResource:
        return LookupResource(self._client)

    @cached_property
    def with_raw_response(self) -> VectorStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#accessing-raw-response-data-eg-headers
        """
        return VectorStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#with_streaming_response
        """
        return VectorStoresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        args: object,
        kwargs: object,
        distance_metric: str,
        name: str,
        shared_id: str,
        vector_size: int,
        owner_id: Optional[str] | Omit = omit,
        config: Optional[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStore:
        """
        Creates a new vector-store.

        - **Regular callers** → the store is assigned to _their_ user-id.
        - **Admins** → may pass the optional `owner_id` query-param to create the store
          for a different user.

        Args:
          distance_metric: Distance metric (COSINE, EUCLID, DOT)

          name: Human-friendly store name

          shared_id: Pre-generated unique ID (also used as collection name).

          vector_size: Dimensionality of the vectors

          owner_id: Target user-id (admin-only). If omitted, the store is created for the caller.

          config: Additional configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vector-stores",
            body=maybe_transform(
                {
                    "distance_metric": distance_metric,
                    "name": name,
                    "shared_id": shared_id,
                    "vector_size": vector_size,
                    "config": config,
                },
                vector_store_create_params.VectorStoreCreateParams,
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
                        "owner_id": owner_id,
                    },
                    vector_store_create_params.VectorStoreCreateParams,
                ),
            ),
            cast_to=VectorStore,
        )

    def retrieve(
        self,
        vector_store_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStore:
        """
        Get Vector Store

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._get(
            f"/v1/vector-stores/{vector_store_id}",
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
                    vector_store_retrieve_params.VectorStoreRetrieveParams,
                ),
            ),
            cast_to=VectorStore,
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
    ) -> VectorStoreListResponse:
        """
        List current user's Vector Stores

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/vector-stores",
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
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            cast_to=VectorStoreListResponse,
        )

    def delete(
        self,
        vector_store_id: str,
        *,
        args: object,
        kwargs: object,
        permanent: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Vector Store

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/vector-stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "permanent": permanent,
                    },
                    vector_store_delete_params.VectorStoreDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncVectorStoresResource(AsyncAPIResource):
    @cached_property
    def admin(self) -> AsyncAdminResource:
        return AsyncAdminResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def lookup(self) -> AsyncLookupResource:
        return AsyncLookupResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVectorStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/projectdavid-python#with_streaming_response
        """
        return AsyncVectorStoresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        args: object,
        kwargs: object,
        distance_metric: str,
        name: str,
        shared_id: str,
        vector_size: int,
        owner_id: Optional[str] | Omit = omit,
        config: Optional[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStore:
        """
        Creates a new vector-store.

        - **Regular callers** → the store is assigned to _their_ user-id.
        - **Admins** → may pass the optional `owner_id` query-param to create the store
          for a different user.

        Args:
          distance_metric: Distance metric (COSINE, EUCLID, DOT)

          name: Human-friendly store name

          shared_id: Pre-generated unique ID (also used as collection name).

          vector_size: Dimensionality of the vectors

          owner_id: Target user-id (admin-only). If omitted, the store is created for the caller.

          config: Additional configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vector-stores",
            body=await async_maybe_transform(
                {
                    "distance_metric": distance_metric,
                    "name": name,
                    "shared_id": shared_id,
                    "vector_size": vector_size,
                    "config": config,
                },
                vector_store_create_params.VectorStoreCreateParams,
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
                        "owner_id": owner_id,
                    },
                    vector_store_create_params.VectorStoreCreateParams,
                ),
            ),
            cast_to=VectorStore,
        )

    async def retrieve(
        self,
        vector_store_id: str,
        *,
        args: object,
        kwargs: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStore:
        """
        Get Vector Store

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._get(
            f"/v1/vector-stores/{vector_store_id}",
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
                    vector_store_retrieve_params.VectorStoreRetrieveParams,
                ),
            ),
            cast_to=VectorStore,
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
    ) -> VectorStoreListResponse:
        """
        List current user's Vector Stores

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/vector-stores",
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
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            cast_to=VectorStoreListResponse,
        )

    async def delete(
        self,
        vector_store_id: str,
        *,
        args: object,
        kwargs: object,
        permanent: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Vector Store

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/vector-stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "args": args,
                        "kwargs": kwargs,
                        "permanent": permanent,
                    },
                    vector_store_delete_params.VectorStoreDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class VectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = to_raw_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = to_raw_response_wrapper(
            vector_stores.retrieve,
        )
        self.list = to_raw_response_wrapper(
            vector_stores.list,
        )
        self.delete = to_raw_response_wrapper(
            vector_stores.delete,
        )

    @cached_property
    def admin(self) -> AdminResourceWithRawResponse:
        return AdminResourceWithRawResponse(self._vector_stores.admin)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._vector_stores.files)

    @cached_property
    def lookup(self) -> LookupResourceWithRawResponse:
        return LookupResourceWithRawResponse(self._vector_stores.lookup)


class AsyncVectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = async_to_raw_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            vector_stores.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            vector_stores.list,
        )
        self.delete = async_to_raw_response_wrapper(
            vector_stores.delete,
        )

    @cached_property
    def admin(self) -> AsyncAdminResourceWithRawResponse:
        return AsyncAdminResourceWithRawResponse(self._vector_stores.admin)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._vector_stores.files)

    @cached_property
    def lookup(self) -> AsyncLookupResourceWithRawResponse:
        return AsyncLookupResourceWithRawResponse(self._vector_stores.lookup)


class VectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = to_streamed_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            vector_stores.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            vector_stores.list,
        )
        self.delete = to_streamed_response_wrapper(
            vector_stores.delete,
        )

    @cached_property
    def admin(self) -> AdminResourceWithStreamingResponse:
        return AdminResourceWithStreamingResponse(self._vector_stores.admin)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._vector_stores.files)

    @cached_property
    def lookup(self) -> LookupResourceWithStreamingResponse:
        return LookupResourceWithStreamingResponse(self._vector_stores.lookup)


class AsyncVectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = async_to_streamed_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            vector_stores.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            vector_stores.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            vector_stores.delete,
        )

    @cached_property
    def admin(self) -> AsyncAdminResourceWithStreamingResponse:
        return AsyncAdminResourceWithStreamingResponse(self._vector_stores.admin)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._vector_stores.files)

    @cached_property
    def lookup(self) -> AsyncLookupResourceWithStreamingResponse:
        return AsyncLookupResourceWithStreamingResponse(self._vector_stores.lookup)
