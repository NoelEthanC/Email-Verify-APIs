from django.contrib import admin
from . import models
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = models.User
    list_display = ['username', 'email', 'phone_number', 'is_verified' ]  

admin.site.register(models.User, UserAdmin)