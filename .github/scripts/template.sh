#!/bin/bash

set -eo pipefail

SELECTION=${1:-"1"}
NAME=${2:-"Pro Buddy Dev"}
EMAIL=${3:-"somedude@coolstartup.com"}

main() {
  pip install cookiecutter
  git config --global user.name "${NAME}"
  git config --global user.email "${EMAIL}"
  echo -e "${SELECTION}\n\n\n\n\n\n\n\nfalse\nfalse\nfalse\n" | cookiecutter template/
}

main "$@"
