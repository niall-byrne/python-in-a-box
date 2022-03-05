#!/bin/bash

# .github/scripts/gitleaks.sh
# Installs the binary for Gitleaks on a Linux machine.

# VERSION_GITLEAKS: The version of Gitleaks to install.

# CI only script.

set -eo pipefail

ARCH="linux_x64"

main() {

  curl --fail -sL "https://github.com/zricethezav/gitleaks/releases/download/v${VERSION_GITLEAKS}/gitleaks_${VERSION_GITLEAKS}_${ARCH}.tar.gz" -o gitleaks.tar.gz
  tar -xvzf gitleaks.tar.gz gitleaks
  sudo mv ./gitleaks /usr/bin/gitleaks
  rm gitleaks.tar.gz
  sudo chmod +x /usr/bin/gitleaks

}

main "$@"
