#!/bin/bash

git init
git stage .
git commit -m "Cookiecutter: Initial Generation"
git checkout -b develop
git symbolic-ref HEAD refs/heads/develop
