ARG PYTHON_VERSION={{cookiecutter.python_version}}
FROM python:$PYTHON_VERSION-slim AS base

LABEL maintainer "{{cookiecutter.email}}"
LABEL project "{{cookiecutter.project_slug}}"
LABEL environment ""

ENV PYTHONUNBUFFERED 1
ENV PROJECT_NAME "{{cookiecutter.project_slug}}"
ENV PIB_CONFIG_FILE_LOCATION "/app/assets/cli.yml"
ENV GITLEAKSVERSION "v7.2.0"

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

# Create the runtime user, and enforce permissions
RUN useradd user -d /home/user        \
                 -s /bin/bash         \
                 -M                   \
 && chown -R user:user /home/user     \
 && chown -R user:user /app

# Include the local binary folder in PATH
ENV PATH "/home/user/.local/bin/:${PATH}"

# ======================================================

# Poetry Intermediary
FROM base AS poetry

LABEL environment ""

# Install Latest Poetry
RUN pip install --no-cache-dir poetry

# ======================================================

# Development Environment
FROM poetry AS development
LABEL environment DEVELOPMENT
ENV ENVIRONMENT DEVELOPMENT

# Install Dev Dependencies
RUN apt-get install -y              \
    --no-install-recommends         \
    curl                            \
    fish                            \
    golang-github-pelletier-go-toml \
    jq                              \
    openssh-client                  \
    shellcheck                      \
    sudo                            \
    tig                             \
    vim

# Install Git Leaks
RUN curl --fail -sL "https://github.com/zricethezav/gitleaks/releases/download/${GITLEAKSVERSION}/gitleaks-linux-amd64"    \
    -o /usr/bin/gitleaks                                                                                                && \
    chmod +x /usr/bin/gitleaks

# Add user to sudoers, and make the default user
RUN echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Set the runtime user
USER user

# Copy the poetry configuration
COPY pyproject.toml poetry.lock /app/

# Cache Dependencies
RUN poetry install --no-root -E docs

# Copy the Codebase
COPY . /app

# Create A Symlink For the Bash Customizations
RUN ln -sf /app/assets/.bash_customize /home/user/.bash_customize

# Setup The Dev CLI
RUN poetry run dev setup-bash

CMD ["./{{cookiecutter.project_slug}}/container_init.sh"]

# ======================================================

# Pre Production Environment
FROM poetry as pre_production

LABEL environment "PRE_PRODUCTION"

ENV ENVIRONMENT "PRE_PRODUCTION"

# Set the runtime user
USER user

# Copy the poetry configuration
COPY pyproject.toml poetry.lock /app/

# Export the lock file
RUN poetry export --without-hashes -f requirements.txt -o /app/requirements.txt

# Copy the codebase
COPY . /app

# ======================================================

# Production Environment
FROM base as production

LABEL environment "PRODUCTION"

ENV ENVIRONMENT "PRODUCTION"

# Set the runtime user
USER user

# Copy the requirements.txt file from pre_production
COPY --from=pre_production /app/requirements.txt /app/requirements.txt

# Install Production Packages Only
RUN pip --no-cache-dir install -r requirements.txt

# Copy the codebase
COPY . /app

CMD ["./{{cookiecutter.project_slug}}/container_init.sh"]
