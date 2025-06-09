from django.db import models
from django.conf import settings

from accounts.models.tweet import Tweet


class Retweet(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='retweets'
    )
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE,
                              related_name='retweets')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tweet')
