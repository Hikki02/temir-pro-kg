import uuid

from django.db import models

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.


# class OrderItem(models.Model):
#     """
#     Cart model according Design
#     """
#     uuid = models.UUIDField(default=uuid.uuid4)
#     product = models.ManyToManyField(
#         'products.Product', verbose_name='Product',  through='products.PreProduct'
#     )
#
#     def __str__(self):
#         return f'{self.uuid}'


class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(
       'products.PreProduct', verbose_name='Product',  on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество'
    )

    @property
    def sum_price(self):
        return self.quantity * self.product.price

    @property
    def product_name(self):
        return self.product.uuid

    @property
    def product_price(self):
        return self.product.price

    def __str__(self):
        return f"#{self.quantity} of {self.product.uuid}"


@receiver(post_save, sender=Order)
def create_payment(instance, sender, created, *args, **kwargs):
    from apps.applications.models import Checkout
    order_items = instance.orderitem_set.all()
    Checkout.objects.create(order_id=instance)

