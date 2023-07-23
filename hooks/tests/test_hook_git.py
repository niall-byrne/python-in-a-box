"""Test the PostGenGitSetup class."""

import os
from unittest.mock import Mock, call, patch

import pytest

from hooks.post_gen_project import BaseHookSystemCalls, PostGenGitSetup


class TestPostGenGitSetup:
    """Test the PostGenGitSetup class."""

    def test_instance__when_initialized__has_correct_inheritance(
        self,
        git_setup_hook: PostGenGitSetup,
    ) -> None:
        assert isinstance(git_setup_hook, BaseHookSystemCalls)
        assert isinstance(git_setup_hook, PostGenGitSetup)

    def test_instance__when_initialized__has_correct_properties(
        self,
        git_setup_hook: PostGenGitSetup,
    ) -> None:
        assert git_setup_hook.git_initial_commit_message == \
               "build(COOKIECUTTER): Initial Generation"
        assert git_setup_hook.git_root_folder == \
               ".git"
        assert git_setup_hook.git_default_branch_name == \
               "{{cookiecutter.git_base_branch}}"
        assert git_setup_hook.git_dev_branch_name == \
               "{{cookiecutter.git_dev_branch}}"

    @pytest.mark.parametrize(
        "env,root_exists,expected", [
            [{}, False, True],
            [{}, True, False],
            [{}, True, False],
            [{
                "TEMPLATE_SKIP_GIT_INIT": "0"
            }, False, True],
            [{
                "TEMPLATE_SKIP_GIT_INIT": "0"
            }, True, False],
            [{
                "TEMPLATE_SKIP_GIT_INIT": "1"
            }, False, False],
            [{
                "TEMPLATE_SKIP_GIT_INIT": "1"
            }, True, False],
        ]
    )
    def test_condition__with_parametrized_scenario__returns_expected(
        self,
        env: dict,
        root_exists: bool,
        expected: bool,
        git_setup_hook: PostGenGitSetup,
    ) -> None:
        with patch.dict(os.environ, env, clear=True):
            with patch("os.path.exists", Mock(return_value=root_exists)):
                assert git_setup_hook.condition() == expected

    @patch("os.system")
    def test_hook__when_called__has_correct_system_calls(
        self,
        m_system: Mock,
        git_setup_hook: PostGenGitSetup,
    ) -> None:
        m_system.return_value = 1
        expected_calls = [
            "git init",
            "git stage .",
            "git branch -m {name}".format(
                name=git_setup_hook.git_default_branch_name
            ),
            "git commit -m '{message}'".format(
                message=git_setup_hook.git_initial_commit_message
            ),
            "git checkout -b {name}".format(
                name=git_setup_hook.git_dev_branch_name
            ),
            "git checkout {name}".format(
                name=git_setup_hook.git_default_branch_name
            ),
        ]

        git_setup_hook.hook()

        assert m_system.call_args_list == list(map(call, expected_calls))
