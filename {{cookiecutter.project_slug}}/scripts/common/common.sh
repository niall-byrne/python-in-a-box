#!/bin/bash

unvirtualize() {

  if [[ ! -f /etc/container_release ]]; then

    toggle=1

    if [[ -n "${-//[^e]/}" ]]; then set +e; else toggle=0; fi
    if python -c 'import sys; sys.exit(0 if hasattr(sys, "real_prefix") else 1)'; then
    deactivate_present=$(LC_ALL=C type deactivate 2>/dev/null)
    if [[ -n ${deactivate_present} ]]; then
      deactivate
    else
      exit
    fi
    fi
    if [[ "${toggle}" == "1" ]]; then set -e; fi

  fi

}


security() {

  set -e

  pushd "${PROJECT_HOME}"  > /dev/null
    bandit -r "${PROJECT_NAME}" -c .bandit.rc
    safety check
  popd  > /dev/null

}

source_enviroment() {

  if [[ ! -f /etc/container_release ]]; then

    unvirtualize

    # shellcheck disable=SC1090
    source "$(pipenv --venv)/bin/activate"

  fi

  pushd "${PROJECT_HOME}"  > /dev/null
    set +e
      cd .git/hooks
      ln -sf ../../scripts/hooks/pre-commit pre-commit
    set -e
  popd  > /dev/null

}

setup_python() {

  unvirtualize

  pushd "${PROJECT_HOME}"  > /dev/null
    if [[ ! -f /etc/container_release ]]; then
      set +e
        pipenv --rm
      set -e
      pipenv --python 3.7
    fi
    source_enviroment
    reinstall_requirements
    unvirtualize
  popd  > /dev/null

}

reinstall_requirements() {

  set -e

  pushd "${PROJECT_HOME}"  > /dev/null
    pip install -r assets/requirements.txt --no-warn-script-location
    pip install -r assets/requirements-dev.txt --no-warn-script-location
  popd  > /dev/null

}

lint() {

  set -e

  pushd "${PROJECT_HOME}"  > /dev/null
    yapf -i --recursive --exclude '**/*_pb2.py' --style='{based_on_style: google, INDENT_WIDTH: 2, ALIGN_CLOSING_BRACKET_WITH_VISUAL_INDENT: false, DEDENT_CLOSING_BRACKETS: false}' "${PROJECT_NAME}/"
    isort -y
  popd  > /dev/null

  lint_check


}

lint_check() {

  set -e

  pushd "${PROJECT_HOME}"  > /dev/null
    isort -c
    pushd "${PROJECT_NAME}" > /dev/null
      pylint --rcfile ../.pylint.rc -j 2 "${PROJECT_NAME}"
    popd > /dev/null
    shellcheck -x scripts/*.sh
    shellcheck -x scripts/common/*.sh
  popd  > /dev/null

}

unittests() {

  set -e

  pushd "${PROJECT_HOME}"  > /dev/null
    if [[ $1 == "coverage" ]]; then
      shift
      pytest --cov=. --cov-fail-under=100 "$@"
      coverage html
    else
      pytest "$@"
    fi
  popd  > /dev/null

}