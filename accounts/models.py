from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="accounts/", blank=True)

    followings = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False
    )

    def __str__(self):
        return str(self.username)
