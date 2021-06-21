#!/bin/bash

set -eo pipefail

main() {

  shellcheck ./template/.github/scripts/*.sh
  shellcheck ./template/scripts/*.sh

  shellcheck ./"${TEMPLATED_NAME}"/scripts/*.sh

}

main "$@"
