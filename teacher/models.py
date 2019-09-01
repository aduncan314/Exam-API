from django.db import models
from core.models import Organization
from core.base_models import BaseUser


class TeacherTitle(models.Model):
    title = models.CharField(max_length=16)
    # TODO: set default all?
    visible_to = models.ManyToManyField('core.Organization')

    def __str__(self):
        return self.title


class Teacher(BaseUser):
    title = models.ForeignKey('teacher.TeacherTitle', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {str.capitalize(self.last_name)}'
