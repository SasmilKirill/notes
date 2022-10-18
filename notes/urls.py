from django.contrib import admin
from django.urls import path, include


router = DefaultRouter()
router.register('authors', AuthorsModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token', obtain_auth-token),
]