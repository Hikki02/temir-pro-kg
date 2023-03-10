# Generated by Django 4.1.4 on 2023-01-07 13:06

import apps.socials.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MessangerCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=225)),
            ],
            options={
                'db_table': 'messanger_category',
            },
        ),
        migrations.CreateModel(
            name='SocialCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=225)),
            ],
            options={
                'db_table': 'social_category',
            },
        ),
        migrations.CreateModel(
            name='UserVideo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=225)),
                ('url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_video', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_video',
            },
        ),
        migrations.CreateModel(
            name='UserSocial',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=225)),
                ('url', models.URLField()),
                ('social', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='social', to='socials.socialcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_social', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_social',
            },
        ),
        migrations.CreateModel(
            name='UserProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('visit_website_url_name', models.CharField(max_length=225, null=True)),
                ('visit_website_url_url', models.URLField(null=True)),
                ('image', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_product', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_product',
            },
        ),
        migrations.CreateModel(
            name='UserPhone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=225)),
                ('phone_number', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_phone', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_phone',
            },
        ),
        migrations.CreateModel(
            name='UserMessanger',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=225)),
                ('url', models.URLField()),
                ('messanger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messanger', to='socials.messangercategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messanger', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_messanger',
            },
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('image', models.ImageField(upload_to=apps.socials.utils.user_image_upload_path)),
                ('is_avatar', models.BooleanField(default=False)),
                ('is_background', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_images', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_image',
            },
        ),
        migrations.CreateModel(
            name='UserEmail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_email', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_email',
            },
        ),
        migrations.CreateModel(
            name='UserBankCart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=225)),
                ('back_cart', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bank_cart', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_bank_cart',
            },
        ),
        migrations.CreateModel(
            name='UserBankAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=225)),
                ('back_account', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bank_account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_bank_account',
            },
        ),
    ]
