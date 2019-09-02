from django.contrib.auth.models import AbstractUser
from django.db import models


class OrganizationType(models.Model):
    type_name = models.CharField(max_length=32)

    def __str__(self):
        return self.type_name


class Organization(models.Model):
    name = models.CharField(max_length=128)
    short_name = models.CharField(max_length=32, blank=True)
    org_type = models.ManyToManyField('core.OrganizationType')
    is_searchable = models.BooleanField()

    # TODO customize pronouns

    def __str__(self):
        return self.name if not self.short_name else self.short_name


class UserType(models.Model):
    user_type = models.CharField(max_length=16)
    sort_order = models.IntegerField()

    last_changed = models.DateTimeField()
    last_changed_by = models.ForeignKey('core.CustomUser', on_delete=models.PROTECT)

    def __str__(self):
        return self.user_type


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractbaseuser
class CustomUser(AbstractUser):
    username = models.CharField('Display Name', max_length=150)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'username']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class BaseUserModel(models.Model):
    organization = models.ForeignKey('core.Organization', on_delete=models.PROTECT, blank=True)
    user_type = models.ForeignKey('core.UserType', on_delete=models.PROTECT)

    # children = models.ManyToManyField('self', blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField()
    last_updated_by = models.ForeignKey('self', on_delete=models.PROTECT)

    class Meta:
        abstract = True
