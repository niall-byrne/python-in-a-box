FROM python:3.7-alpine
MAINTAINER {{cookiecutter.email}}
LABEL PROJECT={{cookiecutter.project_slug}}

ENV PYTHONUNBUFFERED 1

# Setup directories
RUN mkdir -p /home/user /app
WORKDIR /app

# Copy codebase and bash environment
COPY . /app
COPY development/bash /home/user/

# Install Dependencies
RUN apk add --no-cache  \
    alpine-sdk          \
    bash                \
    jq                  \
    openssh-client      \
    protoc              \
    protobuf-dev        \
    shellcheck          \
    tig                 \
    vim

# Install Pipenv
RUN pip install pipenv

# Create the runtime user, and change permissions
RUN adduser -D user --home /home/user \
                    --shell /bin/bash \
                    --no-create-home  \
 && chown -R user:user /home/user     \
 && chown -R user:user /app
USER user

# Setup The Dev CLI
RUN scripts/commander.sh setup

CMD ["bash"]
