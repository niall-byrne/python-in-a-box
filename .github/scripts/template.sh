#!/bin/bash

# .github/scripts/template.sh
# Perform automated templating.

# 1: Python Version Selection
# 2: Formatting Selection
# 3: Lockfile Option Selection
# 4: Git Username
# 5: Git Email

# CI only script.

set -eo pipefail

SELECTION_PYTHON=${1:-"1"}
SELECTION_FORMATTING=${2:-"1"}
SELECTION_LOCKFILE=${3:-"1"}
NAME=${4:-"Pro Buddy Dev"}
EMAIL=${5:-"somedude@coolstartup.com"}

main() {
  pip install cookiecutter poetry yapf toml
  git config --global user.name "${NAME}"
  git config --global user.email "${EMAIL}"

  echo -e "${SELECTION_PYTHON}\n1\n\n\n${SELECTION_FORMATTING}\n\n\n\n\n1\n${SELECTION_LOCKFILE}\n2\n2\n2\n" | cookiecutter template/

  echo "Templated With:"
  cat "${TEMPLATED_NAME}/.cookiecutter/cookiecutter.json"
}

main "$@"
