from PPDApp.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "TestDB",
        'USER': "postgres",
        'PASSWORD': "1234",
        'HOST': "localhost",
        'PORT': '5432',
    }
}
TESTING = True
