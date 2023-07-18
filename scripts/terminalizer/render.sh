#!/bin/bash

# scripts/terminalizer/render.sh
# Renders the demo image for documentation.

# Host machine only, requires node.js and the installation of the terminalizer application.

main() {

  if ! command -v terminalizer > /dev/null 2>&1; then
    echo "You must install terminalizer to use this feature."
    echo "https://github.com/faressoft/terminalizer"
    echo ""
    exit 127
  fi

  set -eo pipefail
  terminalizer render demo.yml -o demo.gif
  set +eo pipefail

}

main "$@"
