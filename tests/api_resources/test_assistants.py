# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types import (
    AssistantRead,
    AssistantListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssistants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Projectdavid) -> None:
        assistant = client.assistants.create(
            args={},
            kwargs={},
            model="gpt-4o-mini",
            name="Search Assistant",
        )
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Projectdavid) -> None:
        assistant = client.assistants.create(
            args={},
            kwargs={},
            model="gpt-4o-mini",
            name="Search Assistant",
            id="id",
            description="description",
            instructions="instructions",
            meta_data={},
            response_format="response_format",
            temperature=0,
            tool_resources={"file_search": {}},
            tools=[{}],
            top_p=0,
            webhook_secret="xxxxxxxxxxxxxxxx",
            webhook_url="https://example.com",
        )
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Projectdavid) -> None:
        response = client.assistants.with_raw_response.create(
            args={},
            kwargs={},
            model="gpt-4o-mini",
            name="Search Assistant",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Projectdavid) -> None:
        with client.assistants.with_streaming_response.create(
            args={},
            kwargs={},
            model="gpt-4o-mini",
            name="Search Assistant",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantRead, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Projectdavid) -> None:
        assistant = client.assistants.retrieve(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Projectdavid) -> None:
        response = client.assistants.with_raw_response.retrieve(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Projectdavid) -> None:
        with client.assistants.with_streaming_response.retrieve(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantRead, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.assistants.with_raw_response.retrieve(
                assistant_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Projectdavid) -> None:
        assistant = client.assistants.update(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Projectdavid) -> None:
        assistant = client.assistants.update(
            assistant_id="assistant_id",
            args={},
            kwargs={},
            description="description",
            instructions="instructions",
            meta_data={},
            model="model",
            name="name",
            response_format="response_format",
            temperature=0,
            tool_resources={"foo": {}},
            tools=["string"],
            top_p=0,
            users=["string"],
            vector_stores=["string"],
            webhook_secret="xxxxxxxxxxxxxxxx",
            webhook_url="https://example.com",
        )
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Projectdavid) -> None:
        response = client.assistants.with_raw_response.update(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Projectdavid) -> None:
        with client.assistants.with_streaming_response.update(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantRead, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.assistants.with_raw_response.update(
                assistant_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Projectdavid) -> None:
        assistant = client.assistants.list(
            args={},
            kwargs={},
        )
        assert_matches_type(AssistantListResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Projectdavid) -> None:
        response = client.assistants.with_raw_response.list(
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantListResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Projectdavid) -> None:
        with client.assistants.with_streaming_response.list(
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantListResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssistants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncProjectdavid) -> None:
        assistant = await async_client.assistants.create(
            args={},
            kwargs={},
            model="gpt-4o-mini",
            name="Search Assistant",
        )
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        assistant = await async_client.assistants.create(
            args={},
            kwargs={},
            model="gpt-4o-mini",
            name="Search Assistant",
            id="id",
            description="description",
            instructions="instructions",
            meta_data={},
            response_format="response_format",
            temperature=0,
            tool_resources={"file_search": {}},
            tools=[{}],
            top_p=0,
            webhook_secret="xxxxxxxxxxxxxxxx",
            webhook_url="https://example.com",
        )
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.assistants.with_raw_response.create(
            args={},
            kwargs={},
            model="gpt-4o-mini",
            name="Search Assistant",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.assistants.with_streaming_response.create(
            args={},
            kwargs={},
            model="gpt-4o-mini",
            name="Search Assistant",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantRead, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncProjectdavid) -> None:
        assistant = await async_client.assistants.retrieve(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.assistants.with_raw_response.retrieve(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.assistants.with_streaming_response.retrieve(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantRead, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.assistants.with_raw_response.retrieve(
                assistant_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncProjectdavid) -> None:
        assistant = await async_client.assistants.update(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        assistant = await async_client.assistants.update(
            assistant_id="assistant_id",
            args={},
            kwargs={},
            description="description",
            instructions="instructions",
            meta_data={},
            model="model",
            name="name",
            response_format="response_format",
            temperature=0,
            tool_resources={"foo": {}},
            tools=["string"],
            top_p=0,
            users=["string"],
            vector_stores=["string"],
            webhook_secret="xxxxxxxxxxxxxxxx",
            webhook_url="https://example.com",
        )
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.assistants.with_raw_response.update(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantRead, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.assistants.with_streaming_response.update(
            assistant_id="assistant_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantRead, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.assistants.with_raw_response.update(
                assistant_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncProjectdavid) -> None:
        assistant = await async_client.assistants.list(
            args={},
            kwargs={},
        )
        assert_matches_type(AssistantListResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.assistants.with_raw_response.list(
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantListResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.assistants.with_streaming_response.list(
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantListResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True
