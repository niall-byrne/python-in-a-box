#!/bin/bash

# .github/scripts/release_test.sh
# Controls the version used during the CI "push" job.

# CI only script.

set -eo pipefail

RELEASE_VERSION="1.0.0"  # Increment for end to end testing

main() {

  sed -i "s/version = \"0.0.1\"/version = \"${RELEASE_VERSION}\"/g" "./template/{{cookiecutter.project_slug}}/pyproject.toml"

}

main "$@"
