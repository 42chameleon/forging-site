
from django.db import models


class Forging(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    content = models.TextField('Описание')
    photo = models.ImageField('Фото', upload_to='media/')


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    telephone = models.CharField('Телефон сварщика', max_lengt=20)
