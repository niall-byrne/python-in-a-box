#!/bin/bash

NAME=${1:-"Pro Buddy Dev"}
EMAIL=${2:-"somedude@coolstartup.com"}

main() {
  pip install cookiecutter
  git config --global user.name "${NAME}"
  git config --global user.email "${EMAIL}"
  echo -e '\n\n\n\n\n\n\nfalse\nfalse\nfalse\n' | cookiecutter template/
}

main
