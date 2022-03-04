#!/bin/bash

# .github/scripts/generate_changelog.sh
# Generate a changelog from commitizen and store as a Github Action environment variable.

# CI only script.

set -eo pipefail

main() {

  echo "CHANGE_LOG<<EOF" >> "${GITHUB_ENV}"
  cz ch --start-rev "$(git tag | sort -V | tail -n2 | head -n1)" --dry-run >> "$GITHUB_ENV"
  echo "EOF" >> "${GITHUB_ENV}"

}

main "$@"
