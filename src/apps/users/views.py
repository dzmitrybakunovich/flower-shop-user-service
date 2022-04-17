from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import RegisterSerializer, UserSerializer


class RegisterView(CreateAPIView):
    permission_classes = (
        AllowAny,
    )
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserListView(ListAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    lookup_field = 'uuid'
    queryset = User.objects.all()
    serializer_class = UserSerializer
