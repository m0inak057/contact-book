#!/bin/bash

# Build script for Vercel
echo "Installing dependencies..."
pip3.12 install -r requirements.txt

echo "Collecting static files..."
python3.12 manage.py collectstatic --noinput --clear
