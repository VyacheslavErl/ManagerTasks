from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    image = models.ImageField('Фотография', upload_to='users_image', blank=True, default='no_image.png')
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
