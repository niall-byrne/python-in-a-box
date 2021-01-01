# Python Development CookieCutter Template

Python 3.7 dockerized development environment.

(Please see the [cookiecutter documentation](https://cookiecutter.readthedocs.io/) for instructions on how to use this project template.)

##### Develop Branch:
[![Python In A Box Self Test](https://github.com/shared-vision-solutions/python-in-a-box/workflows/Python%20In%20A%20Box%20Self%20Test/badge.svg?branch=develop)](https://github.com/shared-vision-solutions/python-in-a-box/actions)

##### Master Branch:
[![Python In A Box Self Test](https://github.com/shared-vision-solutions/python-in-a-box/workflows/Python%20In%20A%20Box%20Self%20Test/badge.svg?branch=master)](https://github.com/shared-vision-solutions/python-in-a-box/actions)

## About

This container provides my preferred CLI tooling and a compartmentalized development environment for working on Python projects.

## Getting Started

- `pip install cookiecutter`
- `cookiecutter https://github.com/shared-vision-solutions/python-in-a-box.git`

## Container

[python:3.7-slim](https://github.com/docker-library/python/tree/master/3.7/buster/slim)

## License

[MPL-2](LICENSE)

## Tooling Reference
The CLI is instsalled by default inside the container, and is also available on the host machine.
Run the CLI without arguments to see the complete list of available commands: `dev`

[The 'pib_cli' Python Package](https://pypi.org/project/pib-cli/)

The local CLI configuration is managed by the [cli.yaml](./{{cookiecutter.project_slug}}/assets/cli.yaml) file.

## Installed Python Packages:

| package    | Description                       |
| ---------- | --------------------------------- |
| bandit     | Finds common security issues      |
| commitizen | Standardizes commit messages      |
| isort      | Sorts imports                     |
| pylint     | Static Code Analysis              |
| pytest     | Test suite                        |
| pytest-cov | Coverage support for pytest       |
| sphinx     | Generating documentation          |
| safety     | Dependency vulnerability scanning |
| wheel      | Package distribution tools        |
| yamllint   | Lint yaml configuration files     |
| yapf       | Customizable Code Formatting      |

## Container OS Tooling
| package | Description                                                 |
|---------|-------------------------------------------------------------|
| bash    |  with a customizable environment and shellcheck for linting |
| jq      |  processing json                                            |
| git, ssh|  managing git commits                                       |
| tig     |  managing git history                                       |
| vim     |  managing small edits, and git commit messages              |

## Configuration Files

Files are created in the project root folder for the following:

- [Bandit](https://bandit.readthedocs.io/en/latest/)
  - [.bandit](./{{cookiecutter.project_slug}}/.bandit)
  - [.banditrc](./{{cookiecutter.project_slug}}/.bandit.rc)
- [Coverage](https://coverage.readthedocs.io/en/coverage-5.3.1/)
  - [.coveragerc](./{{cookiecutter.project_slug}}/.coveragerc)
- [Git](https://git-scm.com/)
  - [.gitignore](./{{cookiecutter.project_slug}}/.gitignore)
- [iSort](https://pycqa.github.io/isort/)
  - [.isort.config](./{{cookiecutter.project_slug}}/.isort.cfg)
- [pylint](https://www.pylint.org/)
  - [.pylint.rc](./{{cookiecutter.project_slug}}/.pylint.rc)
- [Read The Docs](https://readthedocs.org/)
  - [.readthedocs.yml](./{{cookiecutter.project_slug}}/.readthedocs.yml)
- [yapf](https://readthedocs.org/)
  - [.style.yapf](./{{cookiecutter.project_slug}}/.style.yapf)
  - [.yapfignore](./{{cookiecutter.project_slug}}/.yapfignore)
- [Software License](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/licensing-a-repository)
  - [LICENSE](./{{cookiecutter.project_slug}}/LICENSE)
- [pipenv](https://github.com/pypa/pipenv) ([scripts/hostmachine.sh](./{{cookiecutter.project_slug}}/scripts/hostmachine.sh))
  - [Pipfile](./{{cookiecutter.project_slug}}/Pipfile) 
- [pytest](https://docs.pytest.org/en/stable/)
  - [pytest.ini](./{{cookiecutter.project_slug}}/pytest.ini)
- [pypi.org](https://pypi.org/)
  - [setup.cfg](./{{cookiecutter.project_slug}}/setup.cfg)
  - [setup.py](./{{cookiecutter.project_slug}}/setup.py)

## Third Party Integrations

Integrations with the following third party services are configured during templating:

- [Github Workflows](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions)
  - [workflows](./{{cookiecutter.project_slug}}/.github/workflows)
- [Docker Hub](https://hub.docker.com/)
  - [release_container.yml](./{{cookiecutter.project_slug}}/.github/workflows/release_container.yml)
- [pypi.org](https://pypi.org/)
  - [setup.py](./{{cookiecutter.project_slug}}/setup.py)
- [Read The Docs](https://readthedocs.org/)
  - [.readthedocs.yml](./{{cookiecutter.project_slug}}/.readthedocs.yml)
