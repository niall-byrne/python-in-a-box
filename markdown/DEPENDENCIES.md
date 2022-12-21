# Managing Dependencies with Python-in-a-Box

#### Python Dependencies:

Use the [pyproject.toml](../{{cookiecutter.project_slug}}/pyproject.toml) file to store your project dependencies in accordance with [PEP 518](https://www.python.org/dev/peps/pep-0518/) and [Poetry Dependency Management](https://python-poetry.org/docs/pyproject/#dependencies-and-dev-dependencies).

Poetry is installed inside the container, so you can leverage this tool:
- [Adding Python Packages with Poetry](https://python-poetry.org/docs/cli/#add)
- [Removing Python Packages With Poetry](https://python-poetry.org/docs/cli/#remove)

The Poetry lock file itself is an OPTIONAL component for your dev environment, and depending on your project you may wish to exclude it from the codebase and your Docker container.  You are given the option to do so during the templating process.

#### OS Level Dependencies:

Modify the [Dockerfile](../{{cookiecutter.project_slug}}/assets/Dockerfile) to accomplish to this.
- Add to the base dependencies list if your package should be in both development and production
- Add to the dev dependencies list if it's a development only package

The container is using a [Debian](https://www.debian.org/) derived image, so [apt-get](https://linux.die.net/man/8/apt-get) is the package manager.

## Default Installed Python Packages:
See the [pib_cli](https://github.com/niall-byrne/pib_cli) documentation for the complete list of installed packages.

## Default Installed Container OS Packages
| package         | Description                                                 |
|-----------------|-------------------------------------------------------------|
| bash            |  with a customizable environment and shellcheck for linting |
| build-essential |  A collection of packages for compiling, linking            |
| curl            |  CLI based web client                                       |
| fish            |  Alternative Shell                                          |
| jq              |  processing json                                            |
| git, ssh        |  managing git commits                                       |
| shellcheck      |  BASH Linting                                               | 
| tig             |  managing git history                                       |
| tomll           |  a toml file linter, and formatter                          |
| trufflehog      |  Scans for checked-in credentials                           |                            
| vim             |  managing small edits, and git commit messages              |
