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
- `cookiecutter https://github.com/shared-vision-solutions/python-in-a-box.git --checkout v0.0.6`

Give your project a name, and populate the other required template inputs.

> There is an optional feature to mount your ssh keys into the container to facilitate commits from inside the container.  
> I've found this approach preferable to bouncing back and forth between the container and the host machine.

Once the templating is finished:
- `cd <your new project director>`
- `docker-compose build`  (Build the docker environment, this will take a couple of minutes)
- `docker-compose up` (Start the environment, if you are running an app like flask or django or other containers in your environment, logs will be produced here.)
- Open a new shell in your terminal, and go to the same new project folder
- `./container` (Puts you inside the development environment)

Now open the project folder in your favorite IDE, or use [VIM](https://www.vim.org/) inside the container to begin writing code.

> You can now use `cz` to make [commitzen](https://github.com/commitizen-tools/commitizen) style commits, and have access to the `dev` command line interface to help you work

## Strict PEP Compliance

I personally prefer a 2 space indent.  This might not be your cup of tea.  No problem.

The [scripts/extras.sh](./{{cookiecutter.project_slug}}/scripts/extras.sh) script can help you out:
- `source scripts/extras.sh`
- `pib_prefer_black`

> This will patch your template to use black instead of yapf, and remove unncessary configuration files.
> Check in your changes, and you'll now be using black to achieve full PEP compliance.

Alternatively, modify your [.style.yapf](./{{cookiecutter.project_slug}}/.style.yapf) file to achieve the same results.

## Container

[python:3.7-slim](https://github.com/docker-library/python/tree/master/3.7/buster/slim)

## License

[MPL-2](LICENSE)

## Tooling Reference
The CLI is installed by default inside the container, and is also available on the host machine.
Run the CLI without arguments to see the complete list of available commands: `dev`

[The 'pib_cli' Python Package](https://pypi.org/project/pib-cli/)

The local CLI configuration is managed by the [cli.yml](./{{cookiecutter.project_slug}}/assets/cli.yml) file.

## Adding / Removing Dependencies For Your Project

#### Python Dependencies:

Use the [pyproject.toml](./{{cookiecutter.project_slug}}/pyproject.toml) file to store your project dependencies in accordance with [PEP 518](https://www.python.org/dev/peps/pep-0518/) and [Poetry Dependency Management](https://python-poetry.org/docs/pyproject/#dependencies-and-dev-dependencies).

Poetry is installed inside the container, so you can leverage this tool:
- [Adding Python Packages with Poetry](https://python-poetry.org/docs/cli/#add)
- [Removing Python Packages With Poetry](https://python-poetry.org/docs/cli/#remove)

#### OS Level Dependencies:

Modify the [Dockerfile](./{{cookiecutter.project_slug}}/assets/Dockerfile) to accomplish to this.
- Add to the base dependencies list if your package should be in both development and production
- Add to the dev dependencies list if it's a development only package

The container is using a [Debian](https://www.debian.org/) derived image, so [apt-get](https://linux.die.net/man/8/apt-get) is the package manager.

## Default Installed Python Packages:
| package    | Description                       |
| ---------- | --------------------------------- |
| bandit     | Finds common security issues      |
| commitizen | Standardizes commit messages      |
| isort      | Sorts imports                     |
| poetry     | Python Package Manager            |
| pylint     | Static Code Analysis              |
| pytest     | Test suite                        |
| pytest-cov | Coverage support for pytest       |
| sphinx     | Generating documentation          |
| safety     | Dependency vulnerability scanning |
| wheel      | Package distribution tools        |
| yamllint   | Lint yaml configuration files     |
| yapf       | Customizable Code Formatting      |

## Default Installed Container OS Packages
| package         | Description                                                 |
|-----------------|-------------------------------------------------------------|
| bash            |  with a customizable environment and shellcheck for linting |
| build-essential |  A collection of packages for compiling, linking            |
| curl            |  CLI based web client                                       |
| fish            |  Alternative Shell                                          |
| gitleaks        |  Scans for checked-in credentials                           |                            
| jq              |  processing json                                            |
| git, ssh        |  managing git commits                                       |
| shellcheck      |  BASH Linting                                               | 
| tig             |  managing git history                                       |
| tomll           |  a toml file linter, and formatter                          |
| vim             |  managing small edits, and git commit messages              |


## Customizing The Development Environment

After you initialize the template with cookiecutter, you'll likely want to customize the resulting development environment to suit your needs.  Here's a couple of quick examples to get you started...

### Webapps, APIs

Install your framework with poetry before making these modifications (see section above).  After everything noted below is suits your needs, rebuild your container:
`docker-compose build && docker-compose up`

For a webapp like [Flask](https://flask.palletsprojects.com/) or [Django](https://www.djangoproject.com/), you'll want to customize the container [init script](./{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/container_init.sh), as well as expose a port in the [docker-compose](./{{cookiecutter.project_slug}}/docker-compose.yml) file.

In the [docker-compose](./{{cookiecutter.project_slug}}/docker-compose.yml) file, find your service, and add a yaml line to include one or more exposed port(s):

```yaml
services:
  mywebapp:
    build:
      context: .
      dockerfile: assets/Dockerfile
      target: development
    env_file:
      - assets/local.env
    ports:
      - "127.0.0.1:8000:8000"
```

> Here `127.0.0.1` refers to your local dev machine, so you can reach your webservice in your browser

In the [init script](./{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/container_init.sh), modify either the `DEVELOPMENT` or `PRODUCTION` function, depending on the use case:
- Remove the line `while true; do sleep 1; done`
- Replace it with the command to start your development server:
  - `python manage.py runserver 0.0.0.0:8000` (for Django projects)
  - `FLASK_ENV=development flask run --host=0.0.0.0` (for Flask projects)

> Be sure to bind to 0.0.0.0 inside the container to expose the service to your host machine

### Adding Databases

Databases are fairly straightforward to add to your [docker-compose](./{{cookiecutter.project_slug}}/docker-compose.yml) file, expose them to your host machine if you want to use applications or tools you've installed to manage the database:

```yaml
services:
  mywebapp:
    build:
      context: .
      dockerfile: assets/Dockerfile
      target: development
    env_file:
      - assets/local.env
    ports:
      - "127.0.0.1:8000:8000"
  db:
    image: postgres:12.0-alpine
    ports:
      - "127.0.0.1:5432:5432"
    env_file:
      - assets/local.env
```

> `mywebapp` can now reach the database at `db:5432`

> To reach the same database on your host machine, build a connection string using `127.0.0.1:5432` 

> Consult the documentation for the database image you are using to learn about how to set credentials, and place any environment variables in the [local.env](./{{cookiecutter.project_slug}}/assets/local.env) file for your development environment (Do not check-in any production values here.)

## Configuration Files

Files are created in the project root folder for the following:

- [Bandit](https://bandit.readthedocs.io/en/latest/)
  - [.bandit](./{{cookiecutter.project_slug}}/.bandit)
  - [.banditrc](./{{cookiecutter.project_slug}}/.bandit.rc)
- [Default Software License](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/licensing-a-repository)
  - [LICENSE](./{{cookiecutter.project_slug}}/LICENSE)
- [Git](https://git-scm.com/)
  - [.gitignore](./{{cookiecutter.project_slug}}/.gitignore)
- [Read The Docs](https://readthedocs.org/)
  - [.readthedocs.yml](./{{cookiecutter.project_slug}}/.readthedocs.yml)
- [poetry](https://python-poetry.org/)  
  - [pyproject.toml](./{{cookiecutter.project_slug}}/pyproject.toml)
- [pytest](https://docs.pytest.org/en/stable/)
  - [pytest.ini](./{{cookiecutter.project_slug}}/pytest.ini)
- [yamllint](https://github.com/adrienverge/yamllint)
  - [.yamllint.yml](./{{cookiecutter.project_slug}}/.yamllint.yml)  
- [yapf](https://readthedocs.org/)
  - [.style.yapf](./{{cookiecutter.project_slug}}/.style.yapf)
  - [.yapfignore](../pib_cli/pib_cli/.yapfignore)
  
## PEP 518 Compliance

- [pyproject.toml](./{{cookiecutter.project_slug}}/pyproject.tom) centralizes configuration for the following:
  - [coverage](https://coverage.readthedocs.io/en/coverage-5.3.1/)
  - [isort](https://pycqa.github.io/isort/)
  - [poetry](https://python-poetry.org/) ([scripts/extras.sh](./{{cookiecutter.project_slug}}/scripts/extras.sh))
  - [pylint](https://www.pylint.org/)
  - [pypi.org](https://pypi.org/)

More configurations will be moved into this centralized file as the individual tools support this standard.

## Third Party Integrations

Integrations with the following third party services are configured during templating:

- [Github Workflows](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions)
  - [workflows](./{{cookiecutter.project_slug}}/.github/workflows)
- [Docker Hub](https://hub.docker.com/)
  - [release_container.yml](./{{cookiecutter.project_slug}}/.github/workflows/release_container.yml)
- [pypi.org](https://pypi.org/)
  - [pyproject.toml](./{{cookiecutter.project_slug}}/pyproject.toml)
- [Read The Docs](https://readthedocs.org/)
  - [.readthedocs.yml](./{{cookiecutter.project_slug}}/.readthedocs.yml)
