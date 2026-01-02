#!/bin/bash

# Build script for Vercel
pip install -r requirements.txt

# Collect static files
python BestPrice/manage.py collectstatic --noinput --clear
