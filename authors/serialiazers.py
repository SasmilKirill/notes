from rest_framework.serializers import ModelSerializer
from .models import Author



class AuthorModelSerializer(ModelSerializer)
    class Meta:
        model = Author
        fielsd = 'user_name, first_name, last_name, email '
        # fields = ('first_name',last_name')
        # excluse = ('last_name',)

class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BiographiesHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biographies
        fields = '__all__'

class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'