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

    docker-compose exec -T mmmm_cookies bash -l -c 'tomll /app/pyproject.toml'
    docker-compose exec -T mmmm_cookies bash -l -c 'dev build-docs'
    docker-compose exec -T mmmm_cookies bash -l -c 'dev build-wheel'
    docker-compose exec -T mmmm_cookies bash -l -c 'dev coverage'
    docker-compose exec -T mmmm_cookies bash -l -c 'dev fmt'
    docker-compose exec -T mmmm_cookies bash -l -c 'dev lint'
    docker-compose exec -T mmmm_cookies bash -l -c 'dev reinstall-requirements'
    docker-compose exec -T mmmm_cookies bash -l -c 'dev sectest'
    docker-compose exec -T mmmm_cookies bash -l -c 'dev setup'
    docker-compose exec -T mmmm_cookies bash -l -c 'dev setup-bash'
    docker-compose exec -T mmmm_cookies bash -l -c 'dev test'
    docker-compose exec mmmm_cookies bash
    docker-compose kill
  popd >/dev/null
popd >/dev/null
