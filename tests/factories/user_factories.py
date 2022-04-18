import uuid

import factory.fuzzy

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    uuid = uuid.uuid4()
    username = 'username'
    email = 'username@example.com'
    password = factory.PostGenerationMethodCall(
        'set_password',
        'testPassword',
    )
    is_staff = False
    is_superuser = False

    class Meta:
        model = User
        django_get_or_create = ("uuid",)
