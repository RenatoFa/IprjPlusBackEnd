from django.db import models
from django.utils import timezone

from .user import User


class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return (timezone.now() -
                self.created_at < timezone.timedelta(minutes=10))
