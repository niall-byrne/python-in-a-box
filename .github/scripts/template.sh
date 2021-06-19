#!/bin/bash

set -eo pipefail

SELECTION=${1:-"1"}
NAME=${2:-"Pro Buddy Dev"}
EMAIL=${3:-"somedude@coolstartup.com"}

main() {
  pip install cookiecutter poetry
  git config --global user.name "${NAME}"
  git config --global user.email "${EMAIL}"
  echo -e "${SELECTION}\n1\n\n\n\n\n\n\n\n2\n2\n2\n" | cookiecutter template/
}

main "$@"
