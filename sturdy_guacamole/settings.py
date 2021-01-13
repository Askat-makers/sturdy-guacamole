"""
Django settings for sturdy_guacamole project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import decouple
import config
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# ji5sx6f6r20#pv8@codb#=g=b5#+76rej^-#04_9@4k77&!u(v
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['aqueous-plateau-10138.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'material.admin',
    'material.admin.default',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',

    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sturdy_guacamole.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sturdy_guacamole.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
            default=config('DATABASE_URL')
        )
}

# 'default': {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'sturdy_guacamole',
#     'USER': 'tof',
#     'PASSWORD': '1',
#     'HOST': '127.0.0.1',
#     'PORT': '5432',
# }


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MATERIAL_ADMIN_SITE = {
    'HEADER': 'NurPressAdminPanel',  # Admin site header
    'TITLE': 'Hulahoo',  # Admin site title
    'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
    'MAIN_BG_COLOR':  'black',  # Admin site main color, css color should be specified
    'MAIN_HOVER_COLOR':  'black',  # Admin site main hover color, css color should be specified
    'PROFILE_PICTURE':  'admin/img/pexels-eberhard-grossgasteiger-1367192.jpg',  # Admin site profile picture (path to static should be specified)
    'PROFILE_BG':  'admin/img/pexels-eberhard-grossgasteiger-1367192.jpg',  # Admin site profile background (path to static should be specified)
    'LOGIN_LOGO':  'admin/img/login-rounded-right.png',  # Admin site logo on login page (path to static should be specified)
    'LOGOUT_BG':  'admin/img/login-rounded.png',  # Admin site background on login/logout pages (path to static should be specified)
    'SHOW_THEMES':  True,  # Show default admin themes button
    'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': True,  # Hide side navbar by default
    'SHOW_COUNTS': True,  # Show instances counts for each model
    'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
        'sites': 'send',
    },
    'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
        'site': 'contact_mail',
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
