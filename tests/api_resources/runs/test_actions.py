# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types.runs import ActionGetByStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_status(self, client: Projectdavid) -> None:
        action = client.runs.actions.get_by_status(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert_matches_type(ActionGetByStatusResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_status_with_all_params(self, client: Projectdavid) -> None:
        action = client.runs.actions.get_by_status(
            run_id="run_id",
            args={},
            kwargs={},
            status="status",
        )
        assert_matches_type(ActionGetByStatusResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_status(self, client: Projectdavid) -> None:
        response = client.runs.actions.with_raw_response.get_by_status(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionGetByStatusResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_status(self, client: Projectdavid) -> None:
        with client.runs.actions.with_streaming_response.get_by_status(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionGetByStatusResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_status(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.actions.with_raw_response.get_by_status(
                run_id="",
                args={},
                kwargs={},
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_status(self, async_client: AsyncProjectdavid) -> None:
        action = await async_client.runs.actions.get_by_status(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert_matches_type(ActionGetByStatusResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_status_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        action = await async_client.runs.actions.get_by_status(
            run_id="run_id",
            args={},
            kwargs={},
            status="status",
        )
        assert_matches_type(ActionGetByStatusResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_status(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.runs.actions.with_raw_response.get_by_status(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionGetByStatusResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_status(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.runs.actions.with_streaming_response.get_by_status(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionGetByStatusResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_status(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.actions.with_raw_response.get_by_status(
                run_id="",
                args={},
                kwargs={},
            )
