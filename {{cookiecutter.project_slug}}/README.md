# Project Documentation

## {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

[Project Documentation](https://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/)

### Develop Branch Builds
- [![{{cookiecutter.project_slug}} Generic Push](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}%20Generic%20Push/badge.svg?branch=develop)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions)
- [![{{cookiecutter.project_slug}} Wheel Push](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}%20Wheel%20Push/badge.svg?branch=develop)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions)

### Master Branch Builds
- [![{{cookiecutter.project_slug}} Generic Push](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}%20Generic%20Push/badge.svg?branch=master)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions)
- [![{{cookiecutter.project_slug}} Wheel Push](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}%20Wheel%20Push/badge.svg?branch=master)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions)

### Release Builds
- [![{{cookiecutter.project_slug}} Release Container](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}%20Release%20Container/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions)
- [![{{cookiecutter.project_slug}} Release Wheel](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}%20Release%20Wheel/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions)

## Getting Started With Python In A Box

Refer to the [python-in-a-box documentation](https://github.com/Shared-Vision-Solutions/python-in-a-box) to get oriented, and learn how to manage your development environment.

## Tooling Reference
The CLI is instsalled by default inside the container, and is also available on the host machine.
Run the CLI without arguments to see the complete list of available commands: `dev`

[The 'pib_cli' Python Package](https://pypi.org/project/pib-cli/)

The local CLI configuration is managed by the [cli.yml](./assets/cli.yml) file.

## Development Dependencies

You'll need to install:
 - [Docker](https://www.docker.com/) 
 - [Docker Compose](https://docs.docker.com/compose/install/)

## Build and Start the Development Environment

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

It will use [poetry](https://python-poetry.org/) to create a virtual environment and install both requirements files in the assets folder.  
This is useful if you want to make your local IDE aware of what's installed.

(`pip install poetry` or `brew install poetry` may be necessary on your system.)

Executing the script will install (or re-install) a complete poetry virtual environment.
- [poetry.lock](./poetry.lock)
- [pyproject.toml](./pyproject.toml)

Running the script the `shell` argument, is a convenience wrapper around `poetry shell`.

