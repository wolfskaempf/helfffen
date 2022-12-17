"""
Django settings for helfffen project.
"""
import os
from pathlib import Path

from environs import Env

env = Env(eager=False)
env.read_env(override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str(
    "HELFFFEN_SECRET_KEY",
    "django-insecure-thai0hai4vieYi5zeu2jeiwie2raetoV9aiQuoh9phahkeopeoviechu3choph5o",
)

DEBUG = env.bool("HELFFFEN_DEBUG", False)

# Allowed hosts and CSRF trusted origins
ALLOWED_HOSTS = env.list("HELFFFEN_ALLOWED_HOSTS", [])
CSRF_TRUSTED_ORIGINS = env.list("HELFFFEN_CSRF_TRUSTED_ORIGINS", [])

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helfffencore.apps.HelfffencoreConfig',
    'widget_tweaks',  # https://github.com/jazzband/django-widget-tweaks
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helfffen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "src" / "templates"],
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

WSGI_APPLICATION = 'helfffen.wsgi.application'

# Database
if env.bool("USE_SQLITE", False):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        },
    }
else:
    with env.prefixed("HELFFFEN_POSTGRES_"):
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": env.str("DB", 'postgres'),
                "USER": env.str("USER", 'postgres'),
                "PASSWORD": env.str("PASSWORD", 'postgres'),
                "HOST": env.str("HOST", 'postgres'),
                "PORT": env.int("PORT", 5432),
            },
        }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'de-DE'

TIME_ZONE = 'Europe/Berlin'

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "helfffencore" / "static",
]

# WhiteNoise Configuration
# http://whitenoise.evans.io/en/stable/#quickstart-for-django-apps
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


if not env.bool("IGNORE_ENV", False):
    env.seal()
