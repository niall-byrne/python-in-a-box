#!/bin/bash

# /hooks/post_gen_project.sh
# Initialize Git and Poetry after templating with cookiecutter.

# Host machine only.  This script is part of the template process.

# PIB_SKIP_POETRY_INIT: set to a value to skip poetry installation
# PIB_SKIP_GIT_INIT: set to a value to skip the repository initialization

initialize_git() {

  [[ -d .git ]] && return 0

  git init
  git stage .
  git commit -m "build(COOKIECUTTER): Initial Generation"
  git tag v0.0.0
  git checkout -b production
  git checkout master

}

initialize_poetry() {

  [[ -f "poetry.lock" ]] && return 0

  poetry lock

}

main() {

  if [[ -z "${PIB_SKIP_POETRY_INIT}" ]]; then
    initialize_poetry
  fi

  if [[ -z "${PIB_SKIP_GIT_INIT}" ]]; then
    initialize_git
  fi

}

main
