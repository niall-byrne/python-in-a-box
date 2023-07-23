"""Test the PostGen2SpaceFormattingSetup class."""

import os
import re
from unittest.mock import DEFAULT, Mock, call, mock_open, patch

import pytest

from hooks import post_gen_project
from hooks.post_gen_project import (BaseHookSystemCalls,
                                    PostGen2SpaceFormattingSetup)


class TestPostGen2SpaceFormattingSetup:
    """Test the PostGen2SpaceFormattingSetup class."""

    def test_instance__when_initialized__has_correct_inheritance(
        self,
        formatting_setup_hook: PostGen2SpaceFormattingSetup,
    ) -> None:
        assert isinstance(formatting_setup_hook, BaseHookSystemCalls)
        assert isinstance(formatting_setup_hook, PostGen2SpaceFormattingSetup)

    def test_instance__when_initialized__has_correct_properties(
        self,
        formatting_setup_hook: PostGen2SpaceFormattingSetup,
    ) -> None:
        assert formatting_setup_hook.formatting_option == \
               "Niall's 2-Space Preference"

    @pytest.mark.parametrize(
        "env,formatting_type,expected", [
            [
                {},
                PostGen2SpaceFormattingSetup.formatting_option,
                True,
            ],
            [
                {},
                "unknown",
                False,
            ],
            [
                {
                    "TEMPLATE_SKIP_FMT_INIT": "0"
                },
                PostGen2SpaceFormattingSetup.formatting_option,
                True,
            ],
            [
                {
                    "TEMPLATE_SKIP_FMT_INIT": "0"
                },
                "unknown",
                False,
            ],
            [
                {
                    "TEMPLATE_SKIP_FMT_INIT": "1"
                },
                PostGen2SpaceFormattingSetup.formatting_option,
                False,
            ],
            [
                {
                    "TEMPLATE_SKIP_FMT_INIT": "1",
                },
                "unknown",
                False,
            ],
        ]
    )
    def test_condition__with_parametrized_scenario__returns_expected(
        self,
        env: dict,
        formatting_type: str,
        expected: bool,
        formatting_setup_hook: PostGen2SpaceFormattingSetup,
    ) -> None:
        with patch.dict(os.environ, env, clear=True):
            with patch(post_gen_project.__name__ + ".Template") as m_template:
                m_template.option_formatting_type = formatting_type

                assert formatting_setup_hook.condition() == expected

    @patch("os.walk")
    @patch("os.getcwd")
    def test_find_python_files__when_called__expected_result(
        self,
        m_cwd: Mock,
        m_walk: Mock,
        formatting_setup_hook: PostGen2SpaceFormattingSetup,
    ) -> None:
        m_cwd.return_value = "/test/folder"
        m_walk.return_value = [
            ("/one", [], ["text.txt", "python.py"]),
            ("/two", [], ["text.txt", "python.py"])
        ]

        result = formatting_setup_hook.find_python_files()

        m_walk.assert_called_once_with(m_cwd.return_value)
        assert result == [
            os.path.join("/one", "python.py"),
            os.path.join("/two", "python.py"),
        ]

    def test_hook__when_called__formats_all_python_files(
        self,
        formatting_setup_hook: PostGen2SpaceFormattingSetup,
    ) -> None:
        with patch.multiple(
            formatting_setup_hook,
            format=DEFAULT,
            find_python_files=DEFAULT,
        ) as m_instance:
            m_instance['find_python_files'].return_value = ["one.py", "two.py"]

            formatting_setup_hook.hook()

        assert m_instance['format'].call_args_list == list(
            map(call, m_instance['find_python_files'].return_value)
        )

    @patch("os.system")
    @patch("importlib.import_module")
    def test_format__when_called__has_correct_file_operations(
        self,
        _: Mock,
        m_system: Mock,
        formatting_setup_hook: PostGen2SpaceFormattingSetup,
    ) -> None:
        m_system.return_value = 1
        mock_filename = "test.py"

        with patch("builtins.open", new_callable=mock_open) as m_open:
            formatting_setup_hook.format(mock_filename)

        assert m_open.call_args_list == [
            call(mock_filename, "r", encoding="utf-8"),
            call(mock_filename, "w", encoding="utf-8"),
        ]

    @patch("os.system")
    @patch("importlib.import_module")
    def test_format__when_file_has_wrong_ident__transforms_idents(
        self,
        _: Mock,
        m_system: Mock,
        formatting_setup_hook: PostGen2SpaceFormattingSetup,
    ) -> None:
        m_system.return_value = 1
        mock_filename = "test.py"
        mock_indent_content = "    indent"

        with patch(
            "builtins.open",
            new_callable=mock_open,
            read_data=mock_indent_content
        ) as m_open:
            formatting_setup_hook.format(mock_filename)

        file_handle = m_open.return_value.__enter__.return_value
        file_handle.write.assert_called_once_with(
            re.sub(r'    ', '  ', mock_indent_content)
        )

    @patch("os.system")
    @patch("importlib.import_module")
    def test_format__when_yapf_installed__calls_yapf(
        self,
        m_import: Mock,
        m_system: Mock,
        formatting_setup_hook: PostGen2SpaceFormattingSetup,
    ) -> None:
        m_system.return_value = 1
        mock_filename = "test.py"

        with patch("builtins.open", new_callable=mock_open):
            formatting_setup_hook.format(mock_filename)

        m_import.assert_called_once_with("yapf")
        m_system.assert_called_once_with(
            "yapf -i {file_path}".format(file_path=mock_filename)
        )

    @patch("os.system")
    @patch("importlib.import_module")
    def test_format__when_yapf_not_found__does_not_call_yapf(
        self,
        m_import: Mock,
        m_system: Mock,
        formatting_setup_hook: PostGen2SpaceFormattingSetup,
    ) -> None:
        m_system.return_value = 1
        m_import.side_effect = ModuleNotFoundError
        mock_filename = "test.py"

        with patch("builtins.open", new_callable=mock_open):
            formatting_setup_hook.format(mock_filename)

        m_import.assert_called_once_with("yapf")
        m_system.assert_not_called()
