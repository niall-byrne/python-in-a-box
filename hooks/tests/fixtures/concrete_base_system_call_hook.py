"""ConcreteBaseHookSystemCalls class."""

from ...post_gen_project import BaseHookSystemCalls


class ConcreteBaseHookSystemCalls(BaseHookSystemCalls):
    """Concrete test implementation of BaseHookSystemCalls."""

    condition_value = True

    def condition(self) -> bool:
        return self.condition_value

    def hook(self) -> None:
        raise NotImplementedError
