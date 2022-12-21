#!/bin/bash

# scripts/utilities/install_trufflehog_linux.sh
# Installs the binary for TruffleHog on a Linux machine.

# VERSION_TRUFFLEHOG: The version of TruffleHog to install.

# Container, CI, or Linux based machines:  Use this script wherever needed to install TruffleHog on Linux.

set -eo pipefail

ARCH="linux_amd64"

main() {

  curl --fail -sL "https://github.com/trufflesecurity/trufflehog/releases/download/v${VERSION_TRUFFLEHOG}/trufflehog_${VERSION_TRUFFLEHOG}_${ARCH}.tar.gz" -o trufflehog.tar.gz
  tar -xvzf trufflehog.tar.gz trufflehog
  mv ./trufflehog /usr/bin/trufflehog
  rm trufflehog.tar.gz
  chmod +x /usr/bin/trufflehog

}

main "$@"