from django.contrib import admin


from .models import User


# - - - - - - - - - - - - - - - - - - - USER - - - - - - - - - - - -
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...
