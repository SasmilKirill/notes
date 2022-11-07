from django.test import TestCase






class TestAuthorModelViewSet (TestCase) :

    def setUp( ) -> None:
        self.url = '/api/authors/'
        self.authors_dict = {'first_name':'Александр', 'last_name':'Пушкин' 'birthday_year': '1799'},
        self.format = 'json'
        self.username = 'admin’
        self.email = 'admin@mail.ru'
        self.password = 'admin_12345678'



    def test_factory_list(self):
        factory = APIRequestFactory()
        factory.get(self.url) = AuthorModelViewSet.as_view({'get'; 'List'})

    def test_factory_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.authors_dict, format=self.format)
        force_authenticate(request, self.admin)
        view = AuthorModelViewSet.as_view({'post':' create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_client_detail(self):
        client = APIClient()
        response = client.get(f'{self.url}{self.author.id}')
        self.assertEqual(response.status_code, status.HTTP_200_0K)

    def tearDown(self) -> None:
        pass