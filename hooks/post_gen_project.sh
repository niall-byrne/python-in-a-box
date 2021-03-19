#!/bin/bash

git init
git stage .
git commit -m "Cookiecutter: Initial Generation"
git symbolic-ref HEAD refs/heads/master
git tag v0.0.0
