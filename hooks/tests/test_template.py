"""Test the Template class."""

from hooks.post_gen_project import Template


class TestTemplate:
    """Test the Template class."""

    def test_instance__when_initialized__has_correct_properties(
        self,
        template: Template,
    ) -> None:
        assert template.option_base_branch_name == \
            "{{cookiecutter.git_base_branch}}"

        assert template.option_docstrings == \
            "{{cookiecutter.optional_docstring_linting}}"

        assert template.option_formatting_type == \
            "{{cookiecutter.formatting}}"

        assert template.option_sphinx == \
            "{{cookiecutter.optional_sphinx_support}}"

        assert template.option_project_slug == \
            "{{cookiecutter.project_slug}}"
