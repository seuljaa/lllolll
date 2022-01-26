from .common import *

DEBUG = False

# 운영서버 DB 정보
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lllolll',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}