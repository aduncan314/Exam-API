from django.db import models


class OrganizationType(models.Model):
    type_name = models.CharField(max_length=32)

    def __str__(self):
        return self.type_name


class Organization(models.Model):
    name = models.CharField(max_length=128)
    org_type = models.ForeignKey('core.OrganizationType', on_delete=models.PROTECT)
    is_searchable = models.BooleanField()

    def __str__(self):
        return f'{self.org_type} - {self.name}'


class UserType(models.Model):
    user_type = models.CharField(max_length=16)

    def __str__(self):
        return self.user_type
