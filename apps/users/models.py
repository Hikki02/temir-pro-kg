from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

from django.core.mail import send_mail

FILTER_CHOICES = (
    ('day', 'day'),
    ('month', 'month'),
    ('year', 'year'),
)

import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.socials.utils import user_image_upload_path


class UserManager(BaseUserManager):

    @classmethod
    def _validate(cls, **kwargs) -> None:
        for k, v in kwargs.items():
            if not k:
                raise ValueError('You have not entered %s' % v)

    def _create(self, work_email: str, username: str, password: str, **extra) -> None:
        self._validate(work_email=work_email, username=username, password=password)
        user = self.model(work_email=self.normalize_email(work_email), username=username,
                          **extra)
        user.set_password(raw_password=password)
        user.save()

    def create_user(self,
                    work_email: str,
                    username: str,
                    password: str) -> None:
        self._create(work_email, username, password, )

    def create_superuser(self,
                         work_email: str,
                         username: str,
                         password: str) -> None:
        self._create(work_email, username, password, is_staff=True, is_superuser=True, is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=225, null=True, blank=True)
    last_name = models.CharField(max_length=225, null=True, blank=True)
    avatar = models.ImageField(upload_to=user_image_upload_path, null=True, blank=True)
    background = models.ImageField(upload_to=user_image_upload_path, null=True, blank=True)
    username = models.CharField(max_length=225, null=True, blank=True)
    number_of_gold_user = models.CharField(max_length=50, null=True, blank=True, unique=True)
    welcome = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    qr_code_url = models.URLField(null=True, blank=True)
    work_phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    personal_phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    website = models.URLField(null=True, blank=True)
    work_email = models.EmailField(unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='personal_email')

    password = models.CharField(max_length=128, default=make_password(settings.DEFAULT_PASSWORD))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    en_english = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'work_email'

    REQUIRED_FIELDS = ['username', ]

    class Meta:
        db_table = 'user'

    objects = UserManager()

    def __str__(self):
        return f'{self.id} -- {self.work_email}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4()
        super(User, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = f"follow the link to reset your password: " \
                              f"\n https://temir-businesscard.com/resetPassword/?token={reset_password_token.key}"
    send_mail(
        # title:
        f"Password Reset for {reset_password_token.user.first_name}",
        # message:
        email_plaintext_message,
        # from:
        "temircard@gmail.com",
        # to:
        [reset_password_token.user.email]

    )


class SaveContactCount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='save_contact_user')
    count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} {self.count}'
