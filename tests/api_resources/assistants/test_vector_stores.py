# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types.assistants import (
    VectorStoreListResponse,
    VectorStoreAttachResponse,
    VectorStoreDetachResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVectorStores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Projectdavid) -> None:
        vector_store = client.assistants.vector_stores.list(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Projectdavid) -> None:
        response = client.assistants.vector_stores.with_raw_response.list(
            assistant_id="assistant_id",
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
        with client.assistants.vector_stores.with_streaming_response.list(
            assistant_id="assistant_id",
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
    def test_path_params_list(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.assistants.vector_stores.with_raw_response.list(
                assistant_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_attach(self, client: Projectdavid) -> None:
        vector_store = client.assistants.vector_stores.attach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )
        assert_matches_type(VectorStoreAttachResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: Projectdavid) -> None:
        response = client.assistants.vector_stores.with_raw_response.attach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStoreAttachResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_attach(self, client: Projectdavid) -> None:
        with client.assistants.vector_stores.with_streaming_response.attach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStoreAttachResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_attach(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.assistants.vector_stores.with_raw_response.attach(
                vector_store_id="vector_store_id",
                assistant_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.assistants.vector_stores.with_raw_response.attach(
                vector_store_id="",
                assistant_id="assistant_id",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_detach(self, client: Projectdavid) -> None:
        vector_store = client.assistants.vector_stores.detach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )
        assert_matches_type(VectorStoreDetachResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: Projectdavid) -> None:
        response = client.assistants.vector_stores.with_raw_response.detach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStoreDetachResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_detach(self, client: Projectdavid) -> None:
        with client.assistants.vector_stores.with_streaming_response.detach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStoreDetachResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_detach(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.assistants.vector_stores.with_raw_response.detach(
                vector_store_id="vector_store_id",
                assistant_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.assistants.vector_stores.with_raw_response.detach(
                vector_store_id="",
                assistant_id="assistant_id",
                args={},
                kwargs={},
            )


class TestAsyncVectorStores:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncProjectdavid) -> None:
        vector_store = await async_client.assistants.vector_stores.list(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.assistants.vector_stores.with_raw_response.list(
            assistant_id="assistant_id",
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
        async with async_client.assistants.vector_stores.with_streaming_response.list(
            assistant_id="assistant_id",
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
    async def test_path_params_list(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.assistants.vector_stores.with_raw_response.list(
                assistant_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncProjectdavid) -> None:
        vector_store = await async_client.assistants.vector_stores.attach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )
        assert_matches_type(VectorStoreAttachResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.assistants.vector_stores.with_raw_response.attach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStoreAttachResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.assistants.vector_stores.with_streaming_response.attach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStoreAttachResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.assistants.vector_stores.with_raw_response.attach(
                vector_store_id="vector_store_id",
                assistant_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.assistants.vector_stores.with_raw_response.attach(
                vector_store_id="",
                assistant_id="assistant_id",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncProjectdavid) -> None:
        vector_store = await async_client.assistants.vector_stores.detach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )
        assert_matches_type(VectorStoreDetachResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.assistants.vector_stores.with_raw_response.detach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStoreDetachResponse, vector_store, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.assistants.vector_stores.with_streaming_response.detach(
            vector_store_id="vector_store_id",
            assistant_id="assistant_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStoreDetachResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.assistants.vector_stores.with_raw_response.detach(
                vector_store_id="vector_store_id",
                assistant_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.assistants.vector_stores.with_raw_response.detach(
                vector_store_id="",
                assistant_id="assistant_id",
                args={},
                kwargs={},
            )
