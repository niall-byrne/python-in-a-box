#!/bin/bash

current_directory="$(pwd)"

set -e

pushd .. >/dev/null
  rm -rf mmmm_cookies
  echo -e '\n\n\n\n\n\nfalse\nfalse\nfalse\n' | cookiecutter python-in-a-box/
  pushd mmmm_cookies >/dev/null

    finish() {
      cd "${current_directory}"
    }

    trap finish EXIT

    docker-compose build
    docker-compose up -d
    sleep 1

    docker-compose exec -T mmmm_cookies tomll /app/pyproject.toml
    docker-compose exec -T mmmm_cookies dev build-docs
    docker-compose exec -T mmmm_cookies dev build-wheel
    docker-compose exec -T mmmm_cookies dev coverage
    docker-compose exec -T mmmm_cookies dev fmt
    docker-compose exec -T mmmm_cookies dev lint
    docker-compose exec -T mmmm_cookies dev reinstall-requirements
    docker-compose exec -T mmmm_cookies dev sectest
    docker-compose exec -T mmmm_cookies dev setup
    docker-compose exec -T mmmm_cookies dev setup-bash
    docker-compose exec -T mmmm_cookies dev test
    docker-compose exec mmmm_cookies bash
    docker-compose kill
  popd >/dev/null
popd >/dev/null
