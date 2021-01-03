#!/bin/bash

set -e

ROOT="$(git rev-parse --show-toplevel)"
ARG="${1}"

export PIB_CONFIG_FILE_LOCATION="${ROOT}./assets/cli.yml"
export PROJECT_NAME="{{cookiecutter.project_slug}}"

conditional_source() {
  if [[ -z "$(poetry env list)" ]]; then
    setup_python
  fi
  spawn_shell
}

setup_python() {

  unvirtualize

  pushd "${ROOT}"  > /dev/null
    if [[ ! -f /etc/container_release ]]; then
      set +e
        poetry env remove python
      set -e
      pip install pib_cli==0.0.4
      poetry install
    fi
  popd  > /dev/null
  echo "Poetry Environment Location: $(poetry env list)"
}

source_environment() {

  if [[ ! -f /etc/container_release ]]; then

    unvirtualize

    # shellcheck disable=SC1090
    source "$(poetry env info --path)/bin/activate"

  fi

  pushd "${ROOT}"  > /dev/null
    set +e
      cd .git/hooks
      ln -sf ../../scripts/hooks/pre-commit pre-commit
    set -e
  popd  > /dev/null

}

spawn_shell() {

  if [[ "${ARG}" == "shell" ]]; then
    poetry shell
  else
    echo "Run this script with the *shell* argument to spawn a shell within the virtual environment."
  fi

}

unvirtualize() {

  if [[ ! -f /etc/container_release ]]; then
    toggle=1
    if [[ -n "${-//[^e]/}" ]]; then set +e; else toggle=0; fi
      deactivate_present=$(LC_ALL=C type deactivate 2>/dev/null)
      if [[ -n ${deactivate_present} ]]; then
        deactivate
      fi
    if [[ "${toggle}" == "1" ]]; then set -e; fi
  fi

}

conditional_source
