from typing import Optional

from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _


class ServiceException(Exception):
    default_detail = _('Service Exception')

    def __init__(self, message: Optional[str] = None) -> None:
        if message is None:
            self.message = self.default_detail

        self.message = force_str(message)

    def __str__(self) -> str:
        return self.message
