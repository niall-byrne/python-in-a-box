"""Test the PostGenGitSetup class."""

import os
from typing import List
from unittest import TestCase
from unittest.mock import Mock, call, patch

from .. import post_gen_project
from ..post_gen_project import BaseHookSystemCalls, PostGenGitSetup


class TestPostGenGitSetup(TestCase):
    """Test the PostGenGitSetup class."""

    def expected_system_calls(self) -> List[str]:
        return [
            "git init",
            "git stage .",
            "git branch -m {name}".format(
                name=self.instance.git_default_branch_name
            ),
            "git commit -m '{message}'".format(
                message=self.instance.git_initial_commit_message
            ),
            "git checkout -b {name}".format(
                name=self.instance.git_dev_branch_name
            ),
            "git checkout {name}".format(
                name=self.instance.git_default_branch_name
            ),
        ]

    def setUp(self) -> None:
        self.instance = PostGenGitSetup()

    def test_initialize__has_correct_properties(self) -> None:
        self.assertIsInstance(self.instance, BaseHookSystemCalls)
        self.assertEqual(
            self.instance.git_initial_commit_message,
            "build(COOKIECUTTER): Initial Generation",
        )
        self.assertEqual(
            self.instance.git_root_folder,
            ".git",
        )
        self.assertEqual(
            self.instance.git_default_branch_name,
            "{{cookiecutter.git_base_branch}}",
        )
        self.assertEqual(
            self.instance.git_dev_branch_name,
            "{{cookiecutter.git_dev_branch}}",
        )

    @patch.dict(os.environ, {}, clear=True)
    def test_condition__no_existing_git__no_env__true(self) -> None:
        with patch("os.path.exists", Mock(return_value=False)):
            self.assertTrue(self.instance.condition())

    @patch.dict(os.environ, {}, clear=True)
    def test_condition__existing_git__no_env__false(self) -> None:
        with patch("os.path.exists", Mock(return_value=True)):
            self.assertFalse(self.instance.condition())

    @patch.dict(os.environ, {"TEMPLATE_SKIP_GIT_INIT": "0"}, clear=True)
    def test_condition__no_existing_git__non_1_env__true(self) -> None:
        with patch("os.path.exists", Mock(return_value=False)):
            self.assertTrue(self.instance.condition())

    @patch.dict(os.environ, {"TEMPLATE_SKIP_GIT_INIT": "0"}, clear=True)
    def test_condition__existing_git__non_1_env__false(self) -> None:
        with patch("os.path.exists", Mock(return_value=True)):
            self.assertFalse(self.instance.condition())

    @patch.dict(os.environ, {"TEMPLATE_SKIP_GIT_INIT": "1"}, clear=True)
    def test_condition__no_existing_git__env_1__false(self) -> None:
        with patch("os.path.exists", Mock(return_value=False)):
            self.assertFalse(self.instance.condition())

    @patch.dict(os.environ, {"TEMPLATE_SKIP_GIT_INIT": "1"}, clear=True)
    def test_condition__existing_git__env_1__false(self) -> None:
        with patch("os.path.exists", Mock(return_value=True)):
            self.assertFalse(self.instance.condition())

    @patch("os.system")
    def test_hook__correct_system_calls(self, m_system: Mock) -> None:
        m_system.return_value = 1
        expected_calls = list(map(call, self.expected_system_calls()))

        with patch(post_gen_project.__name__ + ".Template") as m_template:
            m_template.option_base_branch_name = (
                self.instance.git_default_branch_name
            )
            self.instance.hook()

        m_system.assert_has_calls(expected_calls)
