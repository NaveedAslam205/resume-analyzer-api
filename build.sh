#!/usr/bin/env bash

# Exit on any failure
set -o errexit
# Print each command before executing it
set -o xtrace

# Install dependencies with poetry
poetry install --no-root

# Download spaCy model
poetry run python -m spacy download en_core_web_sm

# Run the server
exec poetry run uvicorn main:app --host=0.0.0.0 --port=${PORT:-10000}
