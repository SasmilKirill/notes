
lpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),







    path('api/list/', BookListAPIView.as_view()),
    path('api/create/', BookCreateAPIView.as_view()),
    path('api/update/<int:pk>/', BookUpdateAPIView.as_view()),
    path('api/delete/<int:pk>/', BookDestroyAPIView.as_view()),
    path('api/detail/<int:pk>/', BookRetrieveAPIView.as_view()),