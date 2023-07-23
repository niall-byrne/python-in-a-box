"""Test the PostGenSphinxFilter class."""

from unittest.mock import patch

from hooks import post_gen_project
from hooks.post_gen_project import BaseHookFilter, PostGenSphinxFilter


class TestPostGenSphinxFilter:
    """Test the PostGenSphinxFilter class."""

    def test_instance__when_initialized__has_correct_inheritance(
        self,
        sphinx_filter: PostGenSphinxFilter,
    ) -> None:
        assert isinstance(sphinx_filter, BaseHookFilter)
        assert isinstance(sphinx_filter, PostGenSphinxFilter)

    def test_instance__when_initialized__has_correct_properties(
        self,
        sphinx_filter: PostGenSphinxFilter,
    ) -> None:
        assert sphinx_filter.excluded == [
            ".darglint",
            ".readthedocs.yml",
            "documentation",
        ]

    def test_condition__when_sphinx_enabled__false(
        self,
        sphinx_filter: PostGenSphinxFilter,
    ) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_sphinx = "true"

            assert sphinx_filter.condition() is False

    def test_condition__when_sphinx_disabled__true(
        self,
        sphinx_filter: PostGenSphinxFilter,
    ) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_sphinx = "false"

            assert sphinx_filter.condition() is True
