from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import check_password

from .user import User


class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return (timezone.now() -
                self.created_at < timezone.timedelta(minutes=10))

    def check_code(self, raw_code):
        return check_password(raw_code, self.code)
