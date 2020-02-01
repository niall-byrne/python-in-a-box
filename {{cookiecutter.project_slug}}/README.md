# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Template Documentation

[Documentation](development/REFERENCE.md)

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

## Install the Project Packages on your Host Machine:
This is useful for making your IDE aware of what's installed in a venv.

- `pip install pipenv`
- `source scripts/dev`
- `dev setup` (Installs the requirements.txt in the `assets` folder.)
- `pipenv --venv` (To get the path of the virtual environment for your IDE.)

## CLI Reference
The CLI is enabled by default inside the container, and is also available on the host machine.

```
$ dev
Valid Commands:
 - lint
 - lint-validate
 - reinstall-requirements
 - setup
 - test
 - test-coverage
```
