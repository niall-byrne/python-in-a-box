#!/bin/bash

# .github/scripts/template.sh
# Perform automated templating.

# 1: Python Version Selection
# 2: Docstrings Option Selection
# 3: Sphinx Option Selection
# 4: Typing Option Selection
# 5: Formatting Selection
# 6: Lockfile Option Selection
# 7: Git Username
# 8: Git Email

# TEMPLATED_BASE_BRANCH: The base branch name set as a string

# CI only script.

set -eo pipefail

SELECTION_PYTHON=${1:-"1"}
SELECTION_DOCSTRINGS=${2:-"1"}
SELECTION_SPHINX=${3:-"1"}
SELECTION_TYPING=${4:-"1"}
SELECTION_FORMATTING=${5:-"1"}
SELECTION_LOCKFILE=${6:-"1"}
NAME=${7:-"Pro Buddy Dev"}
EMAIL=${8:-"somedude@coolstartup.com"}

main() {
  pip install cookiecutter poetry yapf toml
  git config --global user.name "${NAME}"
  git config --global user.email "${EMAIL}"

  {
    echo "TEMPLATE_SELECTION_PYTHON=${SELECTION_PYTHON}"
    echo "TEMPLATE_SELECTION_TYPING=${SELECTION_TYPING}"
    echo "TEMPLATE_SELECTION_DOCSTRINGS=${SELECTION_DOCSTRINGS}"
    echo "TEMPLATE_SELECTION_SPHINX=${SELECTION_SPHINX}"
    echo "TEMPLATE_SELECTION_TYPING=${SELECTION_TYPING}"
    echo "TEMPLATE_SELECTION_FORMATTING=${SELECTION_FORMATTING}"
    echo "TEMPLATE_SELECTION_LOCKFILE=${SELECTION_LOCKFILE}"
  } >> "$GITHUB_ENV"

  echo -e "${SELECTION_PYTHON}\n${SELECTION_DOCSTRINGS}\n${SELECTION_SPHINX}\n${SELECTION_TYPING}\n\n\n${SELECTION_FORMATTING}\n\n${TEMPLATED_BASE_BRANCH}\n\n\n\n${SELECTION_LOCKFILE}\n2\n2\n2\n" | cookiecutter template/

  echo "Templated With:"
  cat "${TEMPLATED_NAME}/.cookiecutter/cookiecutter.json"

}

main "$@"
