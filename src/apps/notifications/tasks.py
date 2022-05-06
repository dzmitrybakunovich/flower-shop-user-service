from typing import Optional, Union

from celery import shared_task
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task
def send_mail(
        subject: str,
        message: str,
        to_email: Union[list, tuple],
        cc_list: Optional[list] = None,
        headers: Optional[dict] = None,
):
    print(subject, message, to_email, cc_list, headers)

    mail = EmailMultiAlternatives(
        subject,
        message,
        'test@gg.com',
        to_email,
        cc=cc_list,
        headers=headers,
    )
    mail.send()
