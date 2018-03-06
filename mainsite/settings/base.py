"""
Django settings for ucsf_dashboard project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j^xyylufaz=la&&ko1+p0(qo*2-hxdo#$4zptq&z=ezn-ny3kn'




# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

HOME_PAGE = "/dashboards/home/overview/"
LOGIN_URL = "/dashboards/0/home/welcome/"
LOGIN_REDIRECT_URL = "/"

# Application definition

PREREQ_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    #'debug_toolbar',
]

PROJECT_APPS = [
    'xf_crud',
    'xf_system',
    'uc_dashboards',
    'crispy_forms',
    'library',
    'uc_dashboards.templatetags.getattribute',
    'uc_dashboards.templatetags.dashgent_filters',
    'uc_dashboards.templatetags.iif',
    'this_dashboard',
    'mainsite',


]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

MIDDLEWARE = [
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'library.middleware.LibraryMiddleware',
]



ROOT_URLCONF = 'mainsite.urls'

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
#                'django.core.context_processors.static',
#                'django.template.context.static',
                'django.contrib.messages.context_processors.messages',
                'uc_dashboards.context_processors.include_login_form',
                'library.middleware.load_app_assets_in_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'mainsite.wsgi.application'

DASHGENT_PAGES = 'dashboards'

EXTRA_JS_ASSETS = ('library_js',)
EXTRA_CSS_ASSETS = ('library_css',)

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),

    },
#    'some_my_sql': {
#        'NAME': 'mysql_db',
#        'ENGINE': 'django.db.backends.mysql',
#        'USER': 'readonly',
#        'PORT': '3307',
#        'HOST': '127.0.0.1',
#        'PASSWORD': 'readonly',
#    },
    'ibbs':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../IBBS.db'),

    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = '/media/'
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = ''
CKEDITOR_JQUERY_URL = os.path.join(STATIC_URL, 'gla/vendors/jquery/dist/jquery.min.js')
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'skin': 'moono-lisa',
        'width': '100%'
    },
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
FIXTURE_DIRS = (os.path.join(PROJECT_ROOT, 'uc_dashboards/fixtures'),)

##FIXTURE_DIRS = (
#   os.path.join(BASE_DIR, 'uc_dashboards/fixtures'),
#)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

INTERNAL_IPS = ('127.0.0.1',)


gettext = lambda s: s
LANGUAGES = (
    ('en-gb', gettext('English')),
    ('pt', gettext('Portuguese')),
    ('nl', gettext('Dutch')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en-gb'

LANGUAGE_COOKIE_NAME = "lc"
