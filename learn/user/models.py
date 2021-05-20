from django.db import models
from django.contrib.auth.models import User#weimported user because we want a one to one relation between profile image and user


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'