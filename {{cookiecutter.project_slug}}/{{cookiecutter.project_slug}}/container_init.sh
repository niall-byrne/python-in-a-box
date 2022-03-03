#!/bin/bash

# ./{{cookiecutter.project_slug}}/container_init.sh
# PIB container init script.

# Container Only:  Please use this hook inside a PIB container.

DEVELOPMENT() {
  pre-commit install
  pushd "{{cookiecutter.project_slug}}" || exit 127
  while true; do sleep 1; done
}

PRODUCTION() {
  {{cookiecutter.project_slug}}
}

eval "${ENVIRONMENT}"
