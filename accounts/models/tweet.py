from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='tweets'
                             )
    content = models.TextField(max_length=280, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', blank=True, null=True,
                            folder='media/tweets/images',
                            overwrite=True)
    file = CloudinaryField('file', blank=True, null=True, resource_type='raw',
                           folder='media/tweets/files',
                           overwrite=True)
    reply_to = models.ForeignKey('self', null=True, blank=True,
                                 on_delete=models.CASCADE,
                                 related_name='replies')

    class Meta:
        ordering = ['-created_at']
