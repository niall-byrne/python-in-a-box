# Python-in-a-Box Configuration Files

The following configuration files are created in the project root folder:

- [Bandit](https://bandit.readthedocs.io/en/latest/)
  - [.bandit](../{{cookiecutter.project_slug}}/.bandit)
  - [.banditrc](../{{cookiecutter.project_slug}}/.bandit.rc)
- [Default Software License](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/licensing-a-repository)
  - [LICENSE](../{{cookiecutter.project_slug}}/LICENSE)
- [Git](https://git-scm.com/)
  - [.gitignore](../{{cookiecutter.project_slug}}/.gitignore)
- [Hadolint](https://github.com/hadolint/hadolint)
  - [.hadolint.yml](../{{cookiecutter.project_slug}}/.hadolint.yml)
- [Read The Docs](https://readthedocs.org/)
  - Only if you opt in for [Sphinx](https://www.sphinx-doc.org/en/master/) support. 
  - [.readthedocs.yml](../{{cookiecutter.project_slug}}/.readthedocs.yml)
- [poetry](https://python-poetry.org/)  
  - [pyproject.toml](../{{cookiecutter.project_slug}}/pyproject.toml)
- [pydocstyle](https://python-poetry.org/)  
  - Only if you opt in for docstring linting. 
  - [.pydocstyle](../{{cookiecutter.project_slug}}/.pydocstyle)
  - [.pydocstyle.tests](../{{cookiecutter.project_slug}}/.pydocstyle)
- [yamllint](https://github.com/adrienverge/yamllint)
  - [.yamllint.yml](../{{cookiecutter.project_slug}}/.yamllint.yml)  
