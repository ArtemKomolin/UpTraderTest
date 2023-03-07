from django.db import models
from django.urls import reverse


class Songs(models.Model):
    song = models.CharField(max_length=255, verbose_name='Трек')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения записи')
    is_published = models.BooleanField(default=True, verbose_name='Запись опубликована')
    cat = models.ForeignKey('Albums', on_delete=models.PROTECT, null=True, verbose_name='Трек из альбома:')

    def __str__(self):
        return self.song


    class Meta:
        verbose_name = 'Песни'
        verbose_name_plural = 'Песни'
        ordering = ['cat', 'time_create']


class Albums(models.Model):
    album = models.CharField(max_length=255, db_index=True, verbose_name='Альбом')
    year = models.CharField(max_length=255, db_index=True, verbose_name='Год релиза альбома')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Обложка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения записи')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.album


    class Meta:
        verbose_name = 'Альбомы'
        verbose_name_plural = 'Альбомы'
        ordering = ['year']
