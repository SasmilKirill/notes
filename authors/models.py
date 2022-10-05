from django.db import models
from django.contrib.auth.models import AbstractUser




class Author(models.Model):
    first_name = models.CharField(max_lenght=64)
    last_name = models.CharField(max_lenght=64)
    birthday_name = models.PositiveIntegerField()


Class User(AbstractUser):
     image = models.ImageField(upload_to='users_image',blank=True)


def __str__(self):
    return f'{ -last_name} { .first_name} { .birthday_year}'

class Biographies(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author,on_delete=models.CASCADE)

class Book (models.Model):
name = models.CharFieldt(max_lrnght=64)
author = models.ManyToManyField(Author)

