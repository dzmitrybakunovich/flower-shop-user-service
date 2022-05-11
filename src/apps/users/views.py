from rest_framework.decorators import parser_classes
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, \
    RetrieveAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import RegisterSerializer, UserSerializer, UpdateUserSerializer


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


class UserUpdateView(UpdateAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    lookup_field = 'uuid'
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    parser_classes = (MultiPartParser,)

# class CurrentUserView(APIView):
#     permission_classes = (
#         IsAuthenticated,
#     )
#     serializer_class = UserSerializer
#
#     def get(self, request):
#         serializer = self.serializer_class(request.user)
#         return Response(serializer.data)
