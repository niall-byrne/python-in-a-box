"""Test the PostGenDocstringFilter class."""

from unittest import TestCase
from unittest.mock import patch

from .. import post_gen_project
from ..post_gen_project import BaseHookFilter, PostGenSphinxFilter


class TestPostGenDocstringFilter(TestCase):
    """Test the PostGenDocstringFilter class."""

    def setUp(self) -> None:
        self.instance = PostGenSphinxFilter()

    def test_initialize(self) -> None:
        self.assertIsInstance(self.instance, BaseHookFilter)
        self.assertListEqual(
            self.instance.excluded,
            [".darglint", ".readthedocs.yml", "documentation"],
        )

    def test_condition_false(self) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_sphinx = "true"
            self.assertFalse(self.instance.condition())

    def test_condition_true(self) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_sphinx = "false"
            self.assertTrue(self.instance.condition())
