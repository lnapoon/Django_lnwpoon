#!/bin/bash
echo "Building Django project on Vercel..."

# Install dependencies
if command -v uv &> /dev/null; then
    echo "Using uv for installation..."
    uv pip install --system -r requirements.txt
else
    echo "Using pip for installation..."
    python3 -m pip install --break-system-packages -r requirements.txt
fi

# Collect static files
python3 manage.py collectstatic --noinput --clear
