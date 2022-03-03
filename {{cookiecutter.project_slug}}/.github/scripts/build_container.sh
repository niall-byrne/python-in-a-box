#!/bin/bash

set -eo pipefail
COMPOSE_FILE=${1-docker-compose.yml}

main() {

  docker-compose -f "${COMPOSE_FILE}" build --build-arg BUILD_ARG_PYTHON_VERSION="${PYTHON_VERSION}"
  docker-compose -f "${COMPOSE_FILE}" up -d

}

main "$@"
