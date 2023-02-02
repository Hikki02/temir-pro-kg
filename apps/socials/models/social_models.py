from django.db import models

from apps.users.models import User
from apps.socials.base import BaseModel, BaseUserSocialModel
from apps.socials.utils import user_image_upload_path


# - - - - - - - - - - - - - - - - -  SOCIAL CATEGORY - - - - - - - - - - - - - - - - -
class SocialCategory(BaseModel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'social_category'


class MessangerCategory(BaseModel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'messanger_category'


# - - - - - - - - - - - - - - - - -  USER SOCIAL - - - - - - - - - - - - - - - - -
class UserSocial(BaseUserSocialModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_social')
    social = models.ForeignKey(SocialCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='social')
    url = models.URLField()

    class Meta:
        db_table = 'user_social'

    def __str__(self):
        return f'{self.social}'


class UserMessanger(BaseUserSocialModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_messanger')
    messanger = models.ForeignKey(MessangerCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='messanger')
    url = models.URLField()

    class Meta:
        db_table = 'user_messanger'

    def __str__(self):
        return f'{self.messanger}'


# - - - - - - - - - - - - - - - - -  USER PHONE - - - - - - - - - - - - - - - - -
class UserPhone(BaseUserSocialModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_phone')
    phone_number = models.CharField(max_length=225)

    class Meta:
        db_table = 'user_phone'

    def __str__(self):
        return f'{self.phone_number}'


# - - - - - - - - - - - - - - - - -  USER EMAIL - - - - - - - - - - - - - - - - -
class UserEmail(BaseUserSocialModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_email', null=True)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'user_email'

    def __str__(self):
        return f'{self.email}'


# - - - - - - - - - - - - - - - - -  USER IMAGE - - - - - - - - - - - - - - - - -
class UserImage(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_images')  # need change to user_image
    image = models.ImageField(upload_to=user_image_upload_path)  # coment

    class Meta:
        db_table = 'user_image'

    def __str__(self):
        return str(self.user.id)


# - - - - - - - - - - - - - - - - -  USER VIDEO - - - - - - - - - - - - - - - - -
class UserVideo(BaseUserSocialModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_video')
    url = models.URLField()

    class Meta:
        db_table = 'user_video'

    def __str__(self):
        return str(self.user.id)


# - - - - - - - - - - - - - - - - -  USER PRODUCT - - - - - - - - - - - - - - - - -
class UserProduct(BaseUserSocialModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product')
    description = models.TextField()
    visit_website_url_name = models.CharField(max_length=225, null=True)
    visit_website_url_url = models.URLField(null=True)
    image = models.ImageField()

    class Meta:
        db_table = 'user_product'
