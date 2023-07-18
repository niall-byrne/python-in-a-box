#!/bin/bash

# scripts/update.sh
# This script helps automate the process of updating a project that has already been templated.
# A branch "update-template" is created, with the changes required to update the workflow.
# Use git cherry-pick (or create a patch from this change set) to update your project.

# Requires: https://pypi.org/project/cookiecutter-project-upgrader/

# Host machine only.  Please do not use this script inside a PIB container.

error() {
  echo "USAGE: ./update.sh [PROJECT FOLDER] [TEMPLATE TAG or BRANCH]"
  exit 127
}

[[ -z $2 ]] && error
[[ -z $1 ]] && error

main() {

  pushd "$1" || error
  cookiecutter_project_upgrader \
    -c .cookiecutter/cookiecutter.json \
    -b "update-template" \
    -u "$2" \
    -f https://github.com/niall-byrne/python-in-a-box.git \
    -e "assets" \
    -e "documentation" \
    -e "$1" \
    -e ".bandit" \
    -e ".bandit.rc" \
    -e ".dockerignore" \
    -e ".gitignore" \
    -e ".readthedocs.yml" \
    -e ".style.yapf" \
    -e ".yamllint.yml" \
    -e ".yapfignore" \
    -e "container" \
    -e "docker-compose.yml" \
    -e "LICENSE" \
    -e "pyproject.toml" \
    -e "pytest.ini" \
    -e "README.md" \
    -e "testing_shim"

  git checkout update-template
  popd || true

}

main "$@"
