#!/bin/bash

# .github/scripts/build_container.sh
# Builds the container to a specific Python version.

# 1: The docker-compose file to use, defaults to "docker-compose.yaml"
# PYTHON_VERSION: The version of Python to build the container with.

# CI only script.

set -eo pipefail

COMPOSE_FILE=${1-docker-compose.yml}

main() {

  docker-compose -f "${COMPOSE_FILE}" build                   \
    --build-arg BUILD_ARG_PYTHON_VERSION="${PYTHON_VERSION}"  \
    --build-arg BUILD_ARG_CONTAINER_GID="$(id -g)"            \
    --build-arg BUILD_ARG_CONTAINER_UID="$(id -u)"
  docker-compose -f "${COMPOSE_FILE}" up -d

}

main "$@"
