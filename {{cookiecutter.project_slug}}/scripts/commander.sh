#!/bin/bash

set -e

PROJECT_HOME="$(git rev-parse --show-toplevel)"
PROJECT_NAME="{{cookiecutter.project_slug}}"
export PROJECT_HOME
export PROJECT_NAME

# shellcheck source=scripts/common/common.sh
source "$( dirname "${BASH_SOURCE[0]}" )/common/common.sh"

# Add Additional Functionality Via Imports Here

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
  'shortlist')
    echo "lint lint-validate reinstall-requirements sectest setup test test-coverage"
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
    echo ' - test'
    echo ' - test-coverage'
    ;;

esac
