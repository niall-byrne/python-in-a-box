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

## CLI Reference

```
$ dev
Valid Commands:
 - lint
 - lint-validate
 - reinstall-requirements
 - setup
 - shell
 - test
 - test-coverage
```
