from django.contrib import admin


# - - - - - - - - - - - - - - - - - - - USER SOCIALS - - - - - - - - - - - -
from apps.socials.models import UserEmail, UserImage, UserPhone, UserSocial, UserVideo, SocialCategory, \
    MessangerCategory, UserMessanger, UserProduct


@admin.register(UserEmail)
class UserEmailAdmin(admin.ModelAdmin):
    ...


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    ...


@admin.register(UserPhone)
class UserPhoneAdmin(admin.ModelAdmin):
    ...


@admin.register(UserSocial)
class UserSocialAdmin(admin.ModelAdmin):
    ...


@admin.register(UserMessanger)
class UserMessangerAdmin(admin.ModelAdmin):
    ...


@admin.register(UserVideo)
class UserVideoAdmin(admin.ModelAdmin):
    ...


@admin.register(SocialCategory)
class SocialCategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(MessangerCategory)
class MessangerCategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(UserProduct)
class UserProductAdmin(admin.ModelAdmin):
    ...
1

# @admin.register(UserSocial)
# class UserSocialAdmin(admin.ModelAdmin):
#     ...
