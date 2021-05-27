#!/bin/bash

set -o pipefail

main() {

  shellcheck ./.github/scripts/*.sh
  shellcheck ./{{cookiecutter.project_slug}}/*.sh
  shellcheck ./scripts/*.sh
  shellcheck ./scripts/hooks/*

}

main "$@"
