from django.db import models
from django.conf import settings

from accounts.models.tweet import Tweet


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='comments')
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE,
                              related_name='comments')
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
