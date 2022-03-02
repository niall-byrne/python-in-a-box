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

  [[ "$(dev @pib version)" =~ pib_cli[[:space:]]version:[[:space:]]1.[0-9]+.[0-9]+ ]]

  dev @pib config validate

  diff <(dev @pib config show) "${PIB_CONFIG_FILE_LOCATION}"
  [[ "$(dev @pib config where)" == "Current Configuration: ${PIB_CONFIG_FILE_LOCATION}" ]]

  set +e

  if [[ -f /etc/container_release ]]; then
    set -e
    dev @pib container setup
    [[ "$(dev @pib container version)" =~ Detected[[:space:]]PIB[[:space:]]container[[:space:]]version:[[:space:]]1\.[0-9]+\.[0-9]+ ]]
    [[ "$(dev @pib container validate)" == "Detected valid container." ]]
  else
    set -e
    [[ "$(dev @pib container validate)" == "No PIB container found." ]] || echo
    [[ "$(dev @pib container version)" == "No PIB container found." ]] || echo
  fi

}

main "$@"
