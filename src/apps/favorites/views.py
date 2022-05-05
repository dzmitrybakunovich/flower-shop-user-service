from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteUserListView(APIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = FavoriteSerializer

    def post(self, request, item_id):
        favorites = Favorite.objects.filter(
            item_id=item_id
        )
        serializer = self.serializer_class(favorites, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class FavoriteCreateView(APIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = FavoriteSerializer

    def post(self, request, item_id):
        favorite = Favorite.objects.create(
            user=request.user,
            item=item_id,
        )
        favorite.save()
        return Response(status=status.HTTP_200_OK)
