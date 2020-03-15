#!/usr/bin/env sh

set -o errexit
set -o nounset

cmd="$*"

if [ "$1" = 'launch-app' ]; then
    python run.py
elif [ "$1" = 'launch-tests' ]; then
    pytest tests
else
    exec "$cmd"
fi