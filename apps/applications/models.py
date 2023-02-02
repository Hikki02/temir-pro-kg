import uuid

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from apps.orders.models import OrderItem, Order
from apps.orders.choices import DELIVER_FORMAT, BY_CARD

# Create your models here.


class Checkout(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4)
    """
    Checkout model according design,
    Adding several fields for better managing:
    ("created_at, in_archive")
    """
    first_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name='Last Name'
    )
    company_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name='Company Name'
    )
    phone = models.CharField(
        null=False, blank=False, verbose_name='Phone number', max_length=200
    )
    email = models.EmailField(
        null=False, blank=False, verbose_name='Email'
    )
    country = models.CharField(
        null=False, blank=False, verbose_name='Country', max_length=255
    )
    emirate = models.CharField(
        null=False, blank=False, verbose_name='Эмираты', max_length=255
    )
    street_address = models.TextField(
        null=False, blank=False, verbose_name='Street address'
    )
    apartment_entrance = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Apartment_entrance'
    )
    house = models.CharField(
        null=False, blank=False, verbose_name='House/Apartment', max_length=255
    )
    order_notes = models.TextField(
        null=True, blank=True, verbose_name='Order Notes'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created at'
    )
    in_archive = models.BooleanField(
        default=False, verbose_name='In Archive'
    )
    order_id = models.OneToOneField(
        Order, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Basket'
    )
    choices = models.PositiveSmallIntegerField(
        choices=DELIVER_FORMAT, verbose_name='Формат выбора оплаты', default=BY_CARD
    )

    class Meta:
        verbose_name = "Checkout"
        verbose_name_plural = "Checkouts"

    def __str__(self):
        return f'{self.order_id}'


class ContactUs(models.Model):
    """
    Contact us model according Design
    Adding several field for better managing:
    ("created_at, in_archive")
    """
    first_name = models.CharField(
        max_length=255, null=True, blank=False, verbose_name="First_name"
    )
    last_name = models.CharField(
        null=True, blank=False, verbose_name='Last_name', max_length=255
    )
    full_name = models.CharField(max_length=225, null=True, blank=True, verbose_name="Full_name")
    email = models.EmailField(
        null=False, blank=False, verbose_name='Email'
    )
    phone_number = models.CharField(
        null=True, blank=True, verbose_name='Phone Number', max_length=255
    )
    message = models.TextField(
        null=False, blank=False, verbose_name='Message'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created at'
    )
    in_archive = models.BooleanField(
        default=False, verbose_name='In Archive'
    )

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'Responses'

    def __str__(self):
        return self.first_name


@receiver(post_delete, sender=Checkout)
def delete_payment(instance, sender, *args, **kwargs):
    from apps.orders.models import Order
    if instance.order_id:
        instance.order_id.delete(False)