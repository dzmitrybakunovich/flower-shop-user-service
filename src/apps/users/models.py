import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Store information about users."""
    uuid = models.UUIDField(
        'UUID',
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    photo = models.ImageField(_('Photo'), upload_to='media/users/photo')

    @property
    def full_name(self) -> str:
        return self.get_full_name()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
