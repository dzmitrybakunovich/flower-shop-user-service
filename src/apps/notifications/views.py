from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.exceptions import ServiceException
from .serializers import NotifySerializer
from .services.notify_service import NotifyService


class NotifyView(CreateModelMixin, GenericAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = NotifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            message = f'Validation error on a new notification. Reason: {serializer.errors}'
            return Response(status=status.HTTP_400_BAD_REQUEST, data=message)

        data = serializer.validated_data
        service = NotifyService(**data)
        #
        # try:
        #     service.perform()
        # except ServiceException as e:
        #     message = f'Cannot save question. Reason: {e}'
        #     return Response(status=status.HTTP_400_BAD_REQUEST, data=message)

        # serializer = self.get_serializer(service.instance)
        # headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED)
