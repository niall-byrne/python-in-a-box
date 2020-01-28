# Python Development CookieCutter Template

Alpine Linux, Python 3.7 dockerized development environment.

## About

This container provides my preferred CLI tooling and a compartmentalized development environment for working on Python projects.

## Container

[python:3.7-alpine](https://github.com/docker-library/python/blob/master/3.7/alpine3.11/Dockerfile)

## License

[MIT](../LICENSE)

## Default Packages:
|        |                                                           |
|--------|-----------------------------------------------------------|
| bandit | Finds common security issues.                             |
| isort  | Sorts imports                                             |               
| pylint | (Google Style Formatting)                                 |
| pytest | Test suite                                                |
| safety | Dependency vulnerability scanning                         |
| wheel  | Package distribution tools                                |
| yapf   | (Google Style Formatting)                                 |


## Container OS Tooling
|      |                                                             |
|------|-------------------------------------------------------------|
| bash |  with a customizable environment and shellcheck for linting |
| jq   |  processing json                                            |
| git, ssh  |  managing git commits                                  |
| tig  |  managing git history                                       |
| vim  |  managing small edits, and git commit messages              |
