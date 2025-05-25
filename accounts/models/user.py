from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from cloudinary.models import CloudinaryField


class UserManager(BaseUserManager):
    def create_user(self, email, name, date_of_birth, password=None):
        if not email:
            raise ValueError('O email é obrigatório.')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            date_of_birth=date_of_birth,
        )
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, date_of_birth, password):
        user = self.create_user(email, name, date_of_birth)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    avatar = CloudinaryField('image', default='media/avatars/default.png',
                             folder='media/avatars',
                             public_id=lambda instance: f'user_{instance.id}',
                             overwrite=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth']

    objects = UserManager()

    def __str__(self):
        return self.email
