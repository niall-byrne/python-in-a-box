# Python Development CookieCutter Template

Python 3.7 dockerized development environment.

(Please see the [cookiecutter documentation](https://cookiecutter.readthedocs.io/) for instructions on how to use this project template.)

##### Develop Branch:
[![Python In A Box Self Test](https://github.com/niall-byrne/python-in-a-box/workflows/Python%20In%20A%20Box%20Self%20Test/badge.svg)](https://github.com/niall-byrne/python-in-a-box/actions?branch=develop)

##### Master Branch:
[![Python In A Box Self Test](https://github.com/niall-byrne/python-in-a-box/workflows/Python%20In%20A%20Box%20Self%20Test/badge.svg)](https://github.com/niall-byrne/python-in-a-box/actions?branch=master)

## About

This container provides my preferred CLI tooling and a compartmentalized development environment for working on Python projects.

## Container

[python:3.7-slim](https://github.com/docker-library/python/tree/master/3.7/buster/slim)

## License

[MPL-2](LICENSE)

## Default Packages:
| package | Description                                                 |
|---------|-------------------------------------------------------------|
| bandit  | Finds common security issues.                               |
| commitizen | Standardizes commit messages                             |
| isort   | Sorts imports                                               |               
| pylint  | (Google Style Formatting)                                   |
| pytest  | Test suite                                                  |
| pytest-cov | Coverage support for pytest                              |
| sphinx  | Generating documentation                                    |
| safety  | Dependency vulnerability scanning                           |
| wheel   | Package distribution tools                                  |
| yapf    | (Google Style Formatting)                                   |


## Container OS Tooling
| package | Description                                                 |
|---------|-------------------------------------------------------------|
| bash    |  with a customizable environment and shellcheck for linting |
| jq      |  processing json                                            |
| git, ssh|  managing git commits                                       |
| tig     |  managing git history                                       |
| vim     |  managing small edits, and git commit messages              |

## Getting Started

- `pip install cookiecutter`
- `cookiecutter https://github.com/niall-byrne/python-in-a-box.git`
