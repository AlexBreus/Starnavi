from django.db import models
from users.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        db_table = 'posts'
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
