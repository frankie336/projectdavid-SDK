# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ProjectdavidError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)

if TYPE_CHECKING:
    from .resources import (
        runs,
        admin,
        files,
        users,
        health,
        actions,
        monitor,
        threads,
        uploads,
        messages,
        subscribe,
        assistants,
        completions,
        vector_stores,
    )
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.actions import ActionsResource, AsyncActionsResource
    from .resources.monitor import MonitorResource, AsyncMonitorResource
    from .resources.threads import ThreadsResource, AsyncThreadsResource
    from .resources.uploads import UploadsResource, AsyncUploadsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.runs.runs import RunsResource, AsyncRunsResource
    from .resources.subscribe import SubscribeResource, AsyncSubscribeResource
    from .resources.admin.admin import AdminResource, AsyncAdminResource
    from .resources.completions import CompletionsResource, AsyncCompletionsResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.assistants.assistants import AssistantsResource, AsyncAssistantsResource
    from .resources.vector_stores.vector_stores import VectorStoresResource, AsyncVectorStoresResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Projectdavid",
    "AsyncProjectdavid",
    "Client",
    "AsyncClient",
]


class Projectdavid(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Projectdavid client instance.

        This automatically infers the `api_key` argument from the `PROJECTDAVID_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PROJECTDAVID_API_KEY")
        if api_key is None:
            raise ProjectdavidError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PROJECTDAVID_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PROJECTDAVID_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def monitor(self) -> MonitorResource:
        from .resources.monitor import MonitorResource

        return MonitorResource(self)

    @cached_property
    def subscribe(self) -> SubscribeResource:
        from .resources.subscribe import SubscribeResource

        return SubscribeResource(self)

    @cached_property
    def completions(self) -> CompletionsResource:
        from .resources.completions import CompletionsResource

        return CompletionsResource(self)

    @cached_property
    def threads(self) -> ThreadsResource:
        from .resources.threads import ThreadsResource

        return ThreadsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def runs(self) -> RunsResource:
        from .resources.runs import RunsResource

        return RunsResource(self)

    @cached_property
    def assistants(self) -> AssistantsResource:
        from .resources.assistants import AssistantsResource

        return AssistantsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def actions(self) -> ActionsResource:
        from .resources.actions import ActionsResource

        return ActionsResource(self)

    @cached_property
    def uploads(self) -> UploadsResource:
        from .resources.uploads import UploadsResource

        return UploadsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def vector_stores(self) -> VectorStoresResource:
        from .resources.vector_stores import VectorStoresResource

        return VectorStoresResource(self)

    @cached_property
    def admin(self) -> AdminResource:
        from .resources.admin import AdminResource

        return AdminResource(self)

    @cached_property
    def with_raw_response(self) -> ProjectdavidWithRawResponse:
        return ProjectdavidWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectdavidWithStreamedResponse:
        return ProjectdavidWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def retrieve_root(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Read Root"""
        return self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncProjectdavid(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncProjectdavid client instance.

        This automatically infers the `api_key` argument from the `PROJECTDAVID_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PROJECTDAVID_API_KEY")
        if api_key is None:
            raise ProjectdavidError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PROJECTDAVID_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PROJECTDAVID_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def monitor(self) -> AsyncMonitorResource:
        from .resources.monitor import AsyncMonitorResource

        return AsyncMonitorResource(self)

    @cached_property
    def subscribe(self) -> AsyncSubscribeResource:
        from .resources.subscribe import AsyncSubscribeResource

        return AsyncSubscribeResource(self)

    @cached_property
    def completions(self) -> AsyncCompletionsResource:
        from .resources.completions import AsyncCompletionsResource

        return AsyncCompletionsResource(self)

    @cached_property
    def threads(self) -> AsyncThreadsResource:
        from .resources.threads import AsyncThreadsResource

        return AsyncThreadsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        from .resources.runs import AsyncRunsResource

        return AsyncRunsResource(self)

    @cached_property
    def assistants(self) -> AsyncAssistantsResource:
        from .resources.assistants import AsyncAssistantsResource

        return AsyncAssistantsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def actions(self) -> AsyncActionsResource:
        from .resources.actions import AsyncActionsResource

        return AsyncActionsResource(self)

    @cached_property
    def uploads(self) -> AsyncUploadsResource:
        from .resources.uploads import AsyncUploadsResource

        return AsyncUploadsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def vector_stores(self) -> AsyncVectorStoresResource:
        from .resources.vector_stores import AsyncVectorStoresResource

        return AsyncVectorStoresResource(self)

    @cached_property
    def admin(self) -> AsyncAdminResource:
        from .resources.admin import AsyncAdminResource

        return AsyncAdminResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncProjectdavidWithRawResponse:
        return AsyncProjectdavidWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectdavidWithStreamedResponse:
        return AsyncProjectdavidWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def retrieve_root(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Read Root"""
        return await self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ProjectdavidWithRawResponse:
    _client: Projectdavid

    def __init__(self, client: Projectdavid) -> None:
        self._client = client

        self.retrieve_root = to_raw_response_wrapper(
            client.retrieve_root,
        )

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def monitor(self) -> monitor.MonitorResourceWithRawResponse:
        from .resources.monitor import MonitorResourceWithRawResponse

        return MonitorResourceWithRawResponse(self._client.monitor)

    @cached_property
    def subscribe(self) -> subscribe.SubscribeResourceWithRawResponse:
        from .resources.subscribe import SubscribeResourceWithRawResponse

        return SubscribeResourceWithRawResponse(self._client.subscribe)

    @cached_property
    def completions(self) -> completions.CompletionsResourceWithRawResponse:
        from .resources.completions import CompletionsResourceWithRawResponse

        return CompletionsResourceWithRawResponse(self._client.completions)

    @cached_property
    def threads(self) -> threads.ThreadsResourceWithRawResponse:
        from .resources.threads import ThreadsResourceWithRawResponse

        return ThreadsResourceWithRawResponse(self._client.threads)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def runs(self) -> runs.RunsResourceWithRawResponse:
        from .resources.runs import RunsResourceWithRawResponse

        return RunsResourceWithRawResponse(self._client.runs)

    @cached_property
    def assistants(self) -> assistants.AssistantsResourceWithRawResponse:
        from .resources.assistants import AssistantsResourceWithRawResponse

        return AssistantsResourceWithRawResponse(self._client.assistants)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def actions(self) -> actions.ActionsResourceWithRawResponse:
        from .resources.actions import ActionsResourceWithRawResponse

        return ActionsResourceWithRawResponse(self._client.actions)

    @cached_property
    def uploads(self) -> uploads.UploadsResourceWithRawResponse:
        from .resources.uploads import UploadsResourceWithRawResponse

        return UploadsResourceWithRawResponse(self._client.uploads)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def vector_stores(self) -> vector_stores.VectorStoresResourceWithRawResponse:
        from .resources.vector_stores import VectorStoresResourceWithRawResponse

        return VectorStoresResourceWithRawResponse(self._client.vector_stores)

    @cached_property
    def admin(self) -> admin.AdminResourceWithRawResponse:
        from .resources.admin import AdminResourceWithRawResponse

        return AdminResourceWithRawResponse(self._client.admin)


class AsyncProjectdavidWithRawResponse:
    _client: AsyncProjectdavid

    def __init__(self, client: AsyncProjectdavid) -> None:
        self._client = client

        self.retrieve_root = async_to_raw_response_wrapper(
            client.retrieve_root,
        )

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def monitor(self) -> monitor.AsyncMonitorResourceWithRawResponse:
        from .resources.monitor import AsyncMonitorResourceWithRawResponse

        return AsyncMonitorResourceWithRawResponse(self._client.monitor)

    @cached_property
    def subscribe(self) -> subscribe.AsyncSubscribeResourceWithRawResponse:
        from .resources.subscribe import AsyncSubscribeResourceWithRawResponse

        return AsyncSubscribeResourceWithRawResponse(self._client.subscribe)

    @cached_property
    def completions(self) -> completions.AsyncCompletionsResourceWithRawResponse:
        from .resources.completions import AsyncCompletionsResourceWithRawResponse

        return AsyncCompletionsResourceWithRawResponse(self._client.completions)

    @cached_property
    def threads(self) -> threads.AsyncThreadsResourceWithRawResponse:
        from .resources.threads import AsyncThreadsResourceWithRawResponse

        return AsyncThreadsResourceWithRawResponse(self._client.threads)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def runs(self) -> runs.AsyncRunsResourceWithRawResponse:
        from .resources.runs import AsyncRunsResourceWithRawResponse

        return AsyncRunsResourceWithRawResponse(self._client.runs)

    @cached_property
    def assistants(self) -> assistants.AsyncAssistantsResourceWithRawResponse:
        from .resources.assistants import AsyncAssistantsResourceWithRawResponse

        return AsyncAssistantsResourceWithRawResponse(self._client.assistants)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def actions(self) -> actions.AsyncActionsResourceWithRawResponse:
        from .resources.actions import AsyncActionsResourceWithRawResponse

        return AsyncActionsResourceWithRawResponse(self._client.actions)

    @cached_property
    def uploads(self) -> uploads.AsyncUploadsResourceWithRawResponse:
        from .resources.uploads import AsyncUploadsResourceWithRawResponse

        return AsyncUploadsResourceWithRawResponse(self._client.uploads)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def vector_stores(self) -> vector_stores.AsyncVectorStoresResourceWithRawResponse:
        from .resources.vector_stores import AsyncVectorStoresResourceWithRawResponse

        return AsyncVectorStoresResourceWithRawResponse(self._client.vector_stores)

    @cached_property
    def admin(self) -> admin.AsyncAdminResourceWithRawResponse:
        from .resources.admin import AsyncAdminResourceWithRawResponse

        return AsyncAdminResourceWithRawResponse(self._client.admin)


class ProjectdavidWithStreamedResponse:
    _client: Projectdavid

    def __init__(self, client: Projectdavid) -> None:
        self._client = client

        self.retrieve_root = to_streamed_response_wrapper(
            client.retrieve_root,
        )

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def monitor(self) -> monitor.MonitorResourceWithStreamingResponse:
        from .resources.monitor import MonitorResourceWithStreamingResponse

        return MonitorResourceWithStreamingResponse(self._client.monitor)

    @cached_property
    def subscribe(self) -> subscribe.SubscribeResourceWithStreamingResponse:
        from .resources.subscribe import SubscribeResourceWithStreamingResponse

        return SubscribeResourceWithStreamingResponse(self._client.subscribe)

    @cached_property
    def completions(self) -> completions.CompletionsResourceWithStreamingResponse:
        from .resources.completions import CompletionsResourceWithStreamingResponse

        return CompletionsResourceWithStreamingResponse(self._client.completions)

    @cached_property
    def threads(self) -> threads.ThreadsResourceWithStreamingResponse:
        from .resources.threads import ThreadsResourceWithStreamingResponse

        return ThreadsResourceWithStreamingResponse(self._client.threads)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def runs(self) -> runs.RunsResourceWithStreamingResponse:
        from .resources.runs import RunsResourceWithStreamingResponse

        return RunsResourceWithStreamingResponse(self._client.runs)

    @cached_property
    def assistants(self) -> assistants.AssistantsResourceWithStreamingResponse:
        from .resources.assistants import AssistantsResourceWithStreamingResponse

        return AssistantsResourceWithStreamingResponse(self._client.assistants)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def actions(self) -> actions.ActionsResourceWithStreamingResponse:
        from .resources.actions import ActionsResourceWithStreamingResponse

        return ActionsResourceWithStreamingResponse(self._client.actions)

    @cached_property
    def uploads(self) -> uploads.UploadsResourceWithStreamingResponse:
        from .resources.uploads import UploadsResourceWithStreamingResponse

        return UploadsResourceWithStreamingResponse(self._client.uploads)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def vector_stores(self) -> vector_stores.VectorStoresResourceWithStreamingResponse:
        from .resources.vector_stores import VectorStoresResourceWithStreamingResponse

        return VectorStoresResourceWithStreamingResponse(self._client.vector_stores)

    @cached_property
    def admin(self) -> admin.AdminResourceWithStreamingResponse:
        from .resources.admin import AdminResourceWithStreamingResponse

        return AdminResourceWithStreamingResponse(self._client.admin)


class AsyncProjectdavidWithStreamedResponse:
    _client: AsyncProjectdavid

    def __init__(self, client: AsyncProjectdavid) -> None:
        self._client = client

        self.retrieve_root = async_to_streamed_response_wrapper(
            client.retrieve_root,
        )

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def monitor(self) -> monitor.AsyncMonitorResourceWithStreamingResponse:
        from .resources.monitor import AsyncMonitorResourceWithStreamingResponse

        return AsyncMonitorResourceWithStreamingResponse(self._client.monitor)

    @cached_property
    def subscribe(self) -> subscribe.AsyncSubscribeResourceWithStreamingResponse:
        from .resources.subscribe import AsyncSubscribeResourceWithStreamingResponse

        return AsyncSubscribeResourceWithStreamingResponse(self._client.subscribe)

    @cached_property
    def completions(self) -> completions.AsyncCompletionsResourceWithStreamingResponse:
        from .resources.completions import AsyncCompletionsResourceWithStreamingResponse

        return AsyncCompletionsResourceWithStreamingResponse(self._client.completions)

    @cached_property
    def threads(self) -> threads.AsyncThreadsResourceWithStreamingResponse:
        from .resources.threads import AsyncThreadsResourceWithStreamingResponse

        return AsyncThreadsResourceWithStreamingResponse(self._client.threads)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def runs(self) -> runs.AsyncRunsResourceWithStreamingResponse:
        from .resources.runs import AsyncRunsResourceWithStreamingResponse

        return AsyncRunsResourceWithStreamingResponse(self._client.runs)

    @cached_property
    def assistants(self) -> assistants.AsyncAssistantsResourceWithStreamingResponse:
        from .resources.assistants import AsyncAssistantsResourceWithStreamingResponse

        return AsyncAssistantsResourceWithStreamingResponse(self._client.assistants)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def actions(self) -> actions.AsyncActionsResourceWithStreamingResponse:
        from .resources.actions import AsyncActionsResourceWithStreamingResponse

        return AsyncActionsResourceWithStreamingResponse(self._client.actions)

    @cached_property
    def uploads(self) -> uploads.AsyncUploadsResourceWithStreamingResponse:
        from .resources.uploads import AsyncUploadsResourceWithStreamingResponse

        return AsyncUploadsResourceWithStreamingResponse(self._client.uploads)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def vector_stores(self) -> vector_stores.AsyncVectorStoresResourceWithStreamingResponse:
        from .resources.vector_stores import AsyncVectorStoresResourceWithStreamingResponse

        return AsyncVectorStoresResourceWithStreamingResponse(self._client.vector_stores)

    @cached_property
    def admin(self) -> admin.AsyncAdminResourceWithStreamingResponse:
        from .resources.admin import AsyncAdminResourceWithStreamingResponse

        return AsyncAdminResourceWithStreamingResponse(self._client.admin)


Client = Projectdavid

AsyncClient = AsyncProjectdavid
