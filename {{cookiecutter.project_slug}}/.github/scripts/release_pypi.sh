#!/bin/bash

# .github/scripts/release_pypi.sh
# Builds and publishes Python packages to either TestPYPI, or PYPI.

# PROJECT_NAME:               The name of the project as a string.
# PYPI_API_TOKEN:                 An optional API token for PYPI, stored as a Github Secret.
# TEST_PYPI_API_TOKEN:            An optional API token for TestPYPI, stored as a Github Secret.

# CI only script.

set -eo pipefail

publish_test() {
  docker-compose exec -T "${PROJECT_NAME}" bash -c "                                                     \
        poetry config repositories.testpypi https://test.pypi.org/legacy/                             && \
        poetry config http-basic.testpypi __token__ \"${TEST_PYPI_API_TOKEN}\"                        && \
        poetry publish --build -r testpypi
  "
}

publish_production() {
  docker-compose exec -T "${PROJECT_NAME}" bash -c "                                                     \
        poetry config http-basic.pypi __token__ \"${PYPI_API_TOKEN}\"                                 && \
        poetry publish --build
  "
}

main() {

  if [[ -n "${TEST_PYPI_API_TOKEN}" ]]; then
    publish_test
    echo "Successfully published to TestPyPi."
  fi

  if [[ -n "${PYPI_API_TOKEN}" ]]; then
    publish_production
    echo "Successfully published to PyPi."
  fi

}

main "$@"
