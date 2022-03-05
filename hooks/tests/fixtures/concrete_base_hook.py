"""ConcreteBaseHook class."""

from unittest.mock import Mock

from ...post_gen_project import BaseHook


class ConcreteBaseHook(BaseHook):
    """Concrete test implementation of BaseHook."""

    hook_called = Mock()
    condition_value = True

    def condition(self) -> bool:
        return self.condition_value

    def hook(self) -> None:
        self.hook_called()
