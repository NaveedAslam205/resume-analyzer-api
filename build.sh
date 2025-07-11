#!/usr/bin/env bash

# Exit on any failure
set -o errexit
set -o xtrace

# Install project dependencies using Poetry
poetry install --no-interaction --no-root

# Activate the virtual environment manually
source "$(poetry env info --path)/bin/activate"

# Download spaCy model after spacy is installed
python -m spacy download en_core_web_sm

# Run the server (Render sets the PORT env variable)
exec uvicorn main:app --host=0.0.0.0 --port=${PORT:-10000}
