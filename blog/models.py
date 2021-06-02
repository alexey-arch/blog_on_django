from django.db import models
from django.urls import reverse

class Post(models.Model):
    """
    Модель постов
    """
    title = models.CharField(max_length=200)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class User(models.Model):
    """
    модель пользователя 
    """
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=60)
    
    def __str__(self):
        return self.username