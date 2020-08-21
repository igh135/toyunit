from django.contrib import admin

# Register your models here.

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'UserID')


admin.site.register(User, UserAdmin)
