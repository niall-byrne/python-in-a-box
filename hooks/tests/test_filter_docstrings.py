"""Test the PostGenDocstringFilter class."""

from unittest import TestCase
from unittest.mock import patch

from .. import post_gen_project
from ..post_gen_project import BaseHookFilter, PostGenDocstringFilter


class TestPostGenDocstringFilter(TestCase):
    """Test the PostGenDocstringFilter class."""

    def setUp(self) -> None:
        self.instance = PostGenDocstringFilter()

    def test_initialize(self) -> None:
        self.assertIsInstance(self.instance, BaseHookFilter)
        self.assertListEqual(
            self.instance.excluded,
            [".pydocstyle", ".pydocstyle.tests"],
        )

    def test_condition_false(self) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_docstrings = "true"
            self.assertFalse(self.instance.condition())

    def test_condition_true(self) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_docstrings = "false"
            self.assertTrue(self.instance.condition())
