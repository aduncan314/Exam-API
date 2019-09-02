from rest_framework import serializers

from core.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ['password', 'is_superuser', 'user_permissions', 'date_joined', 'is_staff']
