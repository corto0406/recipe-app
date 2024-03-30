import os
from pathlib import Path


# Base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Secret key
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-8hmo67$m5=-x9fwf%n0+_kcn6vx9^epx^^n0_kak$#1!g_u&^z')

# Debug mode
DEBUG = os.environ.get('DEBUG', 'False').lower() != 'true'

# Allowed hosts
ALLOWED_HOSTS = ['nemanja-food-3b44c7048bc6.herokuapp.com', '127.0.0.1', 'localhost']

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recipes',
    'users'
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'recipe_project.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# WSGI application
WSGI_APPLICATION = 'recipe_project.wsgi.application'

# Language code
LANGUAGE_CODE = 'en-us'

# Time zone
TIME_ZONE = 'UTC'

# Internationalization
USE_I18N = True

# Localization
USE_L10N = True

# Time zone support
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media', 'recipe_images')
MEDIA_URL = '/media/recipe_images/'

# Login redirect URL
LOGIN_REDIRECT_URL = '/'


