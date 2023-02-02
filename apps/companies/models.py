import uuid

from django.db import models

from apps.users.models import User
from apps.users.utils import user_company_image_upload_path


class UserCompany(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_company')
    name = models.CharField(max_length=225, blank=True, null=True)
    activity = models.CharField(max_length=225, blank=True, null=True)
    image = models.ImageField(upload_to=user_company_image_upload_path, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    visit_website_url_name = models.CharField(max_length=225, blank=True, null=True)
    visit_website_url = models.URLField(blank=True, null=True)
    address_url = models.URLField(blank=True, null=True)
    is_main = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_company'

    def __str__(self):
        return f'{self.user} -- {self.name}'
