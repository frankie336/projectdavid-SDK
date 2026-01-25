# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types.users import (
    APIKeyDetails,
    ApikeyListResponse,
    APIKeyCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApikeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Projectdavid) -> None:
        apikey = client.users.apikeys.create(
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert_matches_type(APIKeyCreateResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Projectdavid) -> None:
        apikey = client.users.apikeys.create(
            user_id="user_id",
            args={},
            kwargs={},
            expires_in_days=1,
            key_name="key_name",
        )
        assert_matches_type(APIKeyCreateResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Projectdavid) -> None:
        response = client.users.apikeys.with_raw_response.create(
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = response.parse()
        assert_matches_type(APIKeyCreateResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Projectdavid) -> None:
        with client.users.apikeys.with_streaming_response.create(
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = response.parse()
            assert_matches_type(APIKeyCreateResponse, apikey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.apikeys.with_raw_response.create(
                user_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Projectdavid) -> None:
        apikey = client.users.apikeys.retrieve(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert_matches_type(APIKeyDetails, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Projectdavid) -> None:
        response = client.users.apikeys.with_raw_response.retrieve(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = response.parse()
        assert_matches_type(APIKeyDetails, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Projectdavid) -> None:
        with client.users.apikeys.with_streaming_response.retrieve(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = response.parse()
            assert_matches_type(APIKeyDetails, apikey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.apikeys.with_raw_response.retrieve(
                key_prefix="key_prefix",
                user_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_prefix` but received ''"):
            client.users.apikeys.with_raw_response.retrieve(
                key_prefix="",
                user_id="user_id",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Projectdavid) -> None:
        apikey = client.users.apikeys.list(
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert_matches_type(ApikeyListResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Projectdavid) -> None:
        apikey = client.users.apikeys.list(
            user_id="user_id",
            args={},
            kwargs={},
            include_inactive=True,
        )
        assert_matches_type(ApikeyListResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Projectdavid) -> None:
        response = client.users.apikeys.with_raw_response.list(
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = response.parse()
        assert_matches_type(ApikeyListResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Projectdavid) -> None:
        with client.users.apikeys.with_streaming_response.list(
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = response.parse()
            assert_matches_type(ApikeyListResponse, apikey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.apikeys.with_raw_response.list(
                user_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revoke(self, client: Projectdavid) -> None:
        apikey = client.users.apikeys.revoke(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert apikey is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Projectdavid) -> None:
        response = client.users.apikeys.with_raw_response.revoke(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = response.parse()
        assert apikey is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Projectdavid) -> None:
        with client.users.apikeys.with_streaming_response.revoke(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = response.parse()
            assert apikey is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_revoke(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.apikeys.with_raw_response.revoke(
                key_prefix="key_prefix",
                user_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_prefix` but received ''"):
            client.users.apikeys.with_raw_response.revoke(
                key_prefix="",
                user_id="user_id",
                args={},
                kwargs={},
            )


class TestAsyncApikeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncProjectdavid) -> None:
        apikey = await async_client.users.apikeys.create(
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert_matches_type(APIKeyCreateResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        apikey = await async_client.users.apikeys.create(
            user_id="user_id",
            args={},
            kwargs={},
            expires_in_days=1,
            key_name="key_name",
        )
        assert_matches_type(APIKeyCreateResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.users.apikeys.with_raw_response.create(
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = await response.parse()
        assert_matches_type(APIKeyCreateResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.users.apikeys.with_streaming_response.create(
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = await response.parse()
            assert_matches_type(APIKeyCreateResponse, apikey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.apikeys.with_raw_response.create(
                user_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncProjectdavid) -> None:
        apikey = await async_client.users.apikeys.retrieve(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert_matches_type(APIKeyDetails, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.users.apikeys.with_raw_response.retrieve(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = await response.parse()
        assert_matches_type(APIKeyDetails, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.users.apikeys.with_streaming_response.retrieve(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = await response.parse()
            assert_matches_type(APIKeyDetails, apikey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.apikeys.with_raw_response.retrieve(
                key_prefix="key_prefix",
                user_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_prefix` but received ''"):
            await async_client.users.apikeys.with_raw_response.retrieve(
                key_prefix="",
                user_id="user_id",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncProjectdavid) -> None:
        apikey = await async_client.users.apikeys.list(
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert_matches_type(ApikeyListResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        apikey = await async_client.users.apikeys.list(
            user_id="user_id",
            args={},
            kwargs={},
            include_inactive=True,
        )
        assert_matches_type(ApikeyListResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.users.apikeys.with_raw_response.list(
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = await response.parse()
        assert_matches_type(ApikeyListResponse, apikey, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.users.apikeys.with_streaming_response.list(
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = await response.parse()
            assert_matches_type(ApikeyListResponse, apikey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.apikeys.with_raw_response.list(
                user_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncProjectdavid) -> None:
        apikey = await async_client.users.apikeys.revoke(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert apikey is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.users.apikeys.with_raw_response.revoke(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        apikey = await response.parse()
        assert apikey is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.users.apikeys.with_streaming_response.revoke(
            key_prefix="key_prefix",
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            apikey = await response.parse()
            assert apikey is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.apikeys.with_raw_response.revoke(
                key_prefix="key_prefix",
                user_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_prefix` but received ''"):
            await async_client.users.apikeys.with_raw_response.revoke(
                key_prefix="",
                user_id="user_id",
                args={},
                kwargs={},
            )
