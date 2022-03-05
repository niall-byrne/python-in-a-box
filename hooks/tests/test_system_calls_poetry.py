"""Test the PostGenPoetrySetup class."""

import os
from unittest import TestCase
from unittest.mock import Mock, patch

from ..post_gen_project import BaseHookSystemCalls, PostGenPoetrySetup


class TestPostGenPoetrySetup(TestCase):
    """Test the PostGenPoetrySetup class."""

    def setUp(self) -> None:
        self.instance = PostGenPoetrySetup()

    def test_initialize(self) -> None:
        self.assertIsInstance(self.instance, BaseHookSystemCalls)
        self.assertEqual(
            self.instance.poetry_setup_command,
            "poetry lock",
        )

    @patch.dict(os.environ, {}, clear=True)
    def test_condition_true(self) -> None:
        self.assertTrue(self.instance.condition())

    @patch.dict(os.environ, {"PIB_SKIP_POETRY_INIT": "1"}, clear=True)
    def test_condition_false_env_var(self) -> None:
        self.assertFalse(self.instance.condition())

    @patch("os.system")
    def test_hook(self, m_system: Mock) -> None:
        m_system.return_value = 1

        self.instance.hook()

        m_system.assert_called_once_with(self.instance.poetry_setup_command)
