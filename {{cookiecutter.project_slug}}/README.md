# Project Documentation

## {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

[Project Documentation](https://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/)

### Develop Branch
[![{{cookiecutter.project_slug}}-automation](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}%20Automation/badge.svg?branch=develop)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions)

### Master Branch
[![{{cookiecutter.project_slug}}-automation](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}%20Automation/badge.svg?branch=master)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions)

## Tooling Reference
The CLI is enabled by default inside the container, and is also available on the host machine.
Run the CLI without arguments to see the complete list of available commands: `dev`

[PIB CLI Documentation](https://pib_cli.readthedocs.io/en/latest/)

The local CLI configuration is managed by the [cli.yaml](./assets/cli.yaml) file.

## Third Party Integrations

Integrations with the following third party services are templated and ready to use:

- [Github Workflows](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions)
  - [workflows](./.github/workflows)
- [Docker Hub](https://hub.docker.com/)
  - [release_container.yml](./.github/workflows/release_container.yml)
- [pypi.org](https://pypi.org/)
  - [setup.py](./setup.py)
  - [setup.cfg](./setup.cfg)  
- [Read The Docs](https://readthedocs.org/)
  - [.readthedocs.yml](./.readthedocs.yml)

## Development Dependencies

You'll need to install:
 - [Docker](https://www.docker.com/) 
 - [Docker Compose](https://docs.docker.com/compose/install/)

## Setup the Development Environment

Build the development environment container (this takes a few minutes):
- `docker-compose build`

Start the environment container:
- `docker-compose up -d`

Spawn a shell inside the container:
- `./container`

## Environment
The [local.env](./assets/local.env) file can be modified to inject environment variable content into the container.

You can override the values set in this file by setting shell ENV variables prior to starting the container:
- `export GIT_HOOKS_PROTECTED_BRANCHES='.*'`
- `docker-compose kill` (Kill the current running container.)
- `docker-compose rm` (Remove the stopped container.)
- `docker-compose up -d` (Restart the dev environment, with a new container, containing the override.)
- `./container`

## Git Hooks
Git hooks are installed that will enforce linting and unit-testing on the specified branches.
The following environment variables can be used to customize this behavior:

- `GIT_HOOKS` (Set this value to 1 to enable the pre-commit hook)
- `GIT_HOOKS_PROTECTED_BRANCHES` (Customize this regex to specify the branches that should enforce the Git Hook on commit.)

## Installing a virtual environment on your host machine

The [scripts/hostmachine.sh](./scripts/hostmachine.sh) script does this for you.

It will use `pipenv` to create a virtual environment and install both requirements files in the assets folder.  
This is useful if you want to make your local IDE aware of what's installed.

(`pip install pipenv` or `brew install pipenv` may be necessary on your system.)
 
