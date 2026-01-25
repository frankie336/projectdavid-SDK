# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types import VectorStore

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLookup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_by_collection_name(self, client: Projectdavid) -> None:
        lookup = client.vector_stores.lookup.by_collection_name(
            args={},
            kwargs={},
            name="name",
        )
        assert_matches_type(VectorStore, lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_by_collection_name(self, client: Projectdavid) -> None:
        response = client.vector_stores.lookup.with_raw_response.by_collection_name(
            args={},
            kwargs={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lookup = response.parse()
        assert_matches_type(VectorStore, lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_by_collection_name(self, client: Projectdavid) -> None:
        with client.vector_stores.lookup.with_streaming_response.by_collection_name(
            args={},
            kwargs={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lookup = response.parse()
            assert_matches_type(VectorStore, lookup, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLookup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_by_collection_name(self, async_client: AsyncProjectdavid) -> None:
        lookup = await async_client.vector_stores.lookup.by_collection_name(
            args={},
            kwargs={},
            name="name",
        )
        assert_matches_type(VectorStore, lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_by_collection_name(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.vector_stores.lookup.with_raw_response.by_collection_name(
            args={},
            kwargs={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lookup = await response.parse()
        assert_matches_type(VectorStore, lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_by_collection_name(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.vector_stores.lookup.with_streaming_response.by_collection_name(
            args={},
            kwargs={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lookup = await response.parse()
            assert_matches_type(VectorStore, lookup, path=["response"])

        assert cast(Any, response.is_closed) is True
