import os
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
  long_description = fh.read()

with open(os.path.join("assets", "requirements.txt")) as fh:
  assets = [line for line in fh.read().strip().split('\n') if line[0] != "#"]

packages = find_packages()
packages.remove('{{cookiecutter.project_slug}}.tests')

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.0.1",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.description}}",
    entry_points='''
[console_scripts]
{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.app:cli
    ''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}",
    packages=packages,
    package_data={
        '{{cookiecutter.project_slug}}': [os.path.join("data", "*.txt")],
    },
    include_package_data=True,
    install_requires=assets,
    license="License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.0,<3.8.0',
)
