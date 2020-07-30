from django.db import models


class Forging(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    content = models.TextField('Описание')
    published_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    is_published = models.BooleanField('Опубликовать', default=False, blank=True)
    photo = models.ImageField('Фото', upload_to='media/')
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ковку'
        verbose_name_plural = 'Кованные изделия'


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    telephone = models.CharField('Телефон сварщика', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'