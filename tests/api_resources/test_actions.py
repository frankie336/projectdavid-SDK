# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types import (
    ActionRead,
    ActionListPendingResponse,
)
from projectdavid._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Projectdavid) -> None:
        action = client.actions.create(
            args={},
            kwargs={},
            run_id="example_run_id",
        )
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Projectdavid) -> None:
        action = client.actions.create(
            args={},
            kwargs={},
            run_id="example_run_id",
            id="id",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            function_args={"arg1": "value1"},
            status="pending",
            tool_call_id="call_abc123",
            tool_name="example_tool_name",
            turn_index=0,
        )
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Projectdavid) -> None:
        response = client.actions.with_raw_response.create(
            args={},
            kwargs={},
            run_id="example_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Projectdavid) -> None:
        with client.actions.with_streaming_response.create(
            args={},
            kwargs={},
            run_id="example_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRead, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Projectdavid) -> None:
        action = client.actions.retrieve(
            action_id="action_id",
            args={},
            kwargs={},
        )
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Projectdavid) -> None:
        response = client.actions.with_raw_response.retrieve(
            action_id="action_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Projectdavid) -> None:
        with client.actions.with_streaming_response.retrieve(
            action_id="action_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRead, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            client.actions.with_raw_response.retrieve(
                action_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Projectdavid) -> None:
        action = client.actions.update(
            action_id="action_id",
            args={},
            kwargs={},
            status="pending",
        )
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Projectdavid) -> None:
        action = client.actions.update(
            action_id="action_id",
            args={},
            kwargs={},
            status="pending",
            result={},
        )
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Projectdavid) -> None:
        response = client.actions.with_raw_response.update(
            action_id="action_id",
            args={},
            kwargs={},
            status="pending",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Projectdavid) -> None:
        with client.actions.with_streaming_response.update(
            action_id="action_id",
            args={},
            kwargs={},
            status="pending",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRead, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            client.actions.with_raw_response.update(
                action_id="",
                args={},
                kwargs={},
                status="pending",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Projectdavid) -> None:
        action = client.actions.delete(
            action_id="action_id",
            args={},
            kwargs={},
        )
        assert action is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Projectdavid) -> None:
        response = client.actions.with_raw_response.delete(
            action_id="action_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert action is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Projectdavid) -> None:
        with client.actions.with_streaming_response.delete(
            action_id="action_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            client.actions.with_raw_response.delete(
                action_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_pending(self, client: Projectdavid) -> None:
        action = client.actions.list_pending(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert_matches_type(ActionListPendingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_pending(self, client: Projectdavid) -> None:
        response = client.actions.with_raw_response.list_pending(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionListPendingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_pending(self, client: Projectdavid) -> None:
        with client.actions.with_streaming_response.list_pending(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionListPendingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_pending(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.actions.with_raw_response.list_pending(
                run_id="",
                args={},
                kwargs={},
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncProjectdavid) -> None:
        action = await async_client.actions.create(
            args={},
            kwargs={},
            run_id="example_run_id",
        )
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        action = await async_client.actions.create(
            args={},
            kwargs={},
            run_id="example_run_id",
            id="id",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            function_args={"arg1": "value1"},
            status="pending",
            tool_call_id="call_abc123",
            tool_name="example_tool_name",
            turn_index=0,
        )
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.actions.with_raw_response.create(
            args={},
            kwargs={},
            run_id="example_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.actions.with_streaming_response.create(
            args={},
            kwargs={},
            run_id="example_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRead, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncProjectdavid) -> None:
        action = await async_client.actions.retrieve(
            action_id="action_id",
            args={},
            kwargs={},
        )
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.actions.with_raw_response.retrieve(
            action_id="action_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.actions.with_streaming_response.retrieve(
            action_id="action_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRead, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            await async_client.actions.with_raw_response.retrieve(
                action_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncProjectdavid) -> None:
        action = await async_client.actions.update(
            action_id="action_id",
            args={},
            kwargs={},
            status="pending",
        )
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        action = await async_client.actions.update(
            action_id="action_id",
            args={},
            kwargs={},
            status="pending",
            result={},
        )
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.actions.with_raw_response.update(
            action_id="action_id",
            args={},
            kwargs={},
            status="pending",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRead, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.actions.with_streaming_response.update(
            action_id="action_id",
            args={},
            kwargs={},
            status="pending",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRead, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            await async_client.actions.with_raw_response.update(
                action_id="",
                args={},
                kwargs={},
                status="pending",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncProjectdavid) -> None:
        action = await async_client.actions.delete(
            action_id="action_id",
            args={},
            kwargs={},
        )
        assert action is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.actions.with_raw_response.delete(
            action_id="action_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert action is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.actions.with_streaming_response.delete(
            action_id="action_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert action is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            await async_client.actions.with_raw_response.delete(
                action_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_pending(self, async_client: AsyncProjectdavid) -> None:
        action = await async_client.actions.list_pending(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert_matches_type(ActionListPendingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_pending(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.actions.with_raw_response.list_pending(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionListPendingResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_pending(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.actions.with_streaming_response.list_pending(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionListPendingResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_pending(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.actions.with_raw_response.list_pending(
                run_id="",
                args={},
                kwargs={},
            )
