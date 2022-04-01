#!/bin/bash

# scripts/ci/lint_shellcheck.sh
# Runs shellcheck on all scripts.

# CI only script

set -eo pipefail

main() {

  find . -name "*.sh" -print0  | xargs --null shellcheck

}

main "$@"
