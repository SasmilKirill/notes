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




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES':[
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',

    ]:
    'DEFAULT_FILTER_BACKENDS':[ 'django_filters.rest_framework.DjangoFilterBackend'],
   #'DEFAULT_PAGINATION_CLASS' : 'rest_framework.paginationd.PageNumberPagination',
   #'PAGE_SIZE':1
   'DEFAULT_PERMISSION_CLASSES':[
       'rest.framework.permission.DjangoModelPermissionOrAnonReadOnly'
   ],
   'DEFAULT_AUTHENTICATION_CLASSES' ;[
       'rest_framework.authentication.BasicAuthentication',
       'rest_framework.authentication.SessionAuthentication',
       'rest_framework. authentication.TokenAuthentication',
   ]


}

REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS':
        'rest_framework.versioning.URLPathVersioning',
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
}

REST_FRAMEWORK = {
    #'DEFAULT_VERSIONING_CLASS':
'rest_framework.versioning.URLPathVersioning',
    #'DEFAULT_VERSIONING_CLASS':
'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_VERSIONING_CLASS':
'rest_framework.versioning.QueryParameterVersioning',
}

INSTALLED_APPS = [
    "django.contrib.staticfiles", # Required for GraphiQL
    "graphene_django"
]

GRAPHENE = {
    "SCHEMA": "library.schema.schema"
}

