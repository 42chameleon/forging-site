
from django.db import models


class Forging(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    content = models.TextField('Описание')
    is_published = models.BooleanField('Опубликовать', default=False, blank=True)
    photo = models.ImageField('Фото', upload_to='media/')


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    telephone = models.CharField('Телефон сварщика', max_length=20)
