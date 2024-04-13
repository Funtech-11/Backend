#!/bin/sh

sleep 10
python manage.py migrate
python manage.py load_data
gunicorn funtech.wsgi:application --bind 0:8000
