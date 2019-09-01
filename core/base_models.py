from django.db import models
from core.models import Organization, UserType


# ****************************** Abstract Models ******************************

class BaseUser(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    organization = models.ForeignKey('core.Organization', on_delete=models.PROTECT)
    user_type = models.ForeignKey('core.UserType', on_delete=models.PROTECT)
    children = models.ManyToManyField('self', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplementedError
