"""Test the main function."""

from typing import ContextManager
from unittest.mock import Mock, call

import pytest

from hooks.post_gen_project import main

HooksContextType = ContextManager[dict]


class TestTemplate:
    """Test the main function."""

    def test_base_hook_execute__when_main_called__call_count(
        self,
        m_base_class_execute: Mock,
    ) -> None:

        main()

        assert m_base_class_execute.call_count == 6

    def test_base_hook_execute__when_main_called__hook_class_sequence(
        self,
        patch_hooks_context: HooksContextType,
    ) -> None:
        expected_calls = [
            getattr(call, f"execute{counter}")() for counter in range(0, 6)
        ]
        mock_manager = Mock()
        with patch_hooks_context as mock_classes:
            for sequence, mock_class in enumerate(mock_classes.values()):
                mock_manager.attach_mock(
                    mock_class.return_value.execute, f"execute{sequence}"
                )

            main()

        assert mock_manager.mock_calls == expected_calls

    @pytest.mark.parametrize(
        "class_name", [
            "PostGen2SpaceFormattingSetup",
            "PostGenPoetrySetup",
            "PostGenGitSetup",
            "PostGenPrecommitSetup",
            "PostGenDocstringFilter",
            "PostGenSphinxFilter",
        ]
    )
    def test_render__when_given_a_class_name_and_main_called__calls_execute(
        self,
        patch_hooks_context: HooksContextType,
        class_name: str,
    ) -> None:
        with patch_hooks_context as mock_classes:
            main()

        mock_classes[class_name].return_value.execute.assert_called_once()
