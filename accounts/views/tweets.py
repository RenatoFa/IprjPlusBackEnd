from rest_framework import viewsets, permissions
from accounts.models.tweet import Tweet
from accounts.serializers.tweets import TweetSerializer, TweetCreateSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().select_related('user', 'reply_to')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return TweetCreateSerializer
        return TweetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
