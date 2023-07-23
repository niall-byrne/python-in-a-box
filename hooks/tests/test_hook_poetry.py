"""Test the PostGenPoetrySetup class."""

import os
from unittest.mock import Mock, call, patch

import pytest

from hooks.post_gen_project import BaseHookSystemCalls, PostGenPoetrySetup


class TestPostGenPoetrySetup:
    """Test the PostGenPoetrySetup class."""

    def test_instance__when_initialized__has_correct_inheritance(
        self,
        poetry_setup_hook: PostGenPoetrySetup,
    ) -> None:
        assert isinstance(poetry_setup_hook, BaseHookSystemCalls)
        assert isinstance(poetry_setup_hook, PostGenPoetrySetup)

    def test_instance__when_initialized__has_correct_properties(
        self,
        poetry_setup_hook: PostGenPoetrySetup,
    ) -> None:
        assert poetry_setup_hook.poetry_lock_command == \
               "poetry lock"
        assert poetry_setup_hook.poetry_install_command == \
               "poetry install"

    @pytest.mark.parametrize(
        "env,expected", [
            [{}, True],
            [{
                "TEMPLATE_SKIP_POETRY": "0"
            }, True],
            [{
                "TEMPLATE_SKIP_POETRY": "1"
            }, False],
        ]
    )
    def test_condition__with_parametrized_scenario__returns_expected(
        self,
        env: dict,
        expected: bool,
        poetry_setup_hook: PostGenPoetrySetup,
    ) -> None:
        with patch.dict(os.environ, env, clear=True):
            assert poetry_setup_hook.condition() == expected

    @patch("os.system")
    def test_hook__when_called__has_correct_system_calls(
        self,
        m_system: Mock,
        poetry_setup_hook: PostGenPoetrySetup,
    ) -> None:
        m_system.return_value = 1
        expected_calls = [
            poetry_setup_hook.poetry_lock_command,
            poetry_setup_hook.poetry_install_command
        ]

        poetry_setup_hook.hook()

        assert m_system.call_args_list == list(map(call, expected_calls))
