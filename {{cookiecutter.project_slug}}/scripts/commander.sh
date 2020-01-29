#!/bin/bash

set -e

PROJECTHOME="$(git rev-parse --show-toplevel)"
export PROJECTHOME

# shellcheck source=scripts/common/common.sh
source "$( dirname "${BASH_SOURCE[0]}" )/common/common.sh"

case $1 in
  'lint')
    shift
    source_enviroment
    lint "$@"
    ;;
  'lint-validate')
    shift
    source_enviroment
    lint_check "$@"
    ;;
  'reinstall-requirements')
    shift
    source_enviroment
    reinstall_requirements "$@"
    ;;
  'sectest')
    shift
    source_enviroment
    security "$@"
    ;;
  'setup')
    shift
    setup_python "$@"
    ;;
  'shell')
    shift
    source_enviroment
    pipenv shell
    ;;
  'shortlist')
    echo "lint lint-validate reinstall-requirements sectest setup shell test test-coverage"
    ;;
  'test')
    shift
    source_enviroment
    unittests "$@"
    ;;
  'test-coverage')
    shift
    source_enviroment
    unittests "coverage" "$@"
    ;;
  *)
    echo "Valid Commands:"
    echo ' - lint'
    echo ' - lint-validate'
    echo ' - reinstall-requirements'
    echo ' - sectest'
    echo ' - setup'
    echo ' - shell'
    echo ' - test'
    echo ' - test-coverage'
    ;;

esac
