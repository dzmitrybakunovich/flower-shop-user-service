from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

api_v1_urlpatterns: list = [
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path(
        'notifications/',
        include(
            ('notifications.urls', 'notifications'),
            namespace='notifications')
    ),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]

urlpatterns: list = [
    path('api/v1/', include(api_v1_urlpatterns)),
    path('admin/', admin.site.urls),
]
