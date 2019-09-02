from rest_framework import serializers

from core.serializers import CustomUserSerializer
from teacher.models import Teacher, TeacherTitle


class TeacherTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherTitle
        exclude = []


# class StudentGroupSerializer(serializers.ModelSerializer):

class TeacherSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    title = TeacherTitleSerializer(read_only=True)

    class Meta:
        model = Teacher
        exclude = []
