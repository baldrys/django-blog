import os

SECRET_KEY = 'ce*bg5=9-(90w8)-m*j*_ev9=h=@#^sy%2&nts3h*&mvs&gvbv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'django-blog',

        'USER': 'postgres',

        'PASSWORD': '12345',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}
