import pytest
from django.urls import reverse
from rest_framework import status

from users.views import UserListView


class TestUserListView:
    URL = reverse('api_v1:users:users-list')

    @pytest.mark.django_db
    def test__get_users_list__success(self, drf_client):
        response = drf_client.get(self.URL)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    @pytest.mark.django_db
    def test__get_users_list__unauthorized(self, request_factory):
        request = request_factory.get(self.URL, )
        response = UserListView.as_view()(request)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
