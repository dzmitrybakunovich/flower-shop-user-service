from typing import Optional

from core.services import BaseService
from notifications.tasks import send_mail
from users.models import User


class NotifyService(BaseService):
    def __init__(
            self,
            subject: str,
            message: str,
            recipients_list: list,
            carbon_copy_list: list = None,
            headers: Optional[str] = None,
    ) -> None:
        self.recipients_list = recipients_list
        self.carbon_copy_list = carbon_copy_list
        self.subject = subject
        self.message = message
        self.headers = headers

    def perform(self, **kwargs) -> None:
        recipients = self._get_recipients()
        carbon_copy = self._get_carbon_copy() if self.carbon_copy_list else None

        send_mail.s(
            subject=self.subject,
            message=self.message,
            to_email=recipients,
            cc_list=carbon_copy,
            headers=self.headers
        ).apply_async()

    def _get_recipients(self):
        return list(
            User.objects.filter(
                uuid__in=self.recipients_list,
            ).values_list('email', flat=True)
        )

    def _get_carbon_copy(self):
        return list(
            User.objects.filter(
                uuid__in=self.carbon_copy_list,
            ).values_list('email', flat=True)
        )
