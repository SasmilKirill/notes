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

urlpatterns = [
...
path('api/users/0.1', include('userapp.urls', namespace='0.1')),
path('api/users/0.2', include('userapp.urls', namespace='0.2')),


schema_view = get_schema_view(
   openapi.Info(
      title="Library",
      default_version='0.1',
      description="Documentation to out project",
      contact=openapi.Contact(email="admin@admin.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
