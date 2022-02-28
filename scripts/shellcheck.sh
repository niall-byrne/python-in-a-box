#!/bin/bash

# scripts/setup.sh
# Runs shellcheck on all template scripts.

# This script can be run anywhere shellcheck is installed.

set -eo pipefail

main() {

  shellcheck ./template/.github/scripts/*.sh
  shellcheck ./template/hooks/*.sh
  shellcheck ./template/scripts/*.sh
  shellcheck ./"${TEMPLATED_NAME}"/scripts/*.sh
  shellcheck ./"${TEMPLATED_NAME}"/scripts/hooks/*.sh

}

main "$@"
