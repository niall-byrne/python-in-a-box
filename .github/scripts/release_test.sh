#!/bin/bash

set -eo pipefail

RELEASE_VERSION="0.0.11"  # Increment for end to end testing

main() {

  sed -i "s/version = \"0.0.1\"/version = \"${RELEASE_VERSION}\"/g" "./template/{{cookiecutter.project_slug}}/pyproject.toml"

}

main "$@"
