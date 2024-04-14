#!/bin/sh

sleep 15

python manage.py migrate

source ./.env
echo "from users.models import User; User.objects.create_superuser(username='$ADMIN_USERNAME', first_name='$ADMIN_FIRST_NAME', last_name='$ADMIN_LAST_NAME', password='$ADMIN_PASSWORD')" | python manage.py shell

python manage.py load_data

gunicorn funtech.wsgi:application --bind 0:8000
