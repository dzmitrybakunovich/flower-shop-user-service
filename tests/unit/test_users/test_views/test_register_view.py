import pytest
from django.urls import reverse
from rest_framework import status

from users.views import RegisterView


class TestRegisterView:
    URL = reverse('api_v1:users:sign-up')

    @pytest.mark.django_db
    def test__create_user__success(self, request_factory):
        request = request_factory.post(
            self.URL,
            data={
                'username': 'test',
                'password': 'testPassword',
                'password2': 'testPassword',
                'email': 'email@example.com',
                'firstName': 'FirstName',
                'lastName': 'LastName',
            },
            content_type='application/json',
        )
        response = RegisterView.as_view()(request)

        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test__create_user__fail(self, request_factory):
        request = request_factory.post(
            self.URL,
            data={
                'password': 'testPassword',
                'password2': 'testPassword',
                'firstName': 'FirstName',
            },
            content_type='application/json',
        )
        response = RegisterView.as_view()(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
