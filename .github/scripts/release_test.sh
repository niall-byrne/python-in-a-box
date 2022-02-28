#!/bin/bash

# .github/scripts/release_test.sh
# Controls the version used during the CI "push" job.

# RELEASE_VERSION: The tag used by the push job in the release test.

# CI only script.

set -eo pipefail

RELEASE_VERSION="1.0.0"

main() {

  sed -i "s/version = \"0.0.1\"/version = \"${RELEASE_VERSION}\"/g" "./template/{{cookiecutter.project_slug}}/pyproject.toml"

}

main "$@"
