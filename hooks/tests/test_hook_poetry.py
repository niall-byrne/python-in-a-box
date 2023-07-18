"""Test the PostGenPoetrySetup class."""

import os
from unittest import TestCase
from unittest.mock import Mock, call, patch

from ..post_gen_project import BaseHookSystemCalls, PostGenPoetrySetup


class TestPostGenPoetrySetup(TestCase):
    """Test the PostGenPoetrySetup class."""

    def setUp(self) -> None:
        self.instance = PostGenPoetrySetup()

    def test_initialize__has_correct_properties(self) -> None:
        self.assertIsInstance(self.instance, BaseHookSystemCalls)
        self.assertEqual(
            self.instance.poetry_lock_command,
            "poetry lock",
        )
        self.assertEqual(
            self.instance.poetry_install_command,
            "poetry install",
        )

    @patch.dict(os.environ, {}, clear=True)
    def test_condition__no_env__true(self) -> None:
        self.assertTrue(self.instance.condition())

    @patch.dict(os.environ, {"TEMPLATE_SKIP_POETRY": "0"}, clear=True)
    def test_condition__non_1_env__false(self) -> None:
        self.assertTrue(self.instance.condition())

    @patch.dict(os.environ, {"TEMPLATE_SKIP_POETRY": "1"}, clear=True)
    def test_condition__env_1__false(self) -> None:
        self.assertFalse(self.instance.condition())

    @patch("os.system")
    def test_hook__correct_system_calls(self, m_system: Mock) -> None:
        m_system.return_value = 1

        self.instance.hook()

        m_system.mock_calls = [
            call(self.instance.poetry_lock_command),
            call(self.instance.poetry_install_command)
        ]
