"""Test the PostGenGitSetup class."""

import os
import re
from unittest import TestCase
from unittest.mock import Mock, call, mock_open, patch

from .. import post_gen_project
from ..post_gen_project import BaseHookSystemCalls, PostGen2SpaceFormattingSetup


class TestPostGenGitSetup(TestCase):
    """Test the PostGenGitSetup class."""

    def setUp(self) -> None:
        self.instance = PostGen2SpaceFormattingSetup()
        self.mock_filename = "test.py"
        self.mock_indent_content = "    indent"
        self.file_mock = mock_open(read_data=self.mock_indent_content)

    def test_initialize__has_correct_properties(self) -> None:
        self.assertIsInstance(
            self.instance,
            BaseHookSystemCalls,
        )
        self.assertEqual(
            self.instance.formatting_option,
            "Niall's 2-Space Preference",
        )

    @patch.dict(os.environ, {}, clear=True)
    def test_condition__no_env__true(self) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_formatting_type = self.instance.formatting_option
            self.assertTrue(self.instance.condition())

    @patch.dict(os.environ, {"TEMPLATE_SKIP_FMT_INIT": "0"}, clear=True)
    def test_condition__non_1_env__true(self) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_formatting_type = self.instance.formatting_option
            self.assertTrue(self.instance.condition())

    @patch.dict(os.environ, {}, clear=True)
    def test_condition__another_format__false(self) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_formatting_type = "unknown format"
            self.assertNotEqual(
                self.instance.formatting_option,
                m_template.option_formatting_type,
            )
            self.assertFalse(self.instance.condition())

    @patch.dict(os.environ, {"TEMPLATE_SKIP_FMT_INIT": "1"}, clear=True)
    def test_condition__env_1__false(self) -> None:
        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_formatting_type = self.instance.formatting_option
            self.assertFalse(self.instance.condition())

    @patch("os.walk")
    @patch("os.getcwd")
    def test_find_python_files__expected_value(
        self, m_cwd: Mock, m_walk: Mock
    ) -> None:
        m_cwd.return_value = "/test/folder"
        m_walk.return_value = [
            ("/one", [], ["text.txt", "python.py"]),
            ("/two", [], ["text.txt", "python.py"])
        ]
        result = self.instance.find_python_files()

        m_walk.assert_called_once_with(m_cwd.return_value)
        self.assertListEqual(
            result, [
                os.path.join("/one", "python.py"),
                os.path.join("/two", "python.py"),
            ]
        )

    def test_hook__applies_format_to_all_python_files(self) -> None:
        with patch.object(self.instance, "format") as m_format:
            with patch.object(self.instance, "find_python_files") as m_find:
                m_find.return_value = ["/app/python.py"]
                self.instance.hook()

        m_format.assert_has_calls(list(map(call, m_find.return_value)))

    @patch("os.system")
    @patch("importlib.import_module")
    def test_format__reads_and_writes_expected_files(
        self,
        _: Mock,
        m_system: Mock,
    ) -> None:
        m_system.return_value = 1

        with patch("builtins.open", self.file_mock) as m_open:
            self.instance.format(self.mock_filename)

        m_open.assert_any_call(self.mock_filename, "r", encoding="utf-8")
        m_open.assert_any_call(self.mock_filename, "w", encoding="utf-8")
        file_handle = m_open.return_value.__enter__.return_value

        file_handle.write.assert_called_once_with(
            re.sub(r'    ', '  ', self.mock_indent_content)
        )

    @patch("os.system")
    @patch("importlib.import_module")
    def test_format__when_yapf_installed__calls_yapf(
        self,
        m_import: Mock,
        m_system: Mock,
    ) -> None:
        m_system.return_value = 1

        with patch("builtins.open", self.file_mock):
            self.instance.format(self.mock_filename)

        m_import.assert_called_once_with("yapf")
        m_system.assert_called_once_with(
            "yapf -i {file_path}".format(file_path=self.mock_filename)
        )

    @patch("os.system")
    @patch("importlib.import_module")
    def test_format__when_yapf_not_found__best_effort_only(
        self,
        m_import: Mock,
        m_system: Mock,
    ) -> None:
        m_system.return_value = 1
        m_import.side_effect = ModuleNotFoundError
        mock_filename = "test.py"
        mock_content = "    indent"

        with patch("builtins.open", mock_open(read_data=mock_content)):
            self.instance.format(mock_filename)

        m_import.assert_called_once_with("yapf")
        m_system.assert_not_called()
