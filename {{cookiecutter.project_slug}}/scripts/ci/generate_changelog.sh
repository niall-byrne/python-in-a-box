#!/bin/bash

# scripts/ci/generate_changelog.sh
# Generate a changelog from commitizen and store as a Github Action environment variable.

# CI only script.

set -eo pipefail

main() {

  cz ch --start-rev "$(git tag | sort -V | tail -n2 | head -n1)" --dry-run

}

main "$@"
