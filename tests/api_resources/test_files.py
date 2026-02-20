# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types import (
    File,
    FileDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Projectdavid) -> None:
        file = client.files.retrieve(
            file_id="file_id",
            args={},
            kwargs={},
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Projectdavid) -> None:
        response = client.files.with_raw_response.retrieve(
            file_id="file_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Projectdavid) -> None:
        with client.files.with_streaming_response.retrieve(
            file_id="file_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.retrieve(
                file_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Projectdavid) -> None:
        file = client.files.delete(
            file_id="file_id",
            args={},
            kwargs={},
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Projectdavid) -> None:
        response = client.files.with_raw_response.delete(
            file_id="file_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Projectdavid) -> None:
        with client.files.with_streaming_response.delete(
            file_id="file_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                file_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_signed_url(self, client: Projectdavid) -> None:
        file = client.files.generate_signed_url(
            file_id="file_id",
            args={},
            kwargs={},
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_signed_url_with_all_params(self, client: Projectdavid) -> None:
        file = client.files.generate_signed_url(
            file_id="file_id",
            args={},
            kwargs={},
            expires_in=0,
            use_real_filename=True,
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_signed_url(self, client: Projectdavid) -> None:
        response = client.files.with_raw_response.generate_signed_url(
            file_id="file_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_signed_url(self, client: Projectdavid) -> None:
        with client.files.with_streaming_response.generate_signed_url(
            file_id="file_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_generate_signed_url(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.generate_signed_url(
                file_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_base64(self, client: Projectdavid) -> None:
        file = client.files.get_base64(
            file_id="file_id",
            args={},
            kwargs={},
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_base64(self, client: Projectdavid) -> None:
        response = client.files.with_raw_response.get_base64(
            file_id="file_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_base64(self, client: Projectdavid) -> None:
        with client.files.with_streaming_response.get_base64(
            file_id="file_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_base64(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.get_base64(
                file_id="",
                args={},
                kwargs={},
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.files.retrieve(
            file_id="file_id",
            args={},
            kwargs={},
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.files.with_raw_response.retrieve(
            file_id="file_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.files.with_streaming_response.retrieve(
            file_id="file_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.retrieve(
                file_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.files.delete(
            file_id="file_id",
            args={},
            kwargs={},
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.files.with_raw_response.delete(
            file_id="file_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.files.with_streaming_response.delete(
            file_id="file_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                file_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_signed_url(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.files.generate_signed_url(
            file_id="file_id",
            args={},
            kwargs={},
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_signed_url_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.files.generate_signed_url(
            file_id="file_id",
            args={},
            kwargs={},
            expires_in=0,
            use_real_filename=True,
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_signed_url(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.files.with_raw_response.generate_signed_url(
            file_id="file_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_signed_url(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.files.with_streaming_response.generate_signed_url(
            file_id="file_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_generate_signed_url(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.generate_signed_url(
                file_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_base64(self, async_client: AsyncProjectdavid) -> None:
        file = await async_client.files.get_base64(
            file_id="file_id",
            args={},
            kwargs={},
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_base64(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.files.with_raw_response.get_base64(
            file_id="file_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_base64(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.files.with_streaming_response.get_base64(
            file_id="file_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_base64(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.get_base64(
                file_id="",
                args={},
                kwargs={},
            )
