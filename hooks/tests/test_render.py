"""Test the main function."""

from unittest import TestCase
from unittest.mock import DEFAULT, Mock, call, patch

from .. import post_gen_project
from ..post_gen_project import main

mock_base_hook_execute = Mock()


@patch(post_gen_project.__name__ + ".BaseHook.execute", mock_base_hook_execute)
class TestTemplate(TestCase):
    """Test the main function."""

    def setUp(self):
        mock_base_hook_execute.reset_mock()

    def test_base_hook_execute__call_count(self) -> None:
        main()

        assert mock_base_hook_execute.call_count == 6

    def test_base_hook_execute__call_sequence(self) -> None:
        expected_calls = [
            getattr(call, f"execute{counter}")() for counter in range(0, 6)
        ]
        mock_manager = Mock()
        with patch.multiple(
            post_gen_project.__name__,
            PostGen2SpaceFormattingSetup=DEFAULT,
            PostGenPoetrySetup=DEFAULT,
            PostGenGitSetup=DEFAULT,
            PostGenPrecommitSetup=DEFAULT,
            PostGenDocstringFilter=DEFAULT,
            PostGenSphinxFilter=DEFAULT,
        ) as mock_classes:
            for sequence, mock_class in enumerate(mock_classes.values()):
                mock_manager.attach_mock(
                    mock_class.return_value.execute, f"execute{sequence}"
                )

            main()

        assert mock_manager.mock_calls == expected_calls

    @patch(post_gen_project.__name__ + ".PostGenSphinxFilter.execute")
    def test_render__calls_sphinx_filter(self, m_sphinx_filter: Mock) -> None:
        main()

        m_sphinx_filter.assert_called_once()

    @patch(post_gen_project.__name__ + ".PostGenDocstringFilter.execute")
    def test_render__calls_docstring_filter(
        self, m_docstring_filter: Mock
    ) -> None:
        main()

        m_docstring_filter.assert_called_once()

    @patch(post_gen_project.__name__ + ".PostGenPrecommitSetup.execute")
    def test_render__calls_docstring_setup(
        self, m_precommit_setup: Mock
    ) -> None:
        main()

        m_precommit_setup.assert_called_once()

    @patch(post_gen_project.__name__ + ".PostGenGitSetup.execute")
    def test_render__calls_git_setup(self, m_git_setup: Mock) -> None:
        main()

        m_git_setup.assert_called_once()

    @patch(post_gen_project.__name__ + ".PostGenPoetrySetup.execute")
    def test_render__calls_poetry_setup(self, m_poetry_setup: Mock) -> None:
        main()

        m_poetry_setup.assert_called_once()

    @patch(post_gen_project.__name__ + ".PostGen2SpaceFormattingSetup.execute")
    def test_render__calls_formatting_setup(
        self, m_formatting_setup: Mock
    ) -> None:
        main()

        m_formatting_setup.assert_called_once()
