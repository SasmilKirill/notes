from django.shortcuts import render


from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serialiazers import AuthorModelSerializer

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

    #def get_queryset(selfself):
     #   return Author.objects.get(id=1)