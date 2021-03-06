# Generated by Django 3.2.5 on 2021-07-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=30)),
                ('category', models.CharField(default='Coding', max_length=10)),
                ('book_image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('description', models.TextField()),
                ('download_book', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]
