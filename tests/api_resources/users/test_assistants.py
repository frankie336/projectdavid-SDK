# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from projectdavid import Projectdavid, AsyncProjectdavid

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssistants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_associate(self, client: Projectdavid) -> None:
        assistant = client.users.assistants.associate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_associate(self, client: Projectdavid) -> None:
        response = client.users.assistants.with_raw_response.associate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_associate(self, client: Projectdavid) -> None:
        with client.users.assistants.with_streaming_response.associate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(object, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_associate(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.assistants.with_raw_response.associate(
                assistant_id="assistant_id",
                user_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.users.assistants.with_raw_response.associate(
                assistant_id="",
                user_id="user_id",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disassociate(self, client: Projectdavid) -> None:
        assistant = client.users.assistants.disassociate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert assistant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disassociate(self, client: Projectdavid) -> None:
        response = client.users.assistants.with_raw_response.disassociate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert assistant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disassociate(self, client: Projectdavid) -> None:
        with client.users.assistants.with_streaming_response.disassociate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert assistant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disassociate(self, client: Projectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.assistants.with_raw_response.disassociate(
                assistant_id="assistant_id",
                user_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.users.assistants.with_raw_response.disassociate(
                assistant_id="",
                user_id="user_id",
                args={},
                kwargs={},
            )


class TestAsyncAssistants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_associate(self, async_client: AsyncProjectdavid) -> None:
        assistant = await async_client.users.assistants.associate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_associate(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.users.assistants.with_raw_response.associate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_associate(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.users.assistants.with_streaming_response.associate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(object, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_associate(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.assistants.with_raw_response.associate(
                assistant_id="assistant_id",
                user_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.users.assistants.with_raw_response.associate(
                assistant_id="",
                user_id="user_id",
                args={},
                kwargs={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disassociate(self, async_client: AsyncProjectdavid) -> None:
        assistant = await async_client.users.assistants.disassociate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        )
        assert assistant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disassociate(self, async_client: AsyncProjectdavid) -> None:
        response = await async_client.users.assistants.with_raw_response.disassociate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert assistant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disassociate(self, async_client: AsyncProjectdavid) -> None:
        async with async_client.users.assistants.with_streaming_response.disassociate(
            assistant_id="assistant_id",
            user_id="user_id",
            args={},
            kwargs={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert assistant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disassociate(self, async_client: AsyncProjectdavid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.assistants.with_raw_response.disassociate(
                assistant_id="assistant_id",
                user_id="",
                args={},
                kwargs={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.users.assistants.with_raw_response.disassociate(
                assistant_id="",
                user_id="user_id",
                args={},
                kwargs={},
            )
