from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import RegisterView, UserListView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
    path('<uuid:uuid>/', UserDetailView.as_view(), name='user-detail'),
    path('sign-up/', RegisterView.as_view(), name='sign-up'),
    path('auth/jwt-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
