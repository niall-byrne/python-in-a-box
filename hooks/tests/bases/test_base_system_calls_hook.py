"""Test the BaseHookSystemCalls class."""

from unittest.mock import Mock, patch

from hooks.post_gen_project import BaseHook, BaseHookSystemCalls

from .fixtures.concrete_base_system_call_hook import \
    ConcreteBaseHookSystemCalls


class TestBaseHook:
    """Test the BaseHookSystemCalls class."""

    def test_instance__when_initialized__has_correct_inheritance(
        self,
        concrete_base_system_call_hook: ConcreteBaseHookSystemCalls,
    ) -> None:
        assert isinstance(concrete_base_system_call_hook, BaseHook)
        assert isinstance(concrete_base_system_call_hook, BaseHookSystemCalls)

    @patch("os.system")
    @patch("sys.exit")
    def test_system_call__zero_exit_code__does_not_terminate(
        self,
        m_exit: Mock,
        m_system: Mock,
        concrete_base_system_call_hook: ConcreteBaseHookSystemCalls,
    ) -> None:
        test_command = "fly away and never come back"
        m_system.return_value = 1

        concrete_base_system_call_hook.system_call(test_command)

        m_system.assert_called_once_with(test_command)
        m_exit.assert_not_called()

    @patch("os.system")
    @patch("sys.exit")
    def test_system_call__non_zero_exit_code__terminates(
        self,
        m_exit: Mock,
        m_system: Mock,
        concrete_base_system_call_hook: ConcreteBaseHookSystemCalls,
    ) -> None:
        test_command = "just got back remember me"
        m_system.return_value = 256 * 2

        concrete_base_system_call_hook.system_call(test_command)

        m_system.assert_called_once_with(test_command)
        m_exit.assert_called_once_with(2)
