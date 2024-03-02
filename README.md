## 1. project setting

### init
```bash
mkdir django-web
cd django-web
python3 -m venv venv
source venv/bin/activate
pip install django djangorestframework
django-admin startproject mysite .
python manage.py startapp polls
code .
```

### settings.py
```py
import os
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'bootstrap4',
]

TIME_ZONE = 'Asia/Seoul'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 2. MVT

python manage.py makemigrations polls
 python manage.py sqlmigrate polls 0001
 python manage.py migrate

 python manage.py shell


 ## 3. admin
 python manage.py createsuperuser
 python manage.py runserver