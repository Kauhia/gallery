import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def env_var(key, default=None):
    val = os.environ.get(key, default)
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val

ENV = env_var('ENV', 'dev')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_var('SECRET_KEY', 'n_et%4&rofx797lq9(6wd4%d3l6yl+xjs89z#1d@2r6@krvd3@')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_var('DEBUG', True)

ALLOWED_HOSTS = env_var('ALLOWED_HOSTS','').split()


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'images',
    'comments',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'gallery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['gallery/templates'],
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

WSGI_APPLICATION = 'gallery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
if env_var('ENV', 'dev') == 'dev':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
elif env_var('ENV', 'dev') == 'prod':
    DATABASES = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'NAME': env_var('DB_NAME'),
            'USER': env_var('DB_USER'),
            'PASSWORD': env_var('DB_PASSWORD'),
            'HOST': env_var('DB_SERVER_NAME'),
            'PORT': env_var('DB_SERVER_PORT'),
            'OPTIONS': {
                'driver': 'SQL Server Native Client 11.0',
                'MARS_Connection': 'True',
            }
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'Europe/Helsinki'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# upload folder for user content
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'


if env_var('ENV', 'dev') == 'prod' and env_var('LOGGING', False):
    LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'filters': {
        'require_debug_false': {
          '()': 'django.utils.log.RequireDebugFalse'
        }
      },
      'handlers': {
        'logfile': {
          'class': 'logging.handlers.WatchedFileHandler',
          'filename': 'D:/home/site/wwwroot/error.log'
        },
      },
      'loggers': {
        'django': {
          'handlers': ['logfile'],
          'level': 'ERROR',
          'propagate': False,
        },
      }
    }