# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Projectdavid) -> None:
        completion = client.completions.create(
            api_key="api_key",
            assistant_id="assistant_id",
            message_id="message_id",
            model="model",
            provider="provider",
            run_id="run_id",
            thread_id="thread_id",
        )
        assert_matches_type(object, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Projectdavid) -> None:
        completion = client.completions.create(
            api_key="api_key",
            assistant_id="assistant_id",
            message_id="message_id",
            model="model",
            provider="provider",
            run_id="run_id",
            thread_id="thread_id",
            content="content",
        )
        assert_matches_type(object, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Projectdavid) -> None:
        response = client.completions.with_raw_response.create(
            api_key="api_key",
            assistant_id="assistant_id",
            message_id="message_id",
            model="model",
            provider="provider",
            run_id="run_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(object, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Projectdavid) -> None:
        with client.completions.with_streaming_response.create(
            api_key="api_key",
            assistant_id="assistant_id",
            message_id="message_id",
            model="model",
            provider="provider",
            run_id="run_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(object, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncProjectdavid) -> None:
        completion = await async_client.completions.create(
            api_key="api_key",
            assistant_id="assistant_id",
            message_id="message_id",
            model="model",
            provider="provider",
            run_id="run_id",
            thread_id="thread_id",
        )
        assert_matches_type(object, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        completion = await async_client.completions.create(
            api_key="api_key",
            assistant_id="assistant_id",
            message_id="message_id",
            model="model",
            provider="provider",
            run_id="run_id",
            thread_id="thread_id",
            content="content",
        )
        assert_matches_type(object, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.completions.with_raw_response.create(
            api_key="api_key",
            assistant_id="assistant_id",
            message_id="message_id",
            model="model",
            provider="provider",
            run_id="run_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(object, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.completions.with_streaming_response.create(
            api_key="api_key",
            assistant_id="assistant_id",
            message_id="message_id",
            model="model",
            provider="provider",
            run_id="run_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(object, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
