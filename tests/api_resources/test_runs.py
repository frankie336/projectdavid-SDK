# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types import (
    Run,
    RunList,
    RunRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Projectdavid) -> None:
        run = client.runs.create(
            args={},
            kwargs={},
            id="id",
            assistant_id="assistant_id",
            created_at=0,
            expires_at=0,
            instructions="instructions",
            thread_id="thread_id",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Projectdavid) -> None:
        run = client.runs.create(
            args={},
            kwargs={},
            id="id",
            assistant_id="assistant_id",
            created_at=0,
            expires_at=0,
            instructions="instructions",
            thread_id="thread_id",
            cancelled_at=0,
            completed_at=0,
            failed_at=0,
            incomplete_details={},
            last_error="last_error",
            max_completion_tokens=0,
            max_prompt_tokens=0,
            meta_data={},
            model="model",
            object="object",
            parallel_tool_calls=True,
            required_action="required_action",
            response_format="response_format",
            started_at=0,
            status="queued",
            temperature=0,
            tool_choice="tool_choice",
            tool_resources={},
            tools=[
                {
                    "id": "id",
                    "type": "type",
                    "function": {"function": {}},
                    "name": "name",
                }
            ],
            top_p=0,
            truncation_strategy="auto",
            usage={},
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Projectdavid) -> None:
        response = client.runs.with_raw_response.create(
            args={},
            kwargs={},
            id="id",
            assistant_id="assistant_id",
            created_at=0,
            expires_at=0,
            instructions="instructions",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Projectdavid) -> None:
        with client.runs.with_streaming_response.create(
            args={},
            kwargs={},
            id="id",
            assistant_id="assistant_id",
            created_at=0,
            expires_at=0,
            instructions="instructions",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Projectdavid) -> None:
        run = client.runs.retrieve(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Projectdavid) -> None:
        response = client.runs.with_raw_response.retrieve(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Projectdavid) -> None:
        with client.runs.with_streaming_response.retrieve(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunRetrieveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.retrieve(
                run_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Projectdavid) -> None:
        run = client.runs.list(
            args={},
            kwargs={},
        )
        assert_matches_type(RunList, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Projectdavid) -> None:
        run = client.runs.list(
            args={},
            kwargs={},
            limit=1,
            order="asc",
            thread_id="thread_id",
        )
        assert_matches_type(RunList, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Projectdavid) -> None:
        response = client.runs.with_raw_response.list(
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunList, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Projectdavid) -> None:
        with client.runs.with_streaming_response.list(
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunList, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Projectdavid) -> None:
        run = client.runs.cancel(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Projectdavid) -> None:
        response = client.runs.with_raw_response.cancel(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Projectdavid) -> None:
        with client.runs.with_streaming_response.cancel(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.cancel(
                run_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_events(self, client: Projectdavid) -> None:
        run = client.runs.stream_events(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert run is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_events(self, client: Projectdavid) -> None:
        response = client.runs.with_raw_response.stream_events(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert run is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_events(self, client: Projectdavid) -> None:
        with client.runs.with_streaming_response.stream_events(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert run is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stream_events(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.stream_events(
                run_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_metadata(self, client: Projectdavid) -> None:
        run = client.runs.update_metadata(
            run_id="run_id",
            args={},
            kwargs={},
            body={},
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_metadata(self, client: Projectdavid) -> None:
        response = client.runs.with_raw_response.update_metadata(
            run_id="run_id",
            args={},
            kwargs={},
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_metadata(self, client: Projectdavid) -> None:
        with client.runs.with_streaming_response.update_metadata(
            run_id="run_id",
            args={},
            kwargs={},
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_metadata(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.update_metadata(
                run_id="",
                args={},
                kwargs={},
                body={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_status(self, client: Projectdavid) -> None:
        run = client.runs.update_status(
            run_id="run_id",
            args={},
            kwargs={},
            status="queued",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_status(self, client: Projectdavid) -> None:
        response = client.runs.with_raw_response.update_status(
            run_id="run_id",
            args={},
            kwargs={},
            status="queued",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_status(self, client: Projectdavid) -> None:
        with client.runs.with_streaming_response.update_status(
            run_id="run_id",
            args={},
            kwargs={},
            status="queued",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_status(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.update_status(
                run_id="",
                args={},
                kwargs={},
                status="queued",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncProjectdavid) -> None:
        run = await async_client.runs.create(
            args={},
            kwargs={},
            id="id",
            assistant_id="assistant_id",
            created_at=0,
            expires_at=0,
            instructions="instructions",
            thread_id="thread_id",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        run = await async_client.runs.create(
            args={},
            kwargs={},
            id="id",
            assistant_id="assistant_id",
            created_at=0,
            expires_at=0,
            instructions="instructions",
            thread_id="thread_id",
            cancelled_at=0,
            completed_at=0,
            failed_at=0,
            incomplete_details={},
            last_error="last_error",
            max_completion_tokens=0,
            max_prompt_tokens=0,
            meta_data={},
            model="model",
            object="object",
            parallel_tool_calls=True,
            required_action="required_action",
            response_format="response_format",
            started_at=0,
            status="queued",
            temperature=0,
            tool_choice="tool_choice",
            tool_resources={},
            tools=[
                {
                    "id": "id",
                    "type": "type",
                    "function": {"function": {}},
                    "name": "name",
                }
            ],
            top_p=0,
            truncation_strategy="auto",
            usage={},
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.runs.with_raw_response.create(
            args={},
            kwargs={},
            id="id",
            assistant_id="assistant_id",
            created_at=0,
            expires_at=0,
            instructions="instructions",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.runs.with_streaming_response.create(
            args={},
            kwargs={},
            id="id",
            assistant_id="assistant_id",
            created_at=0,
            expires_at=0,
            instructions="instructions",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncProjectdavid) -> None:
        run = await async_client.runs.retrieve(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.runs.with_raw_response.retrieve(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.runs.with_streaming_response.retrieve(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunRetrieveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.retrieve(
                run_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncProjectdavid) -> None:
        run = await async_client.runs.list(
            args={},
            kwargs={},
        )
        assert_matches_type(RunList, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        run = await async_client.runs.list(
            args={},
            kwargs={},
            limit=1,
            order="asc",
            thread_id="thread_id",
        )
        assert_matches_type(RunList, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.runs.with_raw_response.list(
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunList, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.runs.with_streaming_response.list(
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunList, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncProjectdavid) -> None:
        run = await async_client.runs.cancel(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.runs.with_raw_response.cancel(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.runs.with_streaming_response.cancel(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.cancel(
                run_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_events(self, async_client: AsyncProjectdavid) -> None:
        run = await async_client.runs.stream_events(
            run_id="run_id",
            args={},
            kwargs={},
        )
        assert run is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_events(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.runs.with_raw_response.stream_events(
            run_id="run_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert run is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_events(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.runs.with_streaming_response.stream_events(
            run_id="run_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert run is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stream_events(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.stream_events(
                run_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_metadata(self, async_client: AsyncProjectdavid) -> None:
        run = await async_client.runs.update_metadata(
            run_id="run_id",
            args={},
            kwargs={},
            body={},
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_metadata(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.runs.with_raw_response.update_metadata(
            run_id="run_id",
            args={},
            kwargs={},
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_metadata(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.runs.with_streaming_response.update_metadata(
            run_id="run_id",
            args={},
            kwargs={},
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_metadata(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.update_metadata(
                run_id="",
                args={},
                kwargs={},
                body={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_status(self, async_client: AsyncProjectdavid) -> None:
        run = await async_client.runs.update_status(
            run_id="run_id",
            args={},
            kwargs={},
            status="queued",
        )
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.runs.with_raw_response.update_status(
            run_id="run_id",
            args={},
            kwargs={},
            status="queued",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.runs.with_streaming_response.update_status(
            run_id="run_id",
            args={},
            kwargs={},
            status="queued",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.update_status(
                run_id="",
                args={},
                kwargs={},
                status="queued",
            )
