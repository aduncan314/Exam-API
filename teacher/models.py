from django.db import models

from core.models import Organization, CustomUser


class TeacherTitle(models.Model):
    title = models.CharField(max_length=16)
    # TODO: set default all?
    # visible_to = models.ManyToManyField('core.Organization', blank=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    user = models.ForeignKey('core.CustomUser', on_delete=models.PROTECT)
    title = models.ForeignKey('teacher.TeacherTitle', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.user.last_name}"


class StudentGroup(models.Model):
    group_name = models.CharField(max_length=128)
    year_title = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()

    last_updated = models.DateTimeField()
    last_updated_by = models.ForeignKey('self', on_delete=models.PROTECT)
