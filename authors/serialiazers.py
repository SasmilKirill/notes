from rest_framework.serializers import ModelSerializer
from .models import Author



class AuthorModelSerializer(ModelSerializer)
    from rest_framework import serializers
    from .models import Author, Book
    class AuthorSerializer(serializers.ModelSerializer):
        class Meta:

            model = Author

    fields = '__all__'

    class AuthorSerializerBase(serializers.ModelSerializer):
        class Meta:

            model = Author

    fields = ('name',)

    class BookSerializerBase(serializers.ModelSerializer):

    #
    class Meta:
        model = Book

    fields = '__all__'

    class BookSerializer(serializers.ModelSerializer):
        author = AuthorSerializer()

    class Meta:
        model = Book

    fields = '__all__'
