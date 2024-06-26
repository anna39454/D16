from django.urls import reverse_lazy
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    code = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)# Автор
    title = models.CharField(max_length=255)# Заголовок объявления
    text = models.TextField()# Текст объявления
    created = models.DateTimeField(auto_now_add=True)# Дата создания
    category = models.ForeignKey('Category', on_delete=models.CASCADE)# Категория
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, default=None, null=True, verbose_name='upload')# Вложения

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post_detail', kwargs={'pk':self.pk})



class Category(models.Model):
    name = models.CharField(max_length=64)
    subscribers = models.ManyToManyField(User, through='Subscriber')

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse_lazy('comment_detail', kwargs={'pk': self.pk})







