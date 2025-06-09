from rest_framework import serializers
from accounts.models.tweet import Tweet
from accounts.models.user import User


class UserMinSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'avatar']

    def get_avatar(self, obj):
        if obj.avatar:
            return obj.avatar.url
        return None


class TweetSerializer(serializers.ModelSerializer):
    user = UserMinSerializer(read_only=True)
    image = serializers.SerializerMethodField()
    file = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'id', 'user', 'content', 'image', 'file',
            'created_at', 'reply_to'
        ]
        read_only_fields = ['id', 'user', 'created_at']

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    def get_file(self, obj):
        return obj.file.url if obj.file else None


class TweetCreateSerializer(serializers.ModelSerializer):
    user = UserMinSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = [
            'id', 'user', 'content', 'image', 'file',
            'created_at', 'reply_to'
        ]
        read_only_fields = ['id', 'user', 'created_at']

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    def get_file(self, obj):
        return obj.file.url if obj.file else None
