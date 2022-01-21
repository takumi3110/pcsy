from .base import *
from .local_settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'pcsy',
		'USER': LOCAL_DB_USER,
		'PASSWORD': LOCAL_DB_PASS,
		'HOST': '127.0.0.1',
		'PORT': LOCAL_DB_PORT,
		'OPTIONS': {
			'charset': 'utf8mb4',
		}
	}
}
