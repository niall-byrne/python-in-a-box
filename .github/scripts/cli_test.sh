#!/bin/bash

# .github/scripts/cli_test.sh
# Validate the installed pib_cli version and default configuration.

# PIB_CONFIG_FILE_LOCATION:   The location of the CLI configuration file.
# TEMPLATE_SELECTION_SPHINX:  The template selection for including documentation support.
# TEMPLATE_SELECTION_TYPING:  The template selection for including typing support.

# CI only script.

set -eo pipefail

main() {

  [[ "${TEMPLATE_SELECTION_SPHINX}" == "1" ]] && dev build-docs

  dev build-wheel
  dev coverage
  dev fmt
  dev leaks
  dev lint
  dev reinstall-requirements
  dev sectest
  dev test

  [[ "${TEMPLATE_SELECTION_TYPING}" == "1" ]] && dev types

  dev -h

  dev @pib version | grep -E "pib_cli version: 1.[0-9]+.[0-9]+"

  dev @pib config validate | grep "This configuration is valid."

  diff <(dev @pib config show) "${PIB_CONFIG_FILE_LOCATION}"

  dev @pib config where | grep "Configuration file: ${PIB_CONFIG_FILE_LOCATION}"

  set +eo pipefail

  if [[ -f /etc/container_release ]]; then
    dev @pib container setup | grep "Setup Succeeded!" || exit 127
    dev @pib container version | grep -E 'Container version: 1\.[0-9]+\.[0-9]+' || exit 127
    dev @pib container validate | grep "This container is valid." || exit 127
  else
    dev @pib container setup | grep "This command can only be run inside a PIB container." || exit 127
    dev @pib container version | grep "No PIB container found." || exit 127
    dev @pib container validate | grep "No compatible PIB container found." || exit 127
  fi

}

main "$@"
