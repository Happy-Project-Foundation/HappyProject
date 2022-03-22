from pathlib import Path
import os
import django_heroku as dh

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: change in production
SECRET_KEY = 'happyProj3ctbyShantho$h&B1rnadin3rick'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["happyproject.birnadine.guru", "happyprojectapp.herokuapp.com"]

INSTALLED_APPS = [
    # my apps
    'clientauth.apps.ClientAuthConfig',
    'blog.apps.BlogConfig',
    'gallery.apps.GalleryConfig',
    'home.apps.HomeConfig',
    'hub.apps.HubConfig',
    'watchdog.apps.WatchdogConfig',

    # third-party apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'happy_project.urls'

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

WSGI_APPLICATION = 'happy_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("POSTGRESQL_DBNAME"),
        'USER': os.getenv("POSTGRESQL_USER"),
        'PASSWORD': os.getenv("POSTGRESQL_PASSWD"),
        'HOST': os.getenv("POSTGRESQL_HOST"),
        'PORT': int(os.getenv("POSTGRESQL_PORT")),

    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'watchdog.HappyPerson'
LOGIN_URL = 'clientauth:login'
LOGIN_REDIRECT_URL = 'api:stray'
LOGOUT_REDIRECT_URL = 'home:index'

dh.settings(locals(), test_runner=False)

