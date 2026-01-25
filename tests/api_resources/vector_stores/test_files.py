# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types.vector_stores import (
    VectorStoreFile,
    FileListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Projectdavid) -> None:
        file = client.vector_stores.files.list(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Projectdavid) -> None:
        response = client.vector_stores.files.with_raw_response.list(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Projectdavid) -> None:
        with client.vector_stores.files.with_streaming_response.list(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.list(
                vector_store_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Projectdavid) -> None:
        file = client.vector_stores.files.delete(
            vector_store_id="vector_store_id",
            args={},
            file_path="file_path",
            kwargs={},
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Projectdavid) -> None:
        response = client.vector_stores.files.with_raw_response.delete(
            vector_store_id="vector_store_id",
            args={},
            file_path="file_path",
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Projectdavid) -> None:
        with client.vector_stores.files.with_streaming_response.delete(
            vector_store_id="vector_store_id",
            args={},
            file_path="file_path",
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.delete(
                vector_store_id="",
                args={},
                file_path="file_path",
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Projectdavid) -> None:
        file = client.vector_stores.files.add(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            file_id="file_id",
            file_name="file_name",
            file_path="file_path",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Projectdavid) -> None:
        file = client.vector_stores.files.add(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            file_id="file_id",
            file_name="file_name",
            file_path="file_path",
            meta_data={},
            status="deleted",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Projectdavid) -> None:
        response = client.vector_stores.files.with_raw_response.add(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            file_id="file_id",
            file_name="file_name",
            file_path="file_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Projectdavid) -> None:
        with client.vector_stores.files.with_streaming_response.add(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            file_id="file_id",
            file_name="file_name",
            file_path="file_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.add(
                vector_store_id="",
                args={},
                kwargs={},
                file_id="file_id",
                file_name="file_name",
                file_path="file_path",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_status(self, client: Projectdavid) -> None:
        file = client.vector_stores.files.update_status(
            file_id="file_id",
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            status="deleted",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_status_with_all_params(self, client: Projectdavid) -> None:
        file = client.vector_stores.files.update_status(
            file_id="file_id",
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            status="deleted",
            error_message="error_message",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_status(self, client: Projectdavid) -> None:
        response = client.vector_stores.files.with_raw_response.update_status(
            file_id="file_id",
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            status="deleted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_status(self, client: Projectdavid) -> None:
        with client.vector_stores.files.with_streaming_response.update_status(
            file_id="file_id",
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            status="deleted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_status(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.update_status(
                file_id="file_id",
                vector_store_id="",
                args={},
                kwargs={},
                status="deleted",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.vector_stores.files.with_raw_response.update_status(
                file_id="",
                vector_store_id="vector_store_id",
                args={},
                kwargs={},
                status="deleted",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.vector_stores.files.list(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.vector_stores.files.with_raw_response.list(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.vector_stores.files.with_streaming_response.list(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.list(
                vector_store_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.vector_stores.files.delete(
            vector_store_id="vector_store_id",
            args={},
            file_path="file_path",
            kwargs={},
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.vector_stores.files.with_raw_response.delete(
            vector_store_id="vector_store_id",
            args={},
            file_path="file_path",
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.vector_stores.files.with_streaming_response.delete(
            vector_store_id="vector_store_id",
            args={},
            file_path="file_path",
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.delete(
                vector_store_id="",
                args={},
                file_path="file_path",
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.vector_stores.files.add(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            file_id="file_id",
            file_name="file_name",
            file_path="file_path",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.vector_stores.files.add(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            file_id="file_id",
            file_name="file_name",
            file_path="file_path",
            meta_data={},
            status="deleted",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.vector_stores.files.with_raw_response.add(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            file_id="file_id",
            file_name="file_name",
            file_path="file_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.vector_stores.files.with_streaming_response.add(
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            file_id="file_id",
            file_name="file_name",
            file_path="file_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.add(
                vector_store_id="",
                args={},
                kwargs={},
                file_id="file_id",
                file_name="file_name",
                file_path="file_path",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_status(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.vector_stores.files.update_status(
            file_id="file_id",
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            status="deleted",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.vector_stores.files.update_status(
            file_id="file_id",
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            status="deleted",
            error_message="error_message",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.vector_stores.files.with_raw_response.update_status(
            file_id="file_id",
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            status="deleted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.vector_stores.files.with_streaming_response.update_status(
            file_id="file_id",
            vector_store_id="vector_store_id",
            args={},
            kwargs={},
            status="deleted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.update_status(
                file_id="file_id",
                vector_store_id="",
                args={},
                kwargs={},
                status="deleted",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.update_status(
                file_id="",
                vector_store_id="vector_store_id",
                args={},
                kwargs={},
                status="deleted",
            )
