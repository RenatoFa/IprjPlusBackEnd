from django.contrib.auth.hashers import make_password

from accounts.models.user import User

from rest_framework import serializers
from django.utils.crypto import get_random_string


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'date_of_birth']

    def create(self, validated_data):
        validated_data['password'] = make_password(
            get_random_string(length=12))
        return super().create(validated_data)
