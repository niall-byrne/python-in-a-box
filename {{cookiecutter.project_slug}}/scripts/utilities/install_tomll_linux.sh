#!/bin/bash

# scripts/utilities/install_tomll_linux.sh
# Installs the binary for tomll on a Linux machine.

# VERSION_TOMLL: The version of tomll to install.

# Container, CI, or Linux based machines:  Use this script wherever needed to install tomll on Linux.

set -eo pipefail

ARCH="linux_amd64"

main() {

  curl --fail -sL "https://github.com/pelletier/go-toml/releases/download/${VERSION_TOMLL}/tomll_${ARCH}.tar.xz" -o tomll.tar.xz
  tar xvf tomll.tar.xz
  mv tomll /usr/bin
  chmod +x /usr/bin/tomll

}

main "$@"
