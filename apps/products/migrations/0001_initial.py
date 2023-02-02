# Generated by Django 4.1.4 on 2023-01-07 13:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Model Name')),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование продукта')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('is_available', models.BooleanField(verbose_name='Is available')),
                ('description', models.TextField(verbose_name='Description')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='The name of product model')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='PreProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name_company', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование компании')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Логотип Компании')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Pre_Product',
                'verbose_name_plural': 'Pre_Products',
            },
        ),
    ]