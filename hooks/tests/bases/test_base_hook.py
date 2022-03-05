"""Test the BaseHook class."""

from unittest import TestCase

from ...post_gen_project import BaseHook
from ..fixtures.concrete_base_hook import ConcreteBaseHook


class TestBaseHook(TestCase):
    """Test the BaseHook class."""

    def setUp(self) -> None:
        self.instance = ConcreteBaseHook()

    def test_instantiate(self) -> None:
        self.assertIsInstance(self.instance, BaseHook)

    def test_execute_true(self) -> None:
        self.instance.condition_value = True
        self.instance.execute()
        self.instance.hook_called.assert_called_once_with()

    def test_execute_false(self) -> None:
        self.instance.condition_value = False
        self.instance.execute()
        self.instance.hook_called.assert_not_called()
