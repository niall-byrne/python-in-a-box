"""Template post-generation hooks."""

# Environment Variable Overrides:
# TEMPLATE_SKIP_FMT_INIT:
#           Optionally set to 1 to skip the initial code formatting.
# TEMPLATE_SKIP_GIT_INIT:
#           Optionally set to 1 to skip creating branches and initial commit.
# TEMPLATE_SKIP_POETRY:
#           Optionally set to 1 to skip installing dependencies.
# TEMPLATE_SKIP_PRECOMMIT:
#           Optionally set to 1 to skip installing pre-commit hooks.

import abc
import importlib
import os
import re
import shutil
import sys
from typing import List


class BaseHook(abc.ABC):
    """Base post-generation Cookiecutter hook."""

    def execute(self) -> None:
        """Execute the selected hook conditionally."""
        if self.condition():
            self.hook()

    @abc.abstractmethod
    def condition(self) -> bool:
        """Evaluate a condition to run the hook."""

    @abc.abstractmethod
    def hook(self) -> None:
        """Execute the actual hook."""


class BaseHookSystemCalls(BaseHook, abc.ABC):
    """Base post-generation Cookiecutter hook with system calls."""

    def system_call(self, command: str) -> None:
        """Execute a system call, and propagate the error code appropriately."""
        result = os.system(command)  # nosec
        exit_code = int(result / 256)
        if exit_code:
            sys.exit(exit_code)


class BaseHookFilter(BaseHook, abc.ABC):
    """Base post-generation Cookiecutter hook with filesystem content filter."""

    excluded: List[str]

    def hook(self) -> None:
        """Remove the specified files or folders."""
        for file_path in self.excluded:
            self._remove(file_path)

    def _remove(self, file_path: str) -> None:
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            if os.path.isfile(file_path):
                os.remove(file_path)


class Template:
    """Template values from the end-user."""

    option_base_branch_name = "{{cookiecutter.git_base_branch}}"
    option_dev_branch_name = "{{cookiecutter.git_dev_branch}}"
    option_docstrings = "{{cookiecutter.optional_docstring_linting}}"
    option_formatting_type = "{{cookiecutter.formatting}}"
    option_project_slug = "{{cookiecutter.project_slug}}"
    option_sphinx = "{{cookiecutter.optional_sphinx_support}}"


def main() -> None:
    """Call all post-generation Cookiecutter hooks."""
    PostGen2SpaceFormattingSetup().execute()
    PostGenPoetrySetup().execute()
    PostGenGitSetup().execute()
    PostGenPrecommitSetup().execute()
    PostGenDocstringFilter().execute()
    PostGenSphinxFilter().execute()


class PostGen2SpaceFormattingSetup(BaseHookSystemCalls):
    """Niall's preferred 2-space setup."""

    formatting_option = "Niall's 2-Space Preference"

    def condition(self) -> bool:
        """Skip this hook if it's not selected or if an env var is set."""
        return (
            Template.option_formatting_type == self.formatting_option
            and os.getenv("TEMPLATE_SKIP_FMT_INIT") != "1"
        )

    def hook(self) -> None:
        """Format all specified files."""
        list(map(self.format, self.find_python_files()))

    def find_python_files(self) -> List[str]:
        """Find all files ending in a ".py" extension."""
        paths = []
        for root, _, files in os.walk(os.getcwd()):
            for file in files:
                if file.lower().endswith(".py".lower()):
                    paths.append(os.path.join(root, file))
        return paths

    def format(self, file_path: str) -> None:
        """Format the selected file (and docstrings) to a 2 space indent."""
        with open(file_path, "r", encoding="utf-8") as source:
            content = source.read()
        with open(file_path, "w", encoding="utf-8") as destination:
            destination.write(re.sub(r'    ', '  ', content))
        try:
            importlib.import_module("yapf")
            self.system_call("yapf -i {file_path}".format(file_path=file_path))
        except ModuleNotFoundError:
            pass


class PostGenPoetrySetup(BaseHookSystemCalls):
    """Post-generation hook to configure dependencies with poetry."""

    poetry_lock_command = "poetry lock"
    poetry_install_command = "poetry install"

    def condition(self) -> bool:
        """Skip this hook if an env var is set."""
        return os.getenv("TEMPLATE_SKIP_POETRY") != "1"

    def hook(self) -> None:
        """Create a poetry lock file and install the project."""
        self.system_call(self.poetry_lock_command)
        self.system_call(self.poetry_install_command)


class PostGenGitSetup(BaseHookSystemCalls):
    """Post-generation hook to configure a git repository."""

    git_initial_commit_message = "build(COOKIECUTTER): Initial Generation"
    git_root_folder = ".git"
    git_default_branch_name = Template.option_base_branch_name
    git_dev_branch_name = Template.option_dev_branch_name

    def condition(self) -> bool:
        """Skip this hook if git is initialized or if an env var is set."""
        return (
            (not os.path.exists(self.git_root_folder))
            and os.getenv("TEMPLATE_SKIP_GIT_INIT") != "1"
        )

    def hook(self) -> None:
        """Configure git for the template."""
        list(map(self.system_call, self._get_setup_commands()))

    def _get_setup_commands(self) -> List[str]:
        return [
            "git init",
            "git stage .",
            "git branch -m {name}".format(name=self.git_default_branch_name),
            "git commit -m '{message}'".format(
                message=self.git_initial_commit_message
            ),
            "git checkout -b {name}".format(name=self.git_dev_branch_name),
            "git checkout {name}".format(name=self.git_default_branch_name),
        ]


class PostGenPrecommitSetup(BaseHookSystemCalls):
    """Post-generation hook to configure the pre-commit hooks."""

    precommit_setup_command = "poetry run pre-commit install"

    def condition(self) -> bool:
        """Skip this hook if an env var is set."""
        return os.getenv("TEMPLATE_SKIP_PRECOMMIT") != "1"

    def hook(self) -> None:
        """Configure the pre-commit hooks."""
        self.system_call(self.precommit_setup_command)


class PostGenDocstringFilter(BaseHookFilter):
    """Post-generation hook to filter pydocstyle files."""

    excluded = [".pydocstyle", ".pydocstyle.tests"]

    def condition(self) -> bool:
        """Run the hook if docstrings was not selected."""
        return Template.option_docstrings == "false"


class PostGenSphinxFilter(BaseHookFilter):
    """Post-generation hook to filter sphinx/documentation files."""

    excluded = [".darglint", ".readthedocs.yml", "documentation"]

    def condition(self) -> bool:
        """Run the hook if sphinx was not selected."""
        return Template.option_sphinx == "false"


main()
