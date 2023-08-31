"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3w409^22zp^z%)ic1wp8&a=nadrnict6l+f@=w0@%=(mk__l3k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myshop',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
    'rosetta',
    'parler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # comes after .SessionMiddleware because it needs to use the session
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# The order of middleware classes is very important because each middleware
# can depend on data set by other middleware executed previously.

ROOT_URLCONF = 'myshop.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

# see the list of all built-in context processors at
# https://docs.djangoproject.com/en/3.0/ref/templates/api/#built-in-templatecontext-processors.

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

from django.utils.translation import gettext_lazy as _
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

# The locale directory is the place where message files for your application will reside.
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATICFILES_DIRS = [
    BASE_DIR / "shop/static/css/",
    BASE_DIR / "static/css/",
    BASE_DIR / "static/admin",
]

import mimetypes
mimetypes.add_type("text/css", "css", True)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = 'media/'  # base URL that serves media files uploaded by users
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  # the local path where these files reside,

CART_SESSION_ID = 'cart'
# This is the key that you are going to use to store the cart in the user session.

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Braintree settings
# TODO: Replace the BRAINTREE_MERCHANT_ID,... values with the ones for your account.
BRAINTREE_MERCHANT_ID = '6nvmqgr9hybrrpjd'  # Merchant ID
BRAINTREE_PUBLIC_KEY = '65ysbqjmdn9vwjcz'  # Public Key
BRAINTREE_PRIVATE_KEY = 'e234593a4b10218d90e9c90b01476e04'  # Private Key

import braintree
BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

# You use Environment.Sandbox for integrating the sandbox.
# Once you go live and create a real account, you will need to change this to Environment.Production.
# celery -A myshop worker --pool=solo -l info
# rabbitmq-server
# celery -A myshop flower

PARLER_LANGUAGES = {
    # defines the available languages, en and es, for django-parler.
    None: (
        {'code': 'en'},
        {'code': 'es'},
    ),
    # specify default language en and indicate that it shouldn't hide untranslated content
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}

