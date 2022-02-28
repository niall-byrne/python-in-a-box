#!/bin/bash

# scripts/test.sh
# Templates and builds PIB with default values for testing.

# Host machine only.  Please do not use this script inside a PIB container.

SELECTION_TYPING_SUPPORT=1
SELECTION_PYTHON=1
SELECTION_LOCKFILE=1

main() {

  rm -rf ../mmmm_cookies

  pushd .. || exit 127
    set -eo pipefail
      echo -e "${SELECTION_PYTHON}\n${SELECTION_TYPING_SUPPORT}\n\n\n\n\n\n\n1\n${SELECTION_LOCKFILE}\n\n2\n2\n2\n" | PIB_SKIP_POETRY_INIT=1 cookiecutter ./python-in-a-box/
      cd mmmm_cookies  || exit 127
      docker-compose build
      docker-compose up -d
    set +eo pipefail
    sleep 1
    ./container
    docker-compose kill
    docker-compose -f rm
  popd || exit 127

}

main "$@"
