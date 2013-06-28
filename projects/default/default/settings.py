"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
here = lambda path: os.path.join(BASE_DIR, path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Override this in local_settings.py.'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = (
    #('Your Name', 'your@example.com'),
)
MANAGERS = ADMINS

SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')

EMAIL_SUBJECT_PREFIX = "[{{ project_name }}] "

DEFAULT_FROM_EMAIL = "{{ project_name }} <hi@{{ project_name }}.com>"

# Enable the following if you're proxying behind nginx or another server
# and the server passes the scheme as X-SCHEME.
# E.g. for nginx, add "proxy_set_header X-Scheme $scheme;" to the location block.
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    here("templates"),
)

ALLOWED_HOSTS = []

SITE_URL = "https://www.{{ project_name }}.com"
SITE_NAME = "{{ project_name }}"

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'default.urls'

WSGI_APPLICATION = 'default.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
            },
    'console': {
        'level': 'DEBUG',
        'class': 'logging.StreamHandler',
        }

    },
   'loggers': {
        'django.request': {
            # Remove "mail_admins" below to disable mailing admins.
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = here('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_ROOT = here('static')
STATIC_URL = '/static/'


# Load environment-specific variables from local_settings.py.
try:
    from local_settings import *
except ImportError, exp:
    pass

# Define an INSTALLED_APPS section in your local_settings.py
# to have them loaded.
try:
    INSTALLED_APPS += LOCAL_INSTALLED_APPS
except:
    pass

# Same with MIDDLEWARE_CLASSES.
try:
    MIDDLEWARE_CLASSES += LOCAL_MIDDLEWARE_CLASSES
except:
    pass
