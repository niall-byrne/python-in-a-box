#!/usr/bin/env bash

PROJECT_HOME="$(git rev-parse --show-toplevel)"
PROJECT_NAME="{{cookiecutter.project_slug}}"
PROJECT_AUTHOR="{{cookiecutter.author}}"

export PROJECT_HOME
export PROJECT_NAME
export PROJECT_AUTHOR
