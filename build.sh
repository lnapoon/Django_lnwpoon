#!/bin/bash
echo "Building Django project on Vercel..."

# Install dependencies
if command -v uv &> /dev/null; then
    echo "Using uv to build in virtual environment..."
    uv venv --python 3.12 .venv
    source .venv/bin/activate
    uv pip install -r requirements.txt
    python manage.py collectstatic --noinput --clear
else
    echo "Using standard pip to build in virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install -r requirements.txt
    python3 manage.py collectstatic --noinput --clear
fi
