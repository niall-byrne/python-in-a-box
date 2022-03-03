# Python-in-a-Box Environment Variables

## Docker Build Args

The [Dockerfile](../{{cookiecutter.project_slug}}/assets/Dockerfile) sets some modifiable parameters you can manipulate when building your container:

| Variable                     | Use Case                                                                                                              |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| BUILD_ARG_PYTHON_VERSION     | Set this value to override the default Python version your container is built for.  Useful for cross-version testing. |
| BUILD_ARG_ASPELL_LANGUAGE    | Set this value to override the language [aspell](http://aspell.net/) will be installed to support.                    |

## Default Environment Variables

The [Dockerfile](../{{cookiecutter.project_slug}}/assets/Dockerfile) sets some additional default values that you can override if needed:

| Variable                     | Use Case                                                                               |
|------------------------------|----------------------------------------------------------------------------------------|
| PROJECT_ROOT                 | The root path inside the container.                                                    |
| PROJECT_NAME                 | Set to the slug of your project name generated by cookiecutter.                        |
| PROJECT_AUTHOR               | Set to the author of your project, as entered into cookiecutter.                       |
| PYTHONUNBUFFERED             | Disables buffering in Python to ensure stdout is readily available.                    |
| VERSION_ASPELL               | The installed [aspell](http://aspell.net/) version as a string.                        |
| VERSION_GITLEAKS             | The installed [Gitleaks](https://github.com/zricethezav/gitleaks) version as a string. |
| VERSION_POETRY               | The installed [Poetry](https://python-poetry.org/) version as a string.                |

## Configurable Environment Variables

The [local.env](../{{cookiecutter.project_slug}}/assets/local.env) file contains all other environment content used inside the Docker container.  Here's the definitive guide to these values:

| Variable                     | Use Case                                                                                                                                                                                                       |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GIT_HOOKS_ASPELL_LANG        | A language code string used by the [aspell](http://aspell.net/) binary when spellchecking commit messages. See [this](../{{cookiecutter.project_slug}}/scripts/hooks/check_spelling.sh) hook.                  |
| GIT_HOOKS_ASPELL_ENCODING    | A file encoding string by the [aspell](http://aspell.net/) binary when spellchecking commit messages. See [this](../{{cookiecutter.project_slug}}/scripts/hooks/check_spelling.sh) hook.                       |
| GIT_HOOKS_PROTECTED_BRANCHES | A regex string used by [this](../{{cookiecutter.project_slug}}/scripts/hooks/protected_branches.sh) custom script to perform additional checks on matching branches.                                           |
| PIB_CONFIG_FILE_LOCATION     | A file path string used by the [pib_cli](https://pypi.org/project/pib-cli/) to find [this](../{{cookiecutter.project_slug}}/assets/cli.yml) configuration file, or another that you provide for customization. |
| PYTHONPATH                   | A path string used by Python to find imports in your project.                                                                                                                                                  |

Additional environment variable content your application needs can be added here for used in development, but as this file is checked in, you may want to add more environment files that you keep out of git.  Modify your [docker-compose.yml](../{{cookiecutter.project_slug}}/docker-compose.yml) to reference these additional "secret" files.