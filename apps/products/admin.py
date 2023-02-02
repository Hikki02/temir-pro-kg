from django.contrib import admin
from .models import Product, Category, PreProduct
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Adding the product class to the admin site """

    list_display = (
        'name', "price", "quantity", "is_available", 'model'
    )


admin.site.register(Category)
admin.site.register(PreProduct)
