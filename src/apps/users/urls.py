from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

from .views import RegisterView, UserListView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
    path('<uuid:uuid>/', UserDetailView.as_view(), name='user-detail'),
    path('sign-up/', RegisterView.as_view(), name='sign-up'),
    path('auth/jwt-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/jwt-token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
