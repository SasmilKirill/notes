



@api_view(['GET', 'POST']) ##'POST
@renderer_classes([JSONRenderer , BrowsableAPIRenderer])
def test(request) :
      if request.POST "POST"
         book = Book.objects.all()
         serializer = BookModelSerializer(boor, many=True)
         return Response({'test' :1})
         elif request.GET == 'GET':




class BookCreateAPIView(CreateAPIView) -
   renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer

class BookListAPIView(ListAPIView) :
   renderer_classes = [JSONRenderer, BrowsableAPIRenderer ]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer

class BookRetrieveAPIView(RetrieveAPIView) :
   renderer_classes = [JSONRenderer, BrowsableAPIRenderer ]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer

class BookDestroyAPIView(DestroyAPIView) :
   renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer






class BookViewSet|(ViewSet) :
   renderer_classes = [JSONRenderer, BrowsableAPIRenderer ]

   def list(self, request):
       book = Book.objects.all()
       serializer_class = BookModelSerializer (book, siany=True)
       return Response(serializer_class.data)

   def retrieve(self request, pk=None):
       book = get_object_or_404(Book, pk=pk)
       serializer_class = BookModelSerializer (book)
       return Response(serializer_class.data)

@action(detail=True, methods=['get'])
   def only(self, request, pk=None):
       book = Book.objects.get(id=pk)
       return Response({'book': book.name, 'id' :book.id})




