#!/bin/bash

# .github/scripts/template.sh
# Perform automated templating.

# 1: Python Version Selection
# 2: Formatting Selection
# 3: Typing Option Selection
# 4: Docstrings Option Selection
# 5: Lockfile Option Selection
# 6: Git Username
# 7: Git Email

# CI only script.

set -eo pipefail

SELECTION_PYTHON=${1:-"1"}
SELECTION_FORMATTING=${2:-"1"}
SELECTION_TYPING=${3:-"1"}
SELECTION_DOCSTRINGS=${4:-"1"}
SELECTION_LOCKFILE=${5:-"1"}
NAME=${6:-"Pro Buddy Dev"}
EMAIL=${7:-"somedude@coolstartup.com"}

main() {
  pip install cookiecutter poetry yapf toml
  git config --global user.name "${NAME}"
  git config --global user.email "${EMAIL}"

  {
    echo "TEMPLATE_SELECTION_PYTHON=${SELECTION_PYTHON}"
    echo "TEMPLATE_SELECTION_FORMATTING=${SELECTION_FORMATTING}"
    echo "TEMPLATE_SELECTION_TYPING=${SELECTION_TYPING}"
    echo "TEMPLATE_SELECTION_DOCSTRINGS=${SELECTION_DOCSTRINGS}"
    echo "TEMPLATE_SELECTION_LOCKFILE=${SELECTION_LOCKFILE}"
  } >> "$GITHUB_ENV"

  echo -e "${SELECTION_PYTHON}\n${SELECTION_TYPING}\n\n\n${SELECTION_FORMATTING}\n\n\n\n\n1\n${SELECTION_LOCKFILE}\n\n2\n2\n2\n" | cookiecutter template/

  echo "Templated With:"
  cat "${TEMPLATED_NAME}/.cookiecutter/cookiecutter.json"

}

main "$@"
