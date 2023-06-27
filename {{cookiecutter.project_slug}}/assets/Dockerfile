ARG BUILD_ARG_PYTHON_VERSION={{cookiecutter.python_version}}

FROM python:${BUILD_ARG_PYTHON_VERSION}-slim AS base

ARG BUILD_ARG_ASPELL_LANGUAGE="en"
ARG BUILD_ARG_CONTAINER_GID=1000
ARG BUILD_ARG_CONTAINER_UID=1000

LABEL maintainer="{{cookiecutter.email}}"
LABEL project="{{cookiecutter.project_slug}}"
LABEL environment="stage1"

ENV PIB_CONFIG_FILE_LOCATION "/app/assets/cli.yml"
ENV PIB_DOCUMENTATION_ROOT "/app/documentation"
ENV PIB_PROJECT_NAME "{{cookiecutter.project_slug}}"

ENV PROJECT_NAME "${PIB_PROJECT_NAME}"
ENV PROJECT_AUTHOR "{{cookiecutter.author}}"

ENV PYTHONUNBUFFERED "1"

ENV VERSION_ASPELL "aspell-${BUILD_ARG_ASPELL_LANGUAGE}=*"
ENV VERSION_TOMLL "v1.9.4"
ENV VERSION_TRUFFLEHOG "3.20.0"
ENV VERSION_POETRY "poetry>=1.2.0"

# Mark Container
RUN echo "1.0.0" > /etc/container_pib_version                       && \
    echo "{{cookiecutter.project_slug}}" > /etc/container_release

# Install Base Dependencies
RUN apt-get update               && \
    apt-get upgrade -y           && \
    apt-get install -y              \
    --no-install-recommends         \
    bash=5.*                        \
    build-essential=12.*         && \
    rm -rf /var/lib/apt/lists/*

# Create the runtime user, and enforce permissions
RUN groupadd user -g "${BUILD_ARG_CONTAINER_GID}"
RUN useradd user -d /home/user                    \
                 -s /bin/bash                     \
                 -u "${BUILD_ARG_CONTAINER_UID}"  \
                 -g "${BUILD_ARG_CONTAINER_GID}"  \
                 -m

# Setup directories
RUN mkdir -p /app
RUN chown -R user:user /app
WORKDIR /app

# Include the local binary folder in PATH
ENV PATH "/home/user/.local/bin/:${PATH}"

# ======================================================

# Poetry Intermediary
FROM base AS poetry

LABEL environment="stage2"

# Install Poetry
# hadolint ignore=DL3013
RUN pip install --no-cache-dir "${VERSION_POETRY}" setuptools

# ======================================================

# Development Environment
FROM poetry AS development
LABEL environment="DEVELOPMENT"
ENV ENVIRONMENT DEVELOPMENT

# Install Dev Dependencies
# hadolint ignore=DL3008
RUN apt-get update                      && \
    apt-get install -y                     \
    --no-install-recommends                \
    "${VERSION_ASPELL}"                    \
    curl=7.88.*                            \
    fish=3.6.*                             \
    jq=1.6*                                \
    openssh-client=1:9.*                   \
    shellcheck=0.9.*                       \
    sudo=1.9.*                             \
    tig=2.5.*                              \
    vim=2:9.*

# Install tomll
COPY scripts/utilities/install_tomll_linux.sh .
RUN bash install_tomll_linux.sh &&   \
    rm install_tomll_linux.sh

# Install Trufflehog
COPY scripts/utilities/install_trufflehog_linux.sh .
RUN bash install_trufflehog_linux.sh &&   \
    rm install_trufflehog_linux.sh

# Add user to sudoers, and make the default user
RUN echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Set the runtime user
USER user

# Copy the poetry configuration
COPY pyproject.toml *.lock /app/

# Cache Dependencies
RUN poetry install --no-root -E dev

# Copy the Codebase
COPY . /app

# Install the Application
RUN poetry install -E dev

# Create A Symlink For the Bash Customizations
RUN ln -sf /app/assets/.bash_customize /home/user/.bash_customize

# Enforce git repository permissions
USER root
RUN chown -R user:user /app
USER user

# Setup The Dev CLI, bootstrapping the current version of pib_cli
RUN poetry run dev @pib container setup

CMD ["bash", "-cl", "./{{cookiecutter.project_slug}}/container_init.sh"]

# ======================================================

# Pre Production Environment
FROM poetry as pre_production

LABEL environment="PRE_PRODUCTION"

ENV ENVIRONMENT "PRE_PRODUCTION"

# Set the runtime user
USER user

# Copy the poetry configuration
COPY pyproject.toml *.lock /app/

# Export the lock file
{%- if cookiecutter.include_lock_file|lower == "false" %}
RUN poetry lock{% endif %}
RUN poetry export --without-hashes -f requirements.txt -o /app/requirements.txt

# ======================================================

# Production Environment
FROM base as production

LABEL environment="PRODUCTION"

ENV ENVIRONMENT "PRODUCTION"

# Set the runtime user
USER user

# Copy the requirements.txt file from pre_production
COPY --from=pre_production /app/requirements.txt /app/requirements.txt

# Install Production Packages Only
RUN pip --no-cache-dir install -r requirements.txt

# Copy the codebase
COPY . /app

# Enforce codebase permissions
USER root
RUN chown -R user:user /app
USER user

CMD ["./{{cookiecutter.project_slug}}/container_init.sh"]
