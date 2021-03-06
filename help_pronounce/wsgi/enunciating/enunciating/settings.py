"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from socket import gethostname

from help_pronounce.libs import secrets
from help_pronounce.get_package_dir import get_package_dir


DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = f'{get_package_dir()}'
WSGI_DIR = f'{get_package_dir()}/wsgi'
REPO_DIR = f'{get_package_dir()}/..'
DATA_DIR = f'{get_package_dir()}/data'

sys.path.append(os.path.join(REPO_DIR, 'libs'))
SECRETS = secrets.getter(os.path.join(DATA_DIR, 'secrets.json'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    gethostname(), # For internal OpenShift load balancer security purposes.
    '34.87.199.167',
    'helppronounce.com', # First DNS alias (set up in the app)
    'www.helppronounce.com', # Second DNS alias (set up in the app)
]

# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    #'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# GETTING-STARTED: change 'myproject' to your project name:
ROOT_URLCONF = 'help_pronounce.wsgi.enunciating.enunciating.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [DJ_PROJECT_DIR + '/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'help_pronounce.wsgi.enunciating.enunciating.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # GETTING-STARTED: change 'db.sqlite3' to your sqlite3 database:
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT2 = os.path.join(WSGI_DIR, 'static')
print(STATIC_ROOT2)
STATICFILES_DIRS = [
    STATIC_ROOT2
]

STATIC_ROOT = os.path.expanduser('~/static')

TEMPLATE_DIRS = (
    DJ_PROJECT_DIR + '/templates/',
)
