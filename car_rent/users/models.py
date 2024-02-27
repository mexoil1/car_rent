from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''Model of user'''
    first_name = models.CharField(
        max_length=200,
        verbose_name='Имя')
    last_name = models.CharField(
        max_length=200,
        verbose_name='Фамилия')
    email = models.EmailField(
        unique=True,
        max_length=200,
        verbose_name='Email')
    score = models.FloatField(default=5.0, verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.email} {self.first_name} {self.last_name}'
