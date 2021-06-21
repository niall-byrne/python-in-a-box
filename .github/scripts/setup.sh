#!/bin/bash

# shellcheck disable=SC2129

set -eo pipefail

main() {
  BRANCH_OR_TAG="$(echo "${GITHUB_REF}" | sed 's/refs\/heads\///g' | sed 's/refs\/tags\///g')"
  PROJECT_NAME="python-in-a-box"
  echo "BRANCH_OR_TAG=${BRANCH_OR_TAG}" >> "$GITHUB_ENV"
  echo "WEBHOOK_URL=${WEBHOOK_URL}" >> "$GITHUB_ENV"
  echo "PROJECT_NAME=${PROJECT_NAME}" >> "$GITHUB_ENV"
  echo "NOTIFICATION=${PROJECT_NAME} [${BRANCH_OR_TAG}]" >> "$GITHUB_ENV"
  echo "USERNAME=shared-vision-solutions" >> "$GITHUB_ENV"
  echo "TEMPLATED_NAME=mmmm_cookies" >> "$GITHUB_ENV"
  echo "PYTHON_VERSION=${PYTHON_VERSION}" >> "$GITHUB_ENV"
}

main "$@"
