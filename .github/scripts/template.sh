#!/bin/bash

set -eo pipefail

SELECTION_LOCKFILE=${1:-"1"}
SELECTION_PYTHON=${1:-"1"}
NAME=${2:-"Pro Buddy Dev"}
EMAIL=${3:-"somedude@coolstartup.com"}

main() {
  pip install cookiecutter poetry
  git config --global user.name "${NAME}"
  git config --global user.email "${EMAIL}"
  echo -e "${SELECTION_PYTHON}\n1\n\n\n\n\n\n\n1\n${SELECTION_LOCKFILE}\n\n2\n2\n2\n" | cookiecutter template/
}

main "$@"
