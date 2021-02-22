#!/bin/bash

# Fail on error.
set -e

# Always flush output
export PYTHONUNBUFFERED=1

# Log command (for writing to stderr, unlike echo.)
log() { printf "%s\n" "$*" >&2; }

# Set some baseline variables.
PYTHON="${PYTHON:-/usr/bin/env python}"
MANAGE="${MANAGE:-$PYTHON manage.py}"

cd /app/code

uwsgi --ini /app/uwsgi.ini