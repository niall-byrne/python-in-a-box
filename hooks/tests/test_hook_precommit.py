"""Test the PostGenPrecommitSetup class."""

import os
from unittest.mock import Mock, patch

import pytest

from hooks.post_gen_project import BaseHookSystemCalls, PostGenPrecommitSetup


class TestPostGenPrecommitSetup:
    """Test the PostGenPrecommitSetup class."""

    def test_instance__when_initialized__has_correct_inheritance(
        self,
        precommit_setup_hook: PostGenPrecommitSetup,
    ) -> None:
        assert isinstance(precommit_setup_hook, BaseHookSystemCalls)
        assert isinstance(precommit_setup_hook, PostGenPrecommitSetup)

    def test_instance__when_initialized__has_correct_properties(
        self,
        precommit_setup_hook: PostGenPrecommitSetup,
    ) -> None:
        assert precommit_setup_hook.precommit_setup_command == \
               "poetry run pre-commit install"

    @pytest.mark.parametrize(
        "env,expected", [
            [{}, True],
            [{
                "TEMPLATE_SKIP_PRECOMMIT": "0"
            }, True],
            [{
                "TEMPLATE_SKIP_PRECOMMIT": "1"
            }, False],
        ]
    )
    def test_condition__with_parametrized_scenario__returns_expected(
        self,
        env: dict,
        expected: bool,
        precommit_setup_hook: PostGenPrecommitSetup,
    ) -> None:
        with patch.dict(os.environ, env, clear=True):
            assert precommit_setup_hook.condition() == expected

    @patch("os.system")
    def test_hook__correct_system_calls(
        self,
        m_system: Mock,
        precommit_setup_hook: PostGenPrecommitSetup,
    ) -> None:
        m_system.return_value = 1

        precommit_setup_hook.hook()

        m_system.assert_called_once_with(
            precommit_setup_hook.precommit_setup_command
        )
