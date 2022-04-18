import uuid

import pytest
from pytest_django.lazy_django import skip_if_no_django
from rest_framework_simplejwt.tokens import RefreshToken

from .factories.user_factories import UserFactory


@pytest.fixture()
def request_factory():
    """Request factory instance."""
    from django.test.client import RequestFactory
    skip_if_no_django()

    return RequestFactory()


@pytest.fixture
def user():
    """User instance."""
    user = UserFactory()

    return user


@pytest.fixture
def admin():
    """Administrator instance."""
    admin = UserFactory(
        uuid=uuid.uuid4(),
        username='admin',
        email='admin@example.com',
        is_staff=True,
        is_superuser=True,
    )
    return admin


@pytest.fixture()
def drf_client(user):
    """A Django Rest Framework authenticate client instance."""
    from rest_framework.test import APIClient
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(
        HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
    )

    return client
