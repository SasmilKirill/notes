import graphene
from graphene_django import DjangoObjectType
from mainapp.models import Book, Author

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
schema = graphene.Schema(query=Query)


class BookType(DjangoObjectType):
    class Meta:
        model = Book

    fields = '__all__'

    class Query(graphene.ObjectType):
        all_books = graphene.List(BookType)

    def resolve_all_books(root, info):
        return Book.objects.all()

class AuthorType(DjangoObjectType):
        class Meta:

            model = Author

    fields = '__all__'



class Query(graphene.ObjectType):
    books_by_author_name = graphene.List(BookType,
name=graphene.String(required=False))

    def resolve_books_by_author_name(self, info, name=None):
        books = Book.objects.all()

    if name:
        books = books.filter(author__name=name)
    return books

    class AuthorMutation(graphene.Mutation):
        class Arguments:

            birthday_year = graphene.Int(required=True)

    id = graphene.ID()
    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, birthday_year, id):
        author = Author.objects.get(pk=id)

    author.birthday_year = birthday_year
    author.save()
    return AuthorMutation(author=author)

    class Mutation(graphene.ObjectType):
        update_author = AuthorMutation.Field()



    schema = graphene.Schema(query=Query)


