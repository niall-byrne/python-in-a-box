#!/bin/bash

initialize_git() {

  [[ -d .git ]] && return 0

  git init
  git stage .
  git commit -m "build(Cookiecutter): Initial Generation"
  git tag v0.0.0
  git checkout -b production
  git checkout master

}

initialize_poetry() {

  [[ -f "poetry.lock" ]] && return 0

  poetry lock

}

main() {

  if [[ -n "${PIB_SKIP_INIT}" ]]; then
    return 0
  fi

  initialize_poetry
  initialize_git

}

main
