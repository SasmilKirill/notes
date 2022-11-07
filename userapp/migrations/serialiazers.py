



class AuthorModelSerializer(ModelSerializer):
   class Meta:
   model = Author
   fields = ('username', 'email')
   #fields = ('first_name','last_name')
   #exclude = ('first_name')

class BiographyHyperlinkedModelSerializer(ModelSerializer) :
   class Meta:
   model = Biography
   fields = ('username', 'email', 'firs_tname', 'last_name')