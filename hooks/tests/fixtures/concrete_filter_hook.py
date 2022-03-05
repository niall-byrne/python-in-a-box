"""ConcreteBaseHookFilter class."""

from ...post_gen_project import BaseHookFilter


class ConcreteBaseHookFilter(BaseHookFilter):
    """Concrete test implementation of BaseHookFilter."""

    condition_value = True
    excluded = ["one", "two", "three"]

    def condition(self) -> bool:
        return self.condition_value
