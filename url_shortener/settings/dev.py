from base import *

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'url_shortener',
        'HOST': 'url-shortener.crj2xxc2oczo.ap-southeast-1.rds.amazonaws.com',
        'PORT': 5432,
        'USER': 'shailendra_kumar',
        'PASSWORD': 'dosomething'
    }
}
