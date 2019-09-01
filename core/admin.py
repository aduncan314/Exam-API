from django.contrib import admin
from core.models import Organization, OrganizationType, UserType

admin.site.register(Organization)
admin.site.register(OrganizationType)
admin.site.register(UserType)