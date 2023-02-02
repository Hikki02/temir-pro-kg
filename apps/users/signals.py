from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User
from temir import settings
from temir.conf.auth import AUTH_USER_MODEL


@receiver(post_save, sender=AUTH_USER_MODEL)
def post_save_user_qr_code_url(created, instance, **kwargs):
    if created:
        instance.qr_code_url = f"{settings.SITE_URL}?user={instance.id}"
    else:
        ...