#!/bin/bash

set -eo pipefail

main() {

  RELEASE_TYPE="none"

  if [[ -n "${TEST_PYPI_API_TOKEN}" ]] && [[ "${TEST_RELEASE}" == "1" ]]; then
    # If there is an production pypi token, and test_release is active, enforce test mode only
    RELEASE_TYPE="test"
  fi

  if [[ -n "${PYPI_API_TOKEN}" ]] && [[ "${TEST_RELEASE}" == "0" ]]; then
    # If there is an production pypi token, and test_release is off, enforce production mode only
    RELEASE_TYPE="production"
  fi

  case "${RELEASE_TYPE}" in
    "test")
      echo "CD_TEST=true" >> "$GITHUB_ENV"
      docker-compose exec -T "${PROJECT_NAME}" bash -c "                                                 \
        poetry config repositories.testpypi https://test.pypi.org/legacy/                             && \
        poetry publish --build -r testpypi --username __token__ --password \"${TEST_PYPI_API_TOKEN}\"    \
      "
      ;;
    "production")
      echo "CD_ENABLED=true" >> "$GITHUB_ENV"
      docker-compose exec -T "${PROJECT_NAME}" bash -c "                                                 \
        poetry publish --build --username __token__ --password \"${PYPI_API_TOKEN}\"                     \
      "
      ;;
    *)
      echo "Cannot perform a test or production release with these credentials and settings."
      ;;
  esac

}

main "$@"
