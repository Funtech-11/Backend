import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', default='1@3$5^7*9)pOiUyTrEwQ')

DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'drf_spectacular',
    'rest_framework.authtoken',
    'users',
    'events',
    'djoser',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'funtech.urls'

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

WSGI_APPLICATION = 'funtech.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE', default='django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', default='postgres'),
        'USER': os.getenv('POSTGRES_USER', default='postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='postgres'),
        'HOST': os.getenv('DB_HOST', default='db'),
        'PORT': os.getenv('DB_PORT', default=5432),
    }
}

AUTH_USER_MODEL = "users.User"

# Password validation
VALIDATION = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'{VALIDATION}.UserAttributeSimilarityValidator'},
    {'NAME': f'{VALIDATION}.MinimumLengthValidator'},
    {'NAME': f'{VALIDATION}.CommonPasswordValidator'},
    {'NAME': f'{VALIDATION}.NumericPasswordValidator'},
]

# Rest
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
         'rest_framework.authentication.TokenAuthentication',
     ],
}
DJOSER = {
    'LOGIN_FIELD': 'email'
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Funtech API',
    'DESCRIPTION': 'Funtech Test Swagger API description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# ALLOWED_HOSTS = ['*']
# # CORS
# CORS_URLS_REGEX = r'^/api/.*$'
# CORS_ORIGIN_ALLOW_ALL = True

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cookie
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173"
# ]

# CORS_ALLOW_CREDENTIALS = True

ALLOWED_HOSTS = ['*']
# CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     'http://eventfun.ru/',
#     'http://84.252.73.12'
# ]
# CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]
# CORS_ALLOW_HEADERS = ["Accept", "Authorization", "Content-Type"]
CSRF_TRUSTED_ORIGINS = [
    'http://eventfun.ru/',
    'http://84.252.73.12/'
]
