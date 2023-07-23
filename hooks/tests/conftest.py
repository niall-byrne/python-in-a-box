"""Test fixtures for hook tests."""

from typing import ContextManager
from unittest.mock import DEFAULT, Mock, patch

import pytest

from hooks import post_gen_project


@pytest.fixture
def patch_hooks_context() -> ContextManager[dict]:  # type: ignore[misc]
    yield patch.multiple(
        post_gen_project,
        PostGen2SpaceFormattingSetup=DEFAULT,
        PostGenPoetrySetup=DEFAULT,
        PostGenGitSetup=DEFAULT,
        PostGenPrecommitSetup=DEFAULT,
        PostGenDocstringFilter=DEFAULT,
        PostGenSphinxFilter=DEFAULT,
    )


@pytest.fixture
def m_base_class_execute(monkeypatch: pytest.MonkeyPatch) -> Mock:
    m_base_class_method = Mock()
    monkeypatch.setattr(
        post_gen_project.BaseHook, "execute", m_base_class_method
    )
    return m_base_class_method


@pytest.fixture
def docstring_filter() -> post_gen_project.PostGenDocstringFilter:
    return post_gen_project.PostGenDocstringFilter()


@pytest.fixture
def sphinx_filter() -> post_gen_project.PostGenSphinxFilter:
    return post_gen_project.PostGenSphinxFilter()


@pytest.fixture
def formatting_setup_hook() -> post_gen_project.PostGen2SpaceFormattingSetup:
    return post_gen_project.PostGen2SpaceFormattingSetup()


@pytest.fixture
def git_setup_hook() -> post_gen_project.PostGenGitSetup:
    return post_gen_project.PostGenGitSetup()


@pytest.fixture
def poetry_setup_hook() -> post_gen_project.PostGenPoetrySetup:
    return post_gen_project.PostGenPoetrySetup()


@pytest.fixture
def precommit_setup_hook() -> post_gen_project.PostGenPrecommitSetup:
    return post_gen_project.PostGenPrecommitSetup()


@pytest.fixture
def template() -> post_gen_project.Template:
    return post_gen_project.Template()
