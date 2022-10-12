ROOT_URLCONF = 'Library.url'

TEMPLATES = [
    {
        'BACKEND': 'django. template.backends.django.DjangoTemplates'
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django. template.context_processors.debug',
                'django. tempLate.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Library.wsgi - application’