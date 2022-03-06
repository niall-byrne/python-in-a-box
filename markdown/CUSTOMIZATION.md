# Python-in-a-Box Customization Guide

You'll want to modify the default template to suit your needs.  These key files will get you started:

| File                                                                                        | Use Case                                                                                              |                                                                                                  
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [app.py](../{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/app.py)             | Trash this noise and write your own goodness.  (Update the pyproject.toml and testing_shim to match.) |
| [.bash_customize](../{{cookiecutter.project_slug}}/assets/.bash_customize)                  | An entrypoint you can use to customize the default BASH environment, or maybe add another shell?      |
| [cli.yml](../{{cookiecutter.project_slug}}/assets/cli.yml)                                  | Customize the development CLI here to streamline your team's development process.                     |
| [Dockerfile](../{{cookiecutter.project_slug}}/assets/Dockerfile)                            | There's a multistage Dockerfile here with build targets for Development and Production.               |
| [docker-compose](../{{cookiecutter.project_slug}}/docker-compose.yml)                       | The standard development docker-compose file.  Add containers and networking as needed.               |
| [docker-compose.production](../{{cookiecutter.project_slug}}/docker-compose.production.yml) | A Production targeting docker-compose file.  Test your container in multiple environments.            |
| [local.env](../{{cookiecutter.project_slug}}/assets/local.env)                              | Set environment variables for use in development.  Keep sensitive secrets out of here!                |
| [pyproject.toml](../{{cookiecutter.project_slug}}/pyproject.toml)                           | Manage your project's Python dependencies here with Poetry.                                           |
| [scripts](../{{cookiecutter.project_slug}}/scripts)                                         | A collection of goodies to further ease the pains of Development.                                     |
| [testing_shim](../{{cookiecutter.project_slug}}/testing_shim)                               | When building an invocable command (like a CLI), having this handy is convenient for testing.         |

### An Example Webapp

For a webapp like [Flask](https://flask.palletsprojects.com/) or [Django](https://www.djangoproject.com/), you'll want to customize the container [init script](../{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/container_init.sh), as well as expose a port in the [docker-compose](../{{cookiecutter.project_slug}}/docker-compose.yml) file.

In the [docker-compose](../{{cookiecutter.project_slug}}/docker-compose.yml) file, find your service, and add a yaml line to include one or more exposed port(s):

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

In the [init script](../{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/container_init.sh), modify either the `DEVELOPMENT` or `PRODUCTION` function, depending on the use case:
- Remove the line `while true; do sleep 1; done`
- Replace it with the command to start your development server:
  - `python manage.py runserver 0.0.0.0:8000` (for Django projects)
  - `FLASK_ENV=development flask run --host=0.0.0.0` (for Flask projects)

> Be sure to bind to 0.0.0.0 inside the container to expose the service to your host machine

### Adding Databases

Databases are fairly straightforward to add to your [docker-compose](../{{cookiecutter.project_slug}}/docker-compose.yml) file, expose them to your host machine if you want to use applications or tools you've installed to manage the database:

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

> Consult the documentation for the database image you are using to learn about how to set credentials, and place any environment variables in the [local.env](../{{cookiecutter.project_slug}}/assets/local.env) file for your development environment (Do not check-in any production values here.)

## Remote Debugging 

It's fairly easy to add a process to the container to facilitate remote debugging with [VSC](https://code.visualstudio.com/) or other tools.
- Add your debug server to the codebase:
  - inside the container you'll need your debug process to bind to `0.0.0.0` so that any virtualization layer (such as Docker on OSX) doesn't obscure the IP address.
- In the [docker-compose](../{{cookiecutter.project_slug}}/docker-compose.yml) file you'll want to add a `ports` entry:
  - eg. ```- "127.0.0.1:5678:5678"``` (expose port 5678 inside the container to 127.0.0.1:5678 on my laptop.)
- Connect your client to 127.0.0.1:5678 and debug at will.
