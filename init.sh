#!/bin/bash
python manage.py makemigrations && \
python manage.py migrate && \
python manage.py runserver
# python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', '', 'root123')" && \
# gunicorn django_demo.wsgi -b 0.0.0.0:8000
