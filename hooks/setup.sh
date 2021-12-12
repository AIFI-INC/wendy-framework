#!/bin/bash -e

cp hooks/pre-commit .git/hooks/
chmod a+x .git/hooks/*
echo -e "Copied!"