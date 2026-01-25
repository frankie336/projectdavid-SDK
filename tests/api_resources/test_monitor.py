# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitor:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_run(self, client: Projectdavid) -> None:
        monitor = client.monitor.register_run(
            args={},
            kwargs={},
            run_id="run_id",
        )
        assert_matches_type(object, monitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register_run(self, client: Projectdavid) -> None:
        response = client.monitor.with_raw_response.register_run(
            args={},
            kwargs={},
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(object, monitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register_run(self, client: Projectdavid) -> None:
        with client.monitor.with_streaming_response.register_run(
            args={},
            kwargs={},
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(object, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMonitor:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_run(self, async_client: AsyncProjectdavid) -> None:
        monitor = await async_client.monitor.register_run(
            args={},
            kwargs={},
            run_id="run_id",
        )
        assert_matches_type(object, monitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register_run(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.monitor.with_raw_response.register_run(
            args={},
            kwargs={},
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(object, monitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register_run(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.monitor.with_streaming_response.register_run(
            args={},
            kwargs={},
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(object, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True
