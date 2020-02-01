FROM python:3.7-slim
MAINTAINER {{cookiecutter.email}}
LABEL PROJECT={{cookiecutter.project_slug}}

ENV PYTHONUNBUFFERED 1

# Mark Container
RUN echo "{{cookiecutter.project_slug}}" > /etc/container_release

# Install Dependencies
RUN apt-get update   && \
    apt-get install -y  \
    bash                \
    build-essential     \
    jq                  \
    openssh-client      \
    shellcheck          \
    sudo                \
    tig                 \
    vim

# Setup directories
RUN mkdir -p /home/user /app
WORKDIR /app

# Copy codebase and bash environment
COPY . /app
COPY development/bash /home/user/

# Create the runtime user, and change permissions
RUN useradd user -d /home/user        \
                 -s /bin/bash         \
                 -M                   \
 && chown -R user:user /home/user     \
 && chown -R user:user /app           \
 && echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER user

# Setup The Dev CLI
RUN scripts/commander.sh setup
