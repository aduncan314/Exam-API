from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import Organization, OrganizationType, CustomUser, UserType


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'last_name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Organization)
admin.site.register(OrganizationType)
admin.site.register(UserType)
