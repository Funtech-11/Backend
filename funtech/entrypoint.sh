#!/bin/sh

python manage.py migrate
python manage.py load_data
# python funtech/manage.py load_test_data
gunicorn funtech.wsgi:application --bind 0:8000
