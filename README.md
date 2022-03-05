# Python Development CookieCutter Template

A [cookiecutter](https://cookiecutter.readthedocs.io/) based Python [3.7/3.8/3.9/3.10] dockerized development environment.

##### Master Branch:
[![Python In A Box Self Test](https://github.com/niall-byrne/python-in-a-box/workflows/Python%20In%20A%20Box%20Self%20Test/badge.svg?branch=master)](https://github.com/niall-byrne/python-in-a-box/actions)

##### Production Branch:
[![Python In A Box Self Test](https://github.com/niall-byrne/python-in-a-box/workflows/Python%20In%20A%20Box%20Self%20Test/badge.svg?branch=production)](https://github.com/niall-byrne/python-in-a-box/actions)

##### Version 1.0.0 Compatibility

Please be aware that version 1.0.0 has introduced some incompatible changes with the CLI configuration:
- Some minor changes will be required to keep your configuration compatible.
- Please see the latest [pib_cli](https://pypi.org/project/pib-cli/) release for details.

## About

This project provides extensive CLI tooling and automation inside a docker container for working on Python projects. 

Batteries are included:
- functional CI on day one
- preconfigured Docker and Docker Compose files
- preconfigured git hooks
- structured commit enforcement
- an automated changelog
- preconfigured code formatters and linters
- preconfigured documentation generation
- a customizable `dev` command to orchestrate everything
- a lot more (too much to list here, just try it out...)

![Demo Image](https://i.ibb.co/sqddjYb/render1646245029095.gif)

## Project Requirements

#### Operating System
 - A [Linux](https://en.wikipedia.org/wiki/Linux) or [OSX](https://en.wikipedia.org/wiki/MacOS) based host machine
 - [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows) based host machines will need both [Bash](https://docs.microsoft.com/en-us/windows/wsl/install) and [Docker](https://www.docker.com/) with [Linux Containers](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/linux-containers)

#### Software Requirements
 - [Python](https://www.python.org/)  (3.7, 3.8, 3.9 or 3.10)
 - [Docker](https://www.docker.com/)
 - [Docker Compose](https://docs.docker.com/compose/install/)
 - [Cookiecutter](https://cookiecutter.readthedocs.io/)
 - [Poetry](https://python-poetry.org/)
 

## Quick Start Guide

1. Start by making sure Docker and Docker Compose are both installed.
   - They are bundled together in most modern Docker distributions


2. Install Poetry and Cookiecutter, and instantiate the template:
   - `pip install cookiecutter poetry`
   - `cookiecutter https://github.com/niall-byrne/python-in-a-box.git`


3. Give your project a name, and populate the other required template inputs.

> The Python-in-a-Box approach to development suggests that you always work INSIDE the container.
> To facilitate this, there is an optional feature to mount your SSH keys into the container.  
> This allows you to push commits from the container using your credentials without making your ssh keys part of the container.
> Be aware of it, and use the included [Gitleaks](https://github.com/zricethezav/gitleaks) integrations to ensure your container stays safe.

4. Once the templating is finished:
- `cd <your new project directory>`
- `docker-compose build`  (Build the docker environment, this will take a couple of minutes)
- `docker-compose up` (Start the environment, if you are running an app like [Flask](https://flask.palletsprojects.com/) or [Django](https://www.djangoproject.com/) or other containers are in your environment, logs will be produced here.)
- Open a new shell in your terminal, and go to the same new project folder
- `./container` (Puts you inside the development environment)

Now open the project folder in your favorite IDE, or use [VIM](https://www.vim.org/) inside the container to begin writing code.

> You can now use `cz` to make [commitzen](https://github.com/commitizen-tools/commitizen) style commits, and have access to the `dev` command line interface to help you work

A configurable base branch will be created, allowing you to manage a separate `production` branch in [gitlabflow](https://docs.gitlab.com/ee/topics/gitlab_flow.html) style.

## Container Base Images

- [python:3.7-slim](https://github.com/docker-library/repo-info/blob/master/repos/python/remote/3.7-slim.md)
- [python:3.8-slim](https://github.com/docker-library/repo-info/blob/master/repos/python/remote/3.8-slim.md)
- [python:3.9-slim](https://github.com/docker-library/repo-info/blob/master/repos/python/remote/3.9-slim.md)
- [python:3.10-slim](https://github.com/docker-library/repo-info/blob/master/repos/python/remote/3.10-slim.md)

## Template License

[MPL-2](LICENSE)

- Modify the template however you like!
- This does not affect your software, license it however you like.

## What does this thing come with?

It's batteries included.

This template is brimming with practical Python libraries and open-source binary tools that enable clean, fast development.  You can find the complete list of installed software [here](./markdown/DEPENDENCIES.md).

Of special note is the [Development CLI](./{{cookiecutter.project_slug}}/assets/cli.yml):
- Run the CLI without arguments to see the complete list of available commands: `dev`
- For more details see the [pib_cli](https://pypi.org/project/pib-cli/) Python Package.
- [Customize](./{{cookiecutter.project_slug}}/assets/cli.yml) the CLI to suit your needs.

## Customizing your Development Environment (Webapps, APIs, CLIs...)

After you initialize the template with cookiecutter, you'll likely want to customize the resulting development environment to suit your needs.
You can find a more in-depth guide to customizations [here](./markdown/CUSTOMIZATION.md).

You'll also need to know about the environment variables in use.  There's a [guide](./markdown/ENVIRONMENT.md) for that too.

## Setting up CI/CD

The template renders complete working CI/CD for [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions).  The caveat is that you'll need to configure some [Github Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to make it all work seamlessly.  Consult the individual [workflow](./{{cookiecutter.project_slug}}/.github/workflows) files to figure out what values you need. 

## Configuration and Control

There's a handy index to all the configuration files in the template [here](./markdown/CONFIGURATION.md).
  
## Centralized Configuration (PEP 518 Compliance)

- [pyproject.toml](./{{cookiecutter.project_slug}}/pyproject.toml) centralizes configuration for the following:
  - [bandit](https://bandit.readthedocs.io/en/latest/)
  - [commitizen](https://commitizen-tools.github.io/commitizen/)
  - [coverage](https://coverage.readthedocs.io/en/stable/)
  - [isort](https://pycqa.github.io/isort/)
  - [mypy](https://mypy.readthedocs.io/en/stable/)
  - [poetry](https://python-poetry.org/) ([scripts/extras.sh](./{{cookiecutter.project_slug}}/scripts/extras.sh))
  - [pylint](https://www.pylint.org/)
  - [pytest](https://docs.pytest.org/en/stable/)
  - [yapf](https://github.com/google/yapf)

More configurations will be moved into this centralized file as the individual tools support this standard.

## Integrations

Integrations with the following third party services are configured during templating:

- [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions)
  - [workflows](./{{cookiecutter.project_slug}}/.github/workflows)
- [Docker Hub](https://hub.docker.com/)
  - [release_container.yml](./{{cookiecutter.project_slug}}/.github/workflows/release_container.yml)
- [pypi.org](https://pypi.org/)
  - [pyproject.toml](./{{cookiecutter.project_slug}}/pyproject.toml)
- [Read The Docs](https://readthedocs.org/) 
  - Only if you opt in for [Sphinx](https://www.sphinx-doc.org/) support. 
  - [.readthedocs.yml](./{{cookiecutter.project_slug}}/.readthedocs.yml)

## Production Containers

There is an additional [docker-compose.yml](./{{cookiecutter.project_slug}}/docker-compose.production.yml) file for creating production containers.
This gives you the opportunity to incorporate further testing in the CI/CD pipeline, and make local modifications.

Leveraging [multi stage](https://docs.docker.com/develop/develop-images/multistage-build/) Docker builds, this container keeps Poetry out of the mix, and aims to give you a bare-bones version of your application with a narrower attack plane.

(You'll need to create an `assets/production.env` file that resembles your [assets/local.env](./{{cookiecutter.project_slug}}/assets/local.env) file, and integrate with your CD process.)
