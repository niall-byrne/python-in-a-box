# Project Documentation

## {{ cookiecutter.project_name }}

{{ cookiecutter.description }}
{%- if cookiecutter.optional_sphinx_support == 'true' %}

[Project Documentation](https://{{cookiecutter.project_slug}}.readthedocs.io/)
{%- endif %}

### {{cookiecutter.git_base_branch|capitalize}} Branch Builds
- [![{{cookiecutter.project_slug}} Push Container](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}-push-container/badge.svg?branch={{cookiecutter.git_base_branch}})](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/actions)
- [![{{cookiecutter.project_slug}} Push Generic](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}-push-generic/badge.svg?branch={{cookiecutter.git_base_branch}})](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/actions)
- [![{{cookiecutter.project_slug}} Push Wheel](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}-push-wheel/badge.svg?branch={{cookiecutter.git_base_branch}})](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/actions)

### Production Branch Builds
- [![{{cookiecutter.project_slug}} Push Container](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}-push-container/badge.svg?branch=production)](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/actions)
- [![{{cookiecutter.project_slug}} Push Generic](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}-push-generic/badge.svg?branch=production)](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/actions)
- [![{{cookiecutter.project_slug}} Push Wheel](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}-push-wheel/badge.svg?branch=production)](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/actions)

### Release Automation
- [![{{cookiecutter.project_slug}} Release Container](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}-release-container/badge.svg)](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/actions)
- [![{{cookiecutter.project_slug}} Release Wheel](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/workflows/{{cookiecutter.project_slug}}-release-wheel/badge.svg)](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/actions)
{%- if cookiecutter.optional_sphinx_support == 'true' %}

### Documentation Builds
- [![Documentation Status](https://readthedocs.org/projects/{{cookiecutter.project_slug}}/badge/?version=latest)](https://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/?badge=latest)
{%- endif %}

## Quick Start Guide

You'll need to install:
 - [Docker](https://www.docker.com/) 
 - [Docker Compose](https://docs.docker.com/compose/install/)

Build the development environment container (this takes a few minutes):
- `docker-compose build`

Start the environment container:
- `docker-compose up -d`

Spawn a shell inside the container:
- `./container`

## Tooling Reference

Inside the container you'll find the Development CLI:
- Run the CLI without arguments to see the complete list of available commands: `dev`
- For more details see the [pib_cli](https://pypi.org/project/pib-cli/) Python Package.
- [Customize](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/tree/{{cookiecutter.git_base_branch}}/assets/cli.yml) the CLI to suit your needs.

## Git Hooks
The python library [pre-commit](https://pre-commit.com/) comes installed with a host of useful initial hooks:

## Default Installed Pre-Commit Hooks:
| Hook Name          | Description                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| check_container    | Encourages you to make commits inside the [PIB](https://github.com/niall-byrne/python-in-a-box) environment. |
| check_spelling     | Runs [aspell](http://aspell.net/) on your commit messages to prevent typos.                                  |
| commitizen         | Runs commitizen on your commit message to validate it.                                                       |
| gitleaks           | Runs [gitleaks](https://github.com/zricethezav/gitleaks) to scan for credential leaks.                       |
| protected_branches | Runs additional tests for branches marked as important.                                                      |
| shellcheck         | Runs [shellcheck](https://www.shellcheck.net/) on your shell scripts.                                        |
| pyproject.toml     | Runs [tomll](https://github.com/Ainiroad/go-toml) on your TOML configuration file.                           |
| yamllint           | Runs [yamllint](https://github.com/adrienverge/yamllint) on your YAML configuration files.                   |

Most of these hooks use values from [local.env](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/tree/{{cookiecutter.git_base_branch}}/assets/local.env) file that can be customized.
Furthermore, the spell check script manages its own [word dictionary](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/tree/{{cookiecutter.git_base_branch}}/.aspell.pws) that you can customize. 

## Installing a virtual environment, and the CLI on your host machine

The [scripts/extras.sh](https://github.com/{{cookiecutter.git_username}}/{{cookiecutter.project_slug}}/tree/{{cookiecutter.git_base_branch}}/scripts/extras.sh) script does this for you.

Source this script, and use the `dev` command on your host:
- `pip install poetry`
- `source scripts/extras.sh`
- `pib_setup_hostmachine` (to install the poetry dependencies)  
- `dev --help` (to run the cli outside the container)

This is most useful for making an IDE like pycharm aware of what's installed in your project.

> It is still always recommended to work inside the container, as you'll have access to the full managed python environment, 
> as well as any additional services you are running in containers.  

The dev CLI sometimes makes calls to binaries that are installed inside the container, as such it's not always practical to use it on your host machine.
