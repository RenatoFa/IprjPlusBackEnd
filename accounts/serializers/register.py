from accounts.models.user import User

from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'date_of_birth']
