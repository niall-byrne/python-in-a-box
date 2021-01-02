FROM python:3.7-slim AS base
MAINTAINER {{cookiecutter.email}}
ENV PYTHONUNBUFFERED 1
ENV PROJECT_NAME "{{cookiecutter.project_slug}}"
ENV PIB_CONFIG_FILE_LOCATION "/app/assets/cli.yml"
ENV POETRY_VIRTUALENVS_CREATE "false"
LABEL PROJECT={{cookiecutter.project_slug}}

# Mark Container
RUN echo "{{cookiecutter.project_slug}}" > /etc/container_release

# Install Base Dependencies
RUN apt-get update      && \
    apt-get upgrade -y  && \
    apt-get install -y     \
    bash                   \
    build-essential

# Setup directories
RUN mkdir -p /home/user /app
WORKDIR /app

# Copy the codebase
COPY . /app

# Create the runtime user, and enforce permissions
RUN useradd user -d /home/user        \
                 -s /bin/bash         \
                 -M                   \
 && chown -R user:user /home/user     \
 && chown -R user:user /app

ENV PATH "/home/user/.local/bin/:${PATH}"

# ======================================================

# Development Environment
FROM base AS development
LABEL ENVIRONMENT=DEVELOPMENT
ENV ENVIRONMENT=DEVELOPMENT

# Install Dev Dependencies
RUN apt-get install -y              \
    curl                            \
    golang-github-pelletier-go-toml \
    jq                              \
    openssh-client                  \
    shellcheck                      \
    sudo                            \
    tig                             \
    vim

# Add user to sudoers, and make the default user
RUN echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Set the runtime user
USER user

# Setup The Dev CLI
RUN pip install poetry pib_cli==0.0.4                 && \
    dev setup

CMD ["./{{cookiecutter.project_slug}}/container_init.sh"]

# ======================================================

# Production Environment
FROM base as production
LABEL ENVIRONMENT=PRODUCTION
ENV ENVIRONMENT=PRODUCTION

# Install Production Packages Only
RUN pip install poetry
RUN poetry install --no-dev --no-root

# Set the runtime user
USER user

CMD ["./{{cookiecutter.project_slug}}/container_init.sh"]
