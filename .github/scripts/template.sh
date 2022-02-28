#!/bin/bash

# .github/scripts/template.sh
# Perform automated templating.

# 1: Python Version Selection
# 2: Lockfile Option Selection
# 3: Git Username
# 4: Git Email

# CI only script.

set -eo pipefail

SELECTION_PYTHON=${1:-"1"}
SELECTION_LOCKFILE=${2:-"1"}
NAME=${3:-"Pro Buddy Dev"}
EMAIL=${4:-"somedude@coolstartup.com"}

main() {
  pip install cookiecutter poetry
  git config --global user.name "${NAME}"
  git config --global user.email "${EMAIL}"
  echo -e "${SELECTION_PYTHON}\n1\n\n\n\n\n\n\n1\n${SELECTION_LOCKFILE}\n\n2\n2\n2\n" | cookiecutter template/
}

main "$@"
