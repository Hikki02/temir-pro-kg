from django.db import models

from apps.users.models import User
from ..base import BaseUserSocialModel


# - - - - - - - - - - - - - - - - -  USER BANK ACCOUNT - - - - - - - - - - - - - - - - -
class UserBankAccount(BaseUserSocialModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bank_account')
    back_account = models.CharField(max_length=225, null=True, blank=True)

    class Meta:
        db_table = 'user_bank_account'


# - - - - - - - - - - - - - - - - -  USER BANK CART - - - - - - - - - - - - - - - - -
class UserBankCart(BaseUserSocialModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bank_cart')
    back_cart = models.CharField(max_length=225, null=True, blank=True)

    class Meta:
        db_table = 'user_bank_cart'
