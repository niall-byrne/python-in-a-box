#!/bin/bash

# scripts/hooks/_install.sh
# Install the pre-commit hooks.

# This script can be run anywhere pre-commit is installed.

set -eo pipefail

main() {

  pre-commit install --install-hooks -t pre-commit -t commit-msg

}

main "$@"
