#!/bin/bash

git init
git checkout -b master
git stage .
git commit -m "build(Cookiecutter): Initial Generation"
git symbolic-ref HEAD refs/heads/master
git tag v0.0.0
