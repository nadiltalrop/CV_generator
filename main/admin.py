from django.contrib import admin

from.models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'skills')

admin.site.register(Profile, ProfileAdmin)
