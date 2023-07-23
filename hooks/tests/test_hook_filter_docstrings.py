"""Test the PostGenDocstringFilter class."""

from unittest.mock import patch

from hooks import post_gen_project
from hooks.post_gen_project import BaseHookFilter, PostGenDocstringFilter


class TestPostGenDocstringFilter:
    """Test the PostGenDocstringFilter class."""

    def test_instance__when_initialized__has_correct_inheritance(
        self,
        docstring_filter: PostGenDocstringFilter,
    ) -> None:
        assert isinstance(docstring_filter, BaseHookFilter)
        assert isinstance(docstring_filter, PostGenDocstringFilter)

    def test_instance__when_initialized__has_correct_properties(
        self,
        docstring_filter: PostGenDocstringFilter,
    ) -> None:
        assert docstring_filter.excluded == [
            ".pydocstyle",
            ".pydocstyle.tests",
        ]

    def test_condition__when_docstrings_enabled__false(
        self,
        docstring_filter: PostGenDocstringFilter,
    ) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_docstrings = "true"

            assert docstring_filter.condition() is False

    def test_condition__when_docstrings_enabled__true(
        self,
        docstring_filter: PostGenDocstringFilter,
    ) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_docstrings = "false"

            assert docstring_filter.condition() is True
