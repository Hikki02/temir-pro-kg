import uuid

from django.db import models
# Create your models here.


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super(AvailableManager, self).get_queryset().filter(is_available=True, quantity__gte=1)


class Category(models.Model):

    """The model for product, like category"""

    uuid = models.UUIDField(default=uuid.uuid4, max_length='32')
    title = models.CharField(
        max_length=255, unique=True, null=False, blank=False, verbose_name='Model Name'
    )

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    def __str__(self):
        return self.title


class Product(models.Model):

    """ Model of Product """

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, max_length='32')
    name = models.CharField(
        max_length=255, unique=True, null=False, blank=False, verbose_name='Наименование продукта'
    )
    model = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, verbose_name='The name of product model'
    )
    image = models.ImageField(
        null=False, blank=False, verbose_name='Image'
    )
    price = models.PositiveIntegerField(
        null=False, blank=False, verbose_name='Price'
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Quantity'
    )
    objects = models.Manager()
    available = AvailableManager()
    is_available = models.BooleanField(
        verbose_name='Is available'
    )
    description = models.TextField(
        verbose_name='Description'
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class PreProduct(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, max_length='32', unique=True)
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, verbose_name='Продукт'
    )
    name_company = models.CharField(
        max_length=255, verbose_name='Наименование компании', null=True, blank=True
    )
    logo = models.ImageField(
        null=True, blank=True, verbose_name='Логотип Компании'
    )

    class Meta:
        verbose_name = "Pre_Product"
        verbose_name_plural = "Pre_Products"

    def __str__(self):
        return f'{self.uuid}'
