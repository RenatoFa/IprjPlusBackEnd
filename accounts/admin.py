from django.contrib import admin

from .models.otp import Otp
from .models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'is_active']


admin.site.register(Otp)
