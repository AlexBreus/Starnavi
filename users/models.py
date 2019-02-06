from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import Group


class User(AbstractUser):
    """
    Класс нужен для того, чтобы переопределить и расширить стандартный функционал User-a в Django
    """

    class Meta:
        db_table = 'users'
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
