#!/bin/bash

# .github/scripts/changelog.sh
# Generates a changelog based off the diff between $TAG and the previous sequential tag.

# TAG: The new git tag the changelog is being generated for.

# CI only script

set -eo pipefail

main() {

  echo "{}" > package.json
  TAG="$(git tag | sort --version-sort | tail -n 2 | head -n 1)"
  CHANGE_LOG_CONTENT="$(npx -q generate-changelog -f - -t "${TAG}")"

  {
    echo "CHANGE_LOG_CONTENT<<EOF"
    echo "${CHANGE_LOG_CONTENT}"
    echo "EOF"
  } >> "$GITHUB_ENV"

  rm package.json

}

main
