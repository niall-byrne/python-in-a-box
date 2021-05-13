#!/bin/bash

DEVELOPMENT() {
  pushd "{{cookiecutter.project_slug}}" || exit 127
  while true; do sleep 1; done
}

PRODUCTION() {
  {{cookiecutter.project_slug}}
}

eval "${ENVIRONMENT}"
