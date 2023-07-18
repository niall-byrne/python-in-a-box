"""Test the Template class."""

from unittest import TestCase

from ..post_gen_project import Template


class TestTemplate(TestCase):
    """Test the Template class."""

    def setUp(self) -> None:
        self.instance = Template()

    def test_initialize__has_correct_properties(self) -> None:
        self.assertEqual(
            self.instance.option_base_branch_name,
            "{{cookiecutter.git_base_branch}}",
        )
        self.assertEqual(
            self.instance.option_docstrings,
            "{{cookiecutter.optional_docstring_linting}}",
        )
        self.assertEqual(
            self.instance.option_formatting_type,
            "{{cookiecutter.formatting}}",
        )
        self.assertEqual(
            self.instance.option_sphinx,
            "{{cookiecutter.optional_sphinx_support}}",
        )
        self.assertEqual(
            self.instance.option_project_slug,
            "{{cookiecutter.project_slug}}",
        )
