# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types.vector_stores import AdminListByUserResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_by_user(self, client: Projectdavid) -> None:
        admin = client.vector_stores.admin.list_by_user(
            args={},
            kwargs={},
            owner_id="owner_id",
        )
        assert_matches_type(AdminListByUserResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_by_user(self, client: Projectdavid) -> None:
        response = client.vector_stores.admin.with_raw_response.list_by_user(
            args={},
            kwargs={},
            owner_id="owner_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminListByUserResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_by_user(self, client: Projectdavid) -> None:
        with client.vector_stores.admin.with_streaming_response.list_by_user(
            args={},
            kwargs={},
            owner_id="owner_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminListByUserResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_by_user(self, async_client: AsyncProjectdavid) -> None:
        admin = await async_client.vector_stores.admin.list_by_user(
            args={},
            kwargs={},
            owner_id="owner_id",
        )
        assert_matches_type(AdminListByUserResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_by_user(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.vector_stores.admin.with_raw_response.list_by_user(
            args={},
            kwargs={},
            owner_id="owner_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminListByUserResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_user(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.vector_stores.admin.with_streaming_response.list_by_user(
            args={},
            kwargs={},
            owner_id="owner_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminListByUserResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True
