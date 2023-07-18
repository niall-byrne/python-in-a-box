#!/bin/bash

# .github/scripts/release_docker.sh
# Sets environment content for the Docker CD workflows.

# DOCKER_TOKEN: An API token for DockerHub set as a Github Secret.

# CI only script.

set -eo pipefail

main() {

  if [[ -n "${DOCKER_TOKEN}" ]]; then

    echo "CD_DOCKER_REPO_ENABLED=true" >> "$GITHUB_ENV"

  fi

}

main "$@"
