# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscribe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_run_events(self, client: Projectdavid) -> None:
        subscribe = client.subscribe.retrieve_run_events(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert_matches_type(object, subscribe, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_run_events(self, client: Projectdavid) -> None:
        response = client.subscribe.with_raw_response.retrieve_run_events(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscribe = response.parse()
        assert_matches_type(object, subscribe, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_run_events(self, client: Projectdavid) -> None:
        with client.subscribe.with_streaming_response.retrieve_run_events(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscribe = response.parse()
            assert_matches_type(object, subscribe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_run_events(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.subscribe.with_raw_response.retrieve_run_events(
                run_id="",
                args={},
                kwargs={},
            )


class TestAsyncSubscribe:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_run_events(self, async_client: AsyncProjectdavid) -> None:
        subscribe = await async_client.subscribe.retrieve_run_events(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert_matches_type(object, subscribe, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_run_events(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.subscribe.with_raw_response.retrieve_run_events(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscribe = await response.parse()
        assert_matches_type(object, subscribe, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_run_events(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.subscribe.with_streaming_response.retrieve_run_events(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscribe = await response.parse()
            assert_matches_type(object, subscribe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_run_events(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.subscribe.with_raw_response.retrieve_run_events(
                run_id="",
                args={},
                kwargs={},
            )
