#!/bin/bash

set -o pipefail

main() {

  shellcheck ./template/.github/scripts/*.sh
  shellcheck ./template/scripts/*.sh

}

main "$@"
