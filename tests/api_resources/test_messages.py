# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid
from projectdavid.types import (
    MessageRead,
    MessageDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Projectdavid) -> None:
        message = client.messages.create(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Projectdavid) -> None:
        message = client.messages.create(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
            is_last_chunk=True,
            meta_data={"key": "value"},
            sender_id="sender_id",
            tool_call_id="tool_call_id",
            tool_id="tool_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Projectdavid) -> None:
        response = client.messages.with_raw_response.create(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Projectdavid) -> None:
        with client.messages.with_streaming_response.create(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRead, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Projectdavid) -> None:
        message = client.messages.retrieve(
            message_id="message_id",
            args={},
            kwargs={},
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Projectdavid) -> None:
        response = client.messages.with_raw_response.retrieve(
            message_id="message_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Projectdavid) -> None:
        with client.messages.with_streaming_response.retrieve(
            message_id="message_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRead, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.retrieve(
                message_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Projectdavid) -> None:
        message = client.messages.delete(
            message_id="message_id",
            args={},
            kwargs={},
        )
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Projectdavid) -> None:
        response = client.messages.with_raw_response.delete(
            message_id="message_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Projectdavid) -> None:
        with client.messages.with_streaming_response.delete(
            message_id="message_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageDeleteResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.delete(
                message_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_save_assistant_message(self, client: Projectdavid) -> None:
        message = client.messages.save_assistant_message(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_save_assistant_message_with_all_params(self, client: Projectdavid) -> None:
        message = client.messages.save_assistant_message(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
            is_last_chunk=True,
            meta_data={"key": "value"},
            sender_id="sender_id",
            tool_call_id="tool_call_id",
            tool_id="tool_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_save_assistant_message(self, client: Projectdavid) -> None:
        response = client.messages.with_raw_response.save_assistant_message(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_save_assistant_message(self, client: Projectdavid) -> None:
        with client.messages.with_streaming_response.save_assistant_message(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRead, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_tool_response(self, client: Projectdavid) -> None:
        message = client.messages.submit_tool_response(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_tool_response_with_all_params(self, client: Projectdavid) -> None:
        message = client.messages.submit_tool_response(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
            is_last_chunk=True,
            meta_data={"key": "value"},
            sender_id="sender_id",
            tool_call_id="tool_call_id",
            tool_id="tool_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_tool_response(self, client: Projectdavid) -> None:
        response = client.messages.with_raw_response.submit_tool_response(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_tool_response(self, client: Projectdavid) -> None:
        with client.messages.with_streaming_response.submit_tool_response(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRead, message, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncProjectdavid) -> None:
        message = await async_client.messages.create(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        message = await async_client.messages.create(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
            is_last_chunk=True,
            meta_data={"key": "value"},
            sender_id="sender_id",
            tool_call_id="tool_call_id",
            tool_id="tool_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.messages.with_raw_response.create(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.messages.with_streaming_response.create(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRead, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncProjectdavid) -> None:
        message = await async_client.messages.retrieve(
            message_id="message_id",
            args={},
            kwargs={},
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.messages.with_raw_response.retrieve(
            message_id="message_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.messages.with_streaming_response.retrieve(
            message_id="message_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRead, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.retrieve(
                message_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncProjectdavid) -> None:
        message = await async_client.messages.delete(
            message_id="message_id",
            args={},
            kwargs={},
        )
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.messages.with_raw_response.delete(
            message_id="message_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.messages.with_streaming_response.delete(
            message_id="message_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageDeleteResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.delete(
                message_id="",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_save_assistant_message(self, async_client: AsyncProjectdavid) -> None:
        message = await async_client.messages.save_assistant_message(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_save_assistant_message_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        message = await async_client.messages.save_assistant_message(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
            is_last_chunk=True,
            meta_data={"key": "value"},
            sender_id="sender_id",
            tool_call_id="tool_call_id",
            tool_id="tool_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_save_assistant_message(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.messages.with_raw_response.save_assistant_message(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_save_assistant_message(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.messages.with_streaming_response.save_assistant_message(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRead, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_tool_response(self, async_client: AsyncProjectdavid) -> None:
        message = await async_client.messages.submit_tool_response(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_tool_response_with_all_params(self, async_client: AsyncProjectdavid) -> None:
        message = await async_client.messages.submit_tool_response(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
            is_last_chunk=True,
            meta_data={"key": "value"},
            sender_id="sender_id",
            tool_call_id="tool_call_id",
            tool_id="tool_id",
        )
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_tool_response(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.messages.with_raw_response.submit_tool_response(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRead, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_tool_response(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.messages.with_streaming_response.submit_tool_response(
            args={},
            kwargs={},
            assistant_id="example_assistant_id",
            content="Hello, this is a test message.",
            role="user",
            thread_id="example_thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRead, message, path=["response"])

        assert cast(Any, response.is_closed) is True
