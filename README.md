## 1. project setting

### init
```bash
mkdir django-web
cd django-web
python -m venv venv
source venv/bin/activate
pip install django djangorestframework
django-admin startproject mysite .
python manage.py startapp polls
code .
```

### innit(Windows)
```bash
python -m venv venv
source ./venv/Scripts/activate
pip install pyautogui
pip install keyboard
pip install pynput

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

### migration
```bash
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001
python manage.py migrate

python manage.py shell
```

### admin
```bash
python manage.py createsuperuser
python manage.py runserver
```


## 2. tests
```bash
python manage.py test polls
```


## 3. templates

```bash

python -c "import django; print(django.__path__)"
python -m pip install django-debug-toolbar
```

## 4. mysql 

```bash
# Assume you are activating Python 3 venv
brew install mysql mysql-client pkg-config
export PKG_CONFIG_PATH="$(brew --prefix)/opt/mysql-client/lib/pkgconfig"

pip install mysqlclient
```


## 5. crawling

```bash
python manage.py startapp crawling


pip install requests
pip install beautifulsoup4

# pip3 install --upgrade pip
# pip3 install tk
# brew install python-tk
# brew install python-tk@3.12


ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install --cask tint
brew install tkinter

brew install python-tk@3.9
sudo port install py311-tkinter
brew install python-tk

pip install pyautogui
```

## 6. excel

```bash
pip install openpyxl
```

## 7. selenium

```bash
pip install selenium
pip list
pip install --upgrade pip
pip3 install --upgrade pip
pip install --upgrade selenium
pip install webdriver_manager

```