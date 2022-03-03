#!/bin/bash

# /hooks/post_gen_project.sh
# Initialize Git and Poetry after templating with cookiecutter.
# Filter Sphinx or Docstring linting configuration as needed.

# Host machine only.  This script is part of the template process.

# PIB_SKIP_GIT_INIT:        set to a value to skip the repository initialization
# PIB_SKIP_FMT_INIT:        set to a value to skip initial formatting
# PIB_SKIP_POETRY_INIT:     set to a value to skip poetry installation

FORMATTING_TYPE="{{ cookiecutter.formatting }}"
OPTION_DOCSTRINGS="{{ cookiecutter.optional_docstring_linting }}"
OPTION_SPHINX="{{ cookiecutter.optional_sphinx_support }}"

initialize_fmt() {

 if [[ "${FORMATTING_TYPE}" == "Niall's 2-Space Preference" ]]; then
    find . -name '*.py' -print0 | while read -r -d $'\0' FILE_NAME; do
      python -c "import re;source=open('${FILE_NAME}', 'r');contents=source.read();source.close();destination=open('${FILE_NAME}', 'w'); destination.write(re.sub(r'    ', '  ', contents));destination.close()"
    done
  fi

  if command -v yapf; then
    yapf -i --recursive .
  fi

}

initialize_git() {

  [[ -d .git ]] && return 0

  git init
  git stage .
  git commit -m "build(COOKIECUTTER): Initial Generation"
  git tag v0.0.0
  git checkout -b production
  git checkout master

}

initialize_poetry() {

  [[ -f "poetry.lock" ]] && return 0

  poetry lock

}

template_filter() {

  if [[ "${OPTION_DOCSTRINGS}" == "false" ]]; then
    rm .pydocstyle .pydocstyle.tests
  fi

  if [[ "${OPTION_SPHINX}" == "false" ]]; then
    rm .darglint .readthedocs.yml
    rm -rf documentation
  fi

}

main() {

  template_filter

  if [[ -z "${PIB_SKIP_POETRY_INIT}" ]]; then
    initialize_poetry
  fi

  if [[ -z "${PIB_SKIP_FMT_INIT}" ]]; then
    initialize_fmt
  fi

  if [[ -z "${PIB_SKIP_GIT_INIT}" ]]; then
    initialize_git
  fi

}

main
