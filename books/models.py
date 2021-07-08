from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=10, default='Coding')
    photo_main = models.ImageField(
        null=True, blank=True, upload_to='images/profile/')
    description = models.TextField()
    download_book = models.FileField(upload_to='documents/%Y/%m/%d')
