import os
from pathlib import Path
from decouple import config

# Stripe settings
STRIPE_API_KEY_PUBLISHABLE = "pk_test_51HlNc7H8vBDql4tfjbZZFBPlm2tlujhKXVi1w1UDEdiZUpewuaYPZHHNKX155jKzvUNTf3GHbv6xZAE87CHcEnIt00OHT0PFCI"
STRIPE_API_KEY_HIDDEN = "sk_test_51HlNc7H8vBDql4tf1MYMD3NxLvwB4aAPY2tkXkT9CrRHN4tiGuEeoSc9DyQ8jImKVgwpOrQy3qWI8KrnuGS1nH8e00R9rqp8ZS"
PAYPAL_API_KEY_PUBLISHABLE = 'AfHdIrzKKDcNMypnDfQJlGY0aIcEv2VwD441P8SKdX0ssh_ItQBUNMNx356QUgfEGdg-VKw4sAJa9wu9'
PAYPAL_API_KEY_HIDDEN = 'EBy_IgJByIrgrbbCawtdU3MdyV_tSQVtmaIxuC0tK8qRTTsd09Yvp8F-5vTgjDR9KIyh7SG7JehOIAYS'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")   # this replace the secret key in .env file (ignored by git)
                                    # create a .env file and write SECRET_KEY = '...'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Authentication
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'cart'
LOGOUT_REDIRECT_URL = 'frontpage'

# Gmail configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'duegattibot@gmail.com'
EMAIL_HOST_PASSWORD = 'Egha9ags1992'


# Cart settings
SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'apps.core',
    'apps.store',
    'apps.cart',
    'apps.order',
    'apps.coupon',
    'apps.userprofile',
    'apps.newsletter',
    'apps.shipping'
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

ROOT_URLCONF = 'duegatti.urls'

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
                'apps.store.context_processors.menu_categories',
                'apps.cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'duegatti.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '/home/duegatti/duegatti/static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# HTTPS settings -- Change to TRUE when in production
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

# HSTS settings -- Change to TRUE when in production
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
