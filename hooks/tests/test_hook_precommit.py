"""Test the PostGenPrecommitSetup class."""

import os
from unittest import TestCase
from unittest.mock import Mock, patch

from ..post_gen_project import BaseHookSystemCalls, PostGenPrecommitSetup


class TestPostGenPrecommitSetup(TestCase):
    """Test the PostGenPrecommitSetup class."""

    def setUp(self) -> None:
        self.instance = PostGenPrecommitSetup()

    def test_initialize__has_correct_properties(self) -> None:
        self.assertIsInstance(self.instance, BaseHookSystemCalls)
        self.assertEqual(
            self.instance.precommit_setup_command,
            "poetry run pre-commit install",
        )

    @patch.dict(os.environ, {}, clear=True)
    def test_condition__no_env__true(self) -> None:
        self.assertTrue(self.instance.condition())

    @patch.dict(os.environ, {"TEMPLATE_SKIP_PRECOMMIT": "0"}, clear=True)
    def test_condition__non_1_env__false(self) -> None:
        self.assertTrue(self.instance.condition())

    @patch.dict(os.environ, {"TEMPLATE_SKIP_PRECOMMIT": "1"}, clear=True)
    def test_condition__env_1__false(self) -> None:
        self.assertFalse(self.instance.condition())

    @patch("os.system")
    def test_hook__correct_system_calls(self, m_system: Mock) -> None:
        m_system.return_value = 1

        self.instance.hook()

        m_system.assert_called_once_with(self.instance.precommit_setup_command)
