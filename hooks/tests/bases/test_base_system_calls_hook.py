"""Test the BaseHookSystemCalls class."""

from unittest import TestCase
from unittest.mock import Mock, patch

from ...post_gen_project import BaseHook, BaseHookSystemCalls
from ..fixtures.concrete_base_system_call_hook import (
    ConcreteBaseHookSystemCalls,
)


class TestBaseHook(TestCase):
    """Test the BaseHookSystemCalls class."""

    def setUp(self) -> None:
        self.instance = ConcreteBaseHookSystemCalls()

    def test_instantiate(self) -> None:
        self.assertIsInstance(self.instance, BaseHook)
        self.assertIsInstance(self.instance, BaseHookSystemCalls)

    @patch("os.system")
    @patch("sys.exit")
    def test_system_call_zero_code(self, m_exit: Mock, m_system: Mock) -> None:
        test_command = "fly away and never come back"
        m_system.return_value = 1

        self.instance.system_call(test_command)

        m_system.assert_called_once_with(test_command)
        m_exit.assert_not_called()

    @patch("os.system")
    @patch("sys.exit")
    def test_system_call_non_zero_code(
        self, m_exit: Mock, m_system: Mock
    ) -> None:
        test_command = "just got back remember me"
        m_system.return_value = 256 * 2

        self.instance.system_call(test_command)

        m_system.assert_called_once_with(test_command)
        m_exit.assert_called_once_with(2)
