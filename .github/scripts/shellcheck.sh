#!/bin/bash

set -eo pipefail

main() {

  shellcheck ./template/.github/scripts/*.sh
  shellcheck ./template/scripts/*.sh

}

main "$@"
