#!/bin/bash

PIB_PROJECT_ROOT="$(git rev-parse --show-toplevel)"
export PIB_PROJECT_ROOT

install_git_hooks() {
  pushd "${PIB_PROJECT_ROOT}"  > /dev/null
    set +e
      cd .git/hooks
      ln -sf ../../scripts/hooks/pre-commit pre-commit
    set -e
  popd  > /dev/null
}

pib_prefer_black() {
  pip install black
  sed -i 's/yapf -i --recursive \./black \./g' "${PIB_PROJECT_ROOT}/assets/cli.yml"
  sed -i 's/indent = "  "/indent = "    "/g' "${PIB_PROJECT_ROOT}/pyproject.toml"
  sed -i 's/indent-string = "  "/indent-string = "    "/g' "${PIB_PROJECT_ROOT}/pyproject.toml"
  rm -rf "${PIB_PROJECT_ROOT}/.yapfignore"
  rm -rf "${PIB_PROJECT_ROOT}/.style.yapf"
  black .
}

pib_setup_hostmachine() {
  poetry install

  # shellcheck disable=SC2139
  alias dev="PROJECT_NAME=\"{{cookiecutter.project_slug}}\" PIB_CONFIG_FILE_LOCATION=\"${PIB_PROJECT_ROOT}/assets/cli.yml\" poetry run dev"
}
