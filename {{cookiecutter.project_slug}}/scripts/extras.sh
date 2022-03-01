#!/bin/bash

# scripts/extras.sh
# Allow use of the CLI outside a containerized environment.  (Not recommended.)

# Host machine only:  Please do not use this script inside a PIB container.

set -eo pipefail

PIB_PROJECT_ROOT="$(git rev-parse --show-toplevel)"
export PIB_PROJECT_ROOT

pib_setup_hostmachine() {
  poetry install -E dev
  poetry run "${PIB_PROJECT_ROOT}/scripts/hooks/_install.sh"

  # shellcheck disable=SC2139
  alias dev="PROJECT_NAME=\"{{cookiecutter.project_slug}}\" PIB_CONFIG_FILE_LOCATION=\"${PIB_PROJECT_ROOT}/assets/cli.yml\" poetry run dev"
}
