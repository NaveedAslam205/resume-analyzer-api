#!/usr/bin/env bash

# Exit on any failure
set -o errexit

# Print each command before executing it
set -o xtrace

# Install spaCy model
python -m spacy download en_core_web_sm

# Run the server (Render sets the PORT env variable)
exec uvicorn main:app --host=0.0.0.0 --port=${PORT:-10000}
