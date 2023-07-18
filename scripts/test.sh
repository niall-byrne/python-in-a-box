#!/bin/bash

# scripts/test.sh
# Templates and builds PIB with default values for testing.

# Host machine only.  Please do not use this script inside a PIB container.

SELECTION_PYTHON=1
SELECTION_DOCSTRINGS=1
SELECTION_SPHINX=1
SELECTION_TOML=1
SELECTION_TYPING=1
SELECTION_WORKFLOWS=1
SELECTION_FORMATTING=1
BRANCH_BASE_NAME="main"
BRANCH_DEV_NAME="dev"
SELECTION_LOCKFILE=1

main() {

  rm -rf ../mmmm_cookies

  local COOKIECUTTER_INPUT

  pushd .. || exit 127
  set -eo pipefail
  local PARAMS=(
    "${SELECTION_PYTHON}\n"
    "${SELECTION_DOCSTRINGS}\n"
    "${SELECTION_SPHINX}\n"
    "${SELECTION_TOML}\n"
    "${SELECTION_TYPING}\n"
    "${SELECTION_WORKFLOWS}\n"
    "\n"
    "\n"
    "${SELECTION_FORMATTING}\n"
    "\n"
    "${BRANCH_BASE_NAME}\n"
    "${BRANCH_DEV_NAME}\n"
    "\n"
    "\n"
    "\n"
    "${SELECTION_LOCKFILE}\n"
  )
  COOKIECUTTER_INPUT="$(
    IFS=
    printf '%s' "${PARAMS[*]}"
  )"
  echo -e "${COOKIECUTTER_INPUT}" | TEMPLATE_SKIP_POETRY=1 cookiecutter ./python-in-a-box/
  cd mmmm_cookies || exit 127
  docker-compose build --no-cache
  docker-compose up -d
  set +eo pipefail
  sleep 1
  ./container
  docker-compose kill
  docker-compose -f rm
  popd || exit 127

}

main "$@"
