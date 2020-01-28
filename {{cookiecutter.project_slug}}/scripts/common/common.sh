#!/bin/bash

unvirtualize() {

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

}


security() {

  set -e

  pushd "${PROJECTHOME}"  > /dev/null
    bandit -r {{ cookiecutter.project_slug }} -c .bandit.rc
    safety check
  popd  > /dev/null

}

source_enviroment() {

  unvirtualize

  # shellcheck disable=SC1090
  source "$(pipenv --venv)/bin/activate"

  pushd "${PROJECTHOME}"  > /dev/null
    set +e
      cd .git/hooks
      ln -sf ../../scripts/hooks/pre-commit pre-commit
    set -e
  popd  > /dev/null

}

setup_python() {

  unvirtualize

  pushd "${PROJECTHOME}"  > /dev/null
    set +e
    pipenv --rm
    set -e
    pipenv --python 3.7
    source_enviroment
    reinstall_requirements
    unvirtualize
  popd  > /dev/null

}

reinstall_requirements() {

  set -e

  pushd "${PROJECTHOME}"  > /dev/null
    pip install -r assets/requirements.txt
    pip install -r assets/requirements-dev.txt
  popd  > /dev/null

}

lint() {

  set -e

  pushd "${PROJECTHOME}"  > /dev/null
    yapf -i --recursive --exclude '**/*_pb2.py' --style='{based_on_style: chromium, ALIGN_CLOSING_BRACKET_WITH_VISUAL_INDENT: false, DEDENT_CLOSING_BRACKETS: false}' "{{cookiecutter.project_slug}}/"
    isort -y
  popd  > /dev/null

  lint_check


}

lint_check() {

  set -e

  pushd "${PROJECTHOME}"  > /dev/null
    isort -c
    pylint --rcfile .pylint.rc {{cookiecutter.project_slug}}/
    shellcheck -x scripts/*.sh
    shellcheck -x scripts/common/*.sh
  popd  > /dev/null

}
