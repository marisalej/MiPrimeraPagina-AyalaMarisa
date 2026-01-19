from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="avatars/",
        default="default/default.png",
        blank=True,
        null=True
    )

    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="Biografía"
    )

    def __str__(self):
        return self.username
