from .base import *
from .local_settings import *

ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'pcsy',
		'USER': DEPOY_DB_USER,
		'PASSWORD': DEPLOY_DB_PASS,
		'HOST': '127.0.0.1',
		'PORT': DEPLOY_DB_PORT,
		'OPTIONS': {
			'charset': 'utf8mb4',
		}
	}
}

STATIC_DIR = BASE_DIR.parent
STATIC_ROOT = os.path.join(STATIC_DIR, 'static')
