from collections import namedtuple
from django.db import models
from datetime import date


# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=10, default='Coding')
    photo_main = models.ImageField(
        null=True, blank=True, upload_to='images/profile/')
    # photo_main
    description = models.TextField()
    book_date = models.DateField(blank=True, default=date.today)
    download_book = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
