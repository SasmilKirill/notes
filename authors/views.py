from django.shortcuts import render


from rest_framework.viewsets import ModelViewSet

from .models import Author,Book,BiographiesHyperlinkedModeSerializer
from .serialiazers import AuthorModelSerializer

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

class BiographiesModelViewSet(ModelViewSet):
    queryset = Biographies.objects.all()
    serializer_class = BiographiesHyperlinkedModeSerializer

    #def get_queryset(selfself):
     #   return Author.objects.get(id=1)

