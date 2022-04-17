from django.contrib import admin
from django.urls import path, include

api_v1_urlpatterns: list = [
    path('users/', include(('users.urls', 'users'), namespace='users')),
]

urlpatterns: list = [
    path('api/v1/', include(api_v1_urlpatterns)),
    path('admin/', admin.site.urls),
]
