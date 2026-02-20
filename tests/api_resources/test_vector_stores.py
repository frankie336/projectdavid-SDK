# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types import (
    VectorStore,
    VectorStoreListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVectorStores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Projectdavid) -> None:
        vector_store = client.vector_stores.create(
            args={},
            kwargs={},
            distance_metric="distance_metric",
            name="xxx",
            shared_id="shared_id",
            vector_size=1,
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Projectdavid) -> None:
        vector_store = client.vector_stores.create(
            args={},
            kwargs={},
            distance_metric="distance_metric",
            name="xxx",
            shared_id="shared_id",
            vector_size=1,
            owner_id="owner_id",
            config={},
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Projectdavid) -> None:
        response = client.vector_stores.with_raw_response.create(
            args={},
            kwargs={},
            distance_metric="distance_metric",
            name="xxx",
            shared_id="shared_id",
            vector_size=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Projectdavid) -> None:
        with client.vector_stores.with_streaming_response.create(
            args={},
            kwargs={},
            distance_metric="distance_metric",
            name="xxx",
            shared_id="shared_id",
            vector_size=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Projectdavid) -> None:
        vector_store = client.vector_stores.retrieve(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Projectdavid) -> None:
        response = client.vector_stores.with_raw_response.retrieve(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Projectdavid) -> None:
        with client.vector_stores.with_streaming_response.retrieve(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.with_raw_response.retrieve(
                vector_store_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Projectdavid) -> None:
        vector_store = client.vector_stores.list(
            args={},
            kwargs={},
        )
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Projectdavid) -> None:
        response = client.vector_stores.with_raw_response.list(
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Projectdavid) -> None:
        with client.vector_stores.with_streaming_response.list(
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Projectdavid) -> None:
        vector_store = client.vector_stores.delete(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )
        assert vector_store is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Projectdavid) -> None:
        vector_store = client.vector_stores.delete(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            permanent=True,
        )
        assert vector_store is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Projectdavid) -> None:
        response = client.vector_stores.with_raw_response.delete(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert vector_store is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Projectdavid) -> None:
        with client.vector_stores.with_streaming_response.delete(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert vector_store is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.with_raw_response.delete(
                vector_store_id="",
                args={},
                kwargs={},
            )


class TestAsyncVectorStores:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncProjectdavid) -> None:
        vector_store = await async_client.vector_stores.create(
            args={},
            kwargs={},
            distance_metric="distance_metric",
            name="xxx",
            shared_id="shared_id",
            vector_size=1,
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        vector_store = await async_client.vector_stores.create(
            args={},
            kwargs={},
            distance_metric="distance_metric",
            name="xxx",
            shared_id="shared_id",
            vector_size=1,
            owner_id="owner_id",
            config={},
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.vector_stores.with_raw_response.create(
            args={},
            kwargs={},
            distance_metric="distance_metric",
            name="xxx",
            shared_id="shared_id",
            vector_size=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.vector_stores.with_streaming_response.create(
            args={},
            kwargs={},
            distance_metric="distance_metric",
            name="xxx",
            shared_id="shared_id",
            vector_size=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncProjectdavid) -> None:
        vector_store = await async_client.vector_stores.retrieve(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.vector_stores.with_raw_response.retrieve(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.vector_stores.with_streaming_response.retrieve(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.with_raw_response.retrieve(
                vector_store_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncProjectdavid) -> None:
        vector_store = await async_client.vector_stores.list(
            args={},
            kwargs={},
        )
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.vector_stores.with_raw_response.list(
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.vector_stores.with_streaming_response.list(
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncProjectdavid) -> None:
        vector_store = await async_client.vector_stores.delete(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )
        assert vector_store is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        vector_store = await async_client.vector_stores.delete(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            permanent=True,
        )
        assert vector_store is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.vector_stores.with_raw_response.delete(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert vector_store is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.vector_stores.with_streaming_response.delete(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert vector_store is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.with_raw_response.delete(
                vector_store_id="",
                args={},
                kwargs={},
            )
