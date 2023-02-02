# Generated by Django 4.1.4 on 2023-01-07 13:05

import apps.socials.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=225, null=True)),
                ('last_name', models.CharField(blank=True, max_length=225, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=apps.socials.utils.user_image_upload_path)),
                ('background', models.ImageField(blank=True, null=True, upload_to=apps.socials.utils.user_image_upload_path)),
                ('username', models.CharField(blank=True, max_length=225, null=True)),
                ('number_of_gold_user', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('welcome', models.CharField(blank=True, max_length=200, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('qr_code_url', models.URLField(blank=True, null=True)),
                ('work_phone', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('personal_phone', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('work_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='personal_email')),
                ('password', models.CharField(default='pbkdf2_sha256$390000$n43wXDZOARqtFGjdF7EFsF$GU6NhhLTCfl24jfrnIgrf8bFYs5XfX4v5B94n+VHQBA=', max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='SaveContactCount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='save_contact_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]