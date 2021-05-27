#!/bin/bash

initialize_git() {

  git init
  git stage .
  git commit -m "build(Cookiecutter): Initial Generation"
  git tag v0.0.0
  git checkout -b production
  git checkout master

}

main() {

  if [[ -n "${PIB_SKIP_INIT}" ]]; then
    return 0
  fi

  initialize_git

}

main

