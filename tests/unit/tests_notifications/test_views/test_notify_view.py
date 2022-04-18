import json

import pytest
from django.urls import reverse
from rest_framework import status


class TestNotifyView:
    URL = reverse('api_v1:notifications:send-notification')

    @pytest.mark.django_db
    def test__send_notification_without_cc__success(self, drf_client, user, admin):
        response = drf_client.post(
            self.URL,
            data=json.dumps(
                {
                    'subject': 'Test',
                    'message': 'Test',
                    'recipientsList': [str(user.uuid), str(admin.uuid)],
                    'carbonCopyList': []
                }
            ),
            content_type='application/json',
        )

        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test__send_notification_with_cc__success(self, drf_client, user, admin):
        response = drf_client.post(
            self.URL,
            data=json.dumps(
                {
                    'subject': 'Test',
                    'message': 'Test',
                    'recipientsList': [str(user.uuid)],
                    'carbonCopyList': [str(admin.uuid)]
                }
            ),
            content_type='application/json',
        )

        assert response.status_code == status.HTTP_201_CREATED
