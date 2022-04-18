import pytest
from django.urls import reverse
from rest_framework import status


class TestUserListView:
    URL = 'api_v1:users:user-detail'

    @pytest.mark.django_db
    def test__get_user__success(self, drf_client, user):
        response = drf_client.get(
            reverse(
                self.URL,
                args=[user.uuid]
            ),
        )

        assert response.status_code == status.HTTP_200_OK
