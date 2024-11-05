from django.db import models

class Post(models.Model):
    """данные о посте"""
    title = models.CharField('название проекта', max_length=100)
    version = models.CharField("версия", max_length=15)
    date = models.DateField("Дата публикации")
    link_in_git = models.CharField("Ссылка на гит", max_length=150)
    img = models.ImageField('изображение', upload_to='image/%Y/')

    def __str__(self):
        return f'{self.title}, {self.date}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    