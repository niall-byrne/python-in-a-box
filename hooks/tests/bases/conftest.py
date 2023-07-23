"""Test fixtures for hook tests."""

import pytest

from .fixtures.concrete_base_hook import ConcreteBaseHook
from .fixtures.concrete_base_system_call_hook import \
    ConcreteBaseHookSystemCalls
from .fixtures.concrete_filter_hook import ConcreteBaseHookFilter


@pytest.fixture
def concrete_base_hook() -> ConcreteBaseHook:
    return ConcreteBaseHook()


@pytest.fixture
def concrete_base_filter_hook() -> ConcreteBaseHookFilter:
    return ConcreteBaseHookFilter()


@pytest.fixture
def concrete_base_system_call_hook() -> ConcreteBaseHookSystemCalls:
    return ConcreteBaseHookSystemCalls()
