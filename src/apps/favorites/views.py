from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Favorite
from .serializers import FavoriteSerializer

from notifications.tasks import send_mail


class FavoriteNotifyView(APIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = FavoriteSerializer

    def post(self, request, item_id):
        recipients = list(Favorite.objects.filter(
            item_id=item_id
        ).values_list('user_id', flat=True)
                          )
        print(recipients)

        send_mail.s(
            subject='qqq',
            message='qwqeqwe',
            to_email=recipients,
        ).apply_async()
        return Response(status=status.HTTP_200_OK)


class FavoriteCreateView(APIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = FavoriteSerializer

    def post(self, request, item_id):
        favorite = Favorite.objects.create(
            user=request.user,
            item_id=item_id,
        )
        favorite.save()
        return Response(status=status.HTTP_200_OK)
