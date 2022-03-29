#!/bin/bash

# scripts/extras.sh
# Allow use of the CLI outside a containerized environment.  (Not recommended.)

# Host machine only:  Please do not use this script inside a PIB container.

set -eo pipefail

GIT_ROOT="$(git rev-parse --show-toplevel)"
export GIT_ROOT

pib_setup_hostmachine() {
  poetry install -E dev
  poetry run "${GIT_ROOT}/scripts/hooks/_install.sh"

  # shellcheck disable=SC2139
  alias dev="PIB_PROJECT_NAME=\"{{cookiecutter.project_slug}}\" PIB_CONFIG_FILE_LOCATION=\"${GIT_ROOT}/assets/cli.yml\" poetry run dev"
}
