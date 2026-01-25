# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types.users import APIKeyCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_api_key(self, client: Projectdavid) -> None:
        user = client.admin.users.create_api_key(
            target_user_id="target_user_id",
            args={},
            kwargs={},
        )
        assert_matches_type(APIKeyCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_api_key_with_all_params(self, client: Projectdavid) -> None:
        user = client.admin.users.create_api_key(
            target_user_id="target_user_id",
            args={},
            kwargs={},
            expires_in_days=1,
            key_name="key_name",
        )
        assert_matches_type(APIKeyCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_api_key(self, client: Projectdavid) -> None:
        response = client.admin.users.with_raw_response.create_api_key(
            target_user_id="target_user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(APIKeyCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_api_key(self, client: Projectdavid) -> None:
        with client.admin.users.with_streaming_response.create_api_key(
            target_user_id="target_user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(APIKeyCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_api_key(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_user_id` but received ''"):
            client.admin.users.with_raw_response.create_api_key(
                target_user_id="",
                args={},
                kwargs={},
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_api_key(self, async_client: AsyncProjectdavid) -> None:
        user = await async_client.admin.users.create_api_key(
            target_user_id="target_user_id",
            args={},
            kwargs={},
        )
        assert_matches_type(APIKeyCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_api_key_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        user = await async_client.admin.users.create_api_key(
            target_user_id="target_user_id",
            args={},
            kwargs={},
            expires_in_days=1,
            key_name="key_name",
        )
        assert_matches_type(APIKeyCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_api_key(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.admin.users.with_raw_response.create_api_key(
            target_user_id="target_user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(APIKeyCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_api_key(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.admin.users.with_streaming_response.create_api_key(
            target_user_id="target_user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(APIKeyCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_api_key(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_user_id` but received ''"):
            await async_client.admin.users.with_raw_response.create_api_key(
                target_user_id="",
                args={},
                kwargs={},
            )
