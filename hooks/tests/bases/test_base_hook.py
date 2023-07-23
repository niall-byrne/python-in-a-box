"""Test the BaseHook class."""

from hooks.post_gen_project import BaseHook

from .fixtures.concrete_base_hook import ConcreteBaseHook


class TestBaseHook:
    """Test the BaseHook class."""

    def test_instance__when_initialized__has_correct_inheritance(
        self,
        concrete_base_hook: ConcreteBaseHook,
    ) -> None:
        assert isinstance(concrete_base_hook, BaseHook)

    def test_execute__when_condition_is_true__is_called(
        self,
        concrete_base_hook: ConcreteBaseHook,
    ) -> None:
        concrete_base_hook.condition_value = True

        concrete_base_hook.execute()

        concrete_base_hook.hook_called.assert_called_once_with()

    def test_execute__when_condition_is_false__is_not_called(
        self,
        concrete_base_hook: ConcreteBaseHook,
    ) -> None:
        concrete_base_hook.condition_value = False

        concrete_base_hook.execute()

        concrete_base_hook.hook_called.assert_not_called()
