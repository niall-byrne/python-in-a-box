# Python Development CookieCutter Template

A [cookiecutter](https://cookiecutter.readthedocs.io/) based Python [3.7/3.8/3.9/3.10] dockerized development environment.

##### Master Branch:
[![Python In A Box Self Test](https://github.com/niall-byrne/python-in-a-box/workflows/Python%20In%20A%20Box%20Self%20Test/badge.svg?branch=master)](https://github.com/niall-byrne/python-in-a-box/actions)

##### Production Branch:
[![Python In A Box Self Test](https://github.com/niall-byrne/python-in-a-box/workflows/Python%20In%20A%20Box%20Self%20Test/badge.svg?branch=production)](https://github.com/niall-byrne/python-in-a-box/actions)

## About

This project provides extensive CLI tooling and automation inside a container, specifically for working on Python projects. 

Batteries are included:
- functional CI on day one
- preconfigured Docker and Docker Compose files
- preconfigured pre-commit Git hooks
- structured commit enforcement
- an automated changelog
- preconfigured code formatters and linters
- preconfigured documentation generation
- a customizable `dev` CLI to orchestrate everything
- a lot more (too much to list here, just try it out...)

![Demo Image](https://i.ibb.co/sqddjYb/render1646245029095.gif)

## Project Requirements

#### Operating System
 - A [Linux](https://wikipedia.org/wiki/Linux) or [OSX](https://wikipedia.org/wiki/MacOS) based host machine
 - [Windows](https://wikipedia.org/wiki/Microsoft_Windows) based host machines will need both [Bash](https://docs.microsoft.com/windows/wsl/install) and [Docker with Linux Containers](https://docs.microsoft.com/virtualization/windowscontainers/deploy-containers/linux-containers)

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


4. Once the templating is finished:
- `cd <your new project directory>`
- `docker-compose build`  (Build the docker environment, this will take a couple of minutes.)
- `docker-compose up` (Start the environment, the logs from your [Flask](https://flask.palletsprojects.com/) or [Django](https://www.djangoproject.com/) app, or any other process or container, will appear here.)
- Open a new shell in your terminal, and go to the same new project folder
- `./container` (Puts you inside the development environment, time to break things.)

Now open the project folder in your favorite IDE, or use [VIM](https://www.vim.org/) inside the container to begin writing code.

> Inside the container?<br>
> You can now use `cz` to make structured commits with [Commitizen](https://github.com/commitizen-tools/commitizen). <br>
> You have access to the `dev` CLI to help you work.  It brings all the installed tooling together under a single CLI. <br>
> You'll find [Coverage](https://coverage.readthedocs.io/), [Mypy](https://mypy.readthedocs.io/), [Pylint](https://pylint.pycqa.org/) and [Pytest](https://docs.pytest.org/) pre-configured with sane defaults, ready to go.

A configurable base branch will be created, allowing you to manage a separate `production` branch in [GitHubFlow](https://docs.github.com/get-started/quickstart/github-flow) or [GitLabFlow](https://docs.gitlab.com/ee/topics/gitlab_flow.html) style.

## Working with Git inside Docker Containers

Python-in-a-Box advocates using your favorite IDE on your host machine as your normally would, but doing your CLI development work *inside* the container.
As such there are a couple of keys points to think through:

### How will you manage your ssh keys?

The PIB approach is to mount your local `.ssh` folder inside your Docker container to make it available to Git and SSH as needed.  This folder should be kept strictly separate from any code dependencies and be consumed only by these development tools.

- This is *NOT* adding the keys to your code base, but instead making them available to your development tooling.
- The keys are *NOT* added to the Dockerfile, they are injected at runtime by Docker.
- The inclusion of [TruffleHog](https://github.com/trufflesecurity/trufflehog) in PIB is there to enforce the separation.

There may be other strategies that work, and we'd love to hear about them, but this is the most tried and true approach that we have found.  

To use this strategy answer `true` then Cookiecutter asks you if you want to `include_ssh_keys` in your template.

**Using a password on your Git SSH key provides an additional layer of security that's recommended.**

### How will you manage your git configuration?

The PIB approach is to mount your local Git configuration inside the Docker Container to handle this seamlessly.  

- The PIB container is a blank playground that needs to be customized from scratch.  
- PIB handles setting up Python and Development tooling, but you'll need to configure Git to make it your own. 
- The configuration is *NOT* added to the Dockerfile, it is injected at runtime by Docker.

To use this strategy answer `true` when Cookiecutter asks you if you want to `include_gitconfig` or `include_gitconfig_global` in your template.  
(Depending on your local Git configuration you may have one or both of these files.)

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

The template renders complete working CI/CD for [Github Actions](https://docs.github.com/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions).  The caveat is that you'll need to configure some [Github Secrets](https://docs.github.com/actions/security-guides/encrypted-secrets) to make it all work seamlessly.  Consult the individual [workflow](./{{cookiecutter.project_slug}}/.github/workflows) files to figure out what values you need. 

## Configuration and Control

There's a handy index to all the configuration files in the template [here](./markdown/CONFIGURATION.md).
  
## Centralized Configuration (PEP 518 Compliance)

- [pyproject.toml](./{{cookiecutter.project_slug}}/pyproject.toml) centralizes configuration for the following:
  - [bandit](https://bandit.readthedocs.io/)
  - [commitizen](https://commitizen-tools.github.io/commitizen/)
  - [coverage](https://coverage.readthedocs.io)
  - [isort](https://pycqa.github.io/isort/)
  - [mypy](https://mypy.readthedocs.io)
  - [poetry](https://python-poetry.org/) ([scripts/extras.sh](./{{cookiecutter.project_slug}}/scripts/extras.sh))
  - [pylint](https://pylint.pycqa.org/)
  - [pytest](https://docs.pytest.org)
  - [yapf](https://github.com/google/yapf)

More configurations will be moved into this centralized file as the individual tools support this standard.

## Integrations

Integrations with the following third party services are configured during templating:

- [Github Actions](https://docs.github.com/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions)
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
