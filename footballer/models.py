from django.db import models
from django.urls import reverse


class Footballer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name='Страна')
    club = models.ForeignKey('Club', on_delete=models.PROTECT, verbose_name='Клуб')
    position = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Позиция')
    content = models.TextField(verbose_name='Контент')
    photo = models.ImageField(upload_to=f'photo/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_upload = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Футболист'
        verbose_name_plural = 'Футболисты'
        ordering = ['id']


class Position(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Позиция')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('position', kwargs={'position_slug': self.slug})

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'


class Club(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    foundation_year = models.PositiveSmallIntegerField(verbose_name='Год основания')
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name='Страна')
    league = models.CharField(max_length=255, verbose_name='Лига')
    content = models.TextField(verbose_name='Контент')
    logo = models.ImageField(upload_to=f'logo/%Y/%m/%d/', verbose_name='Логотип')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('club', kwargs={'club_slug': self.slug})

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'


class Country(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    flag = models.ImageField(upload_to=f'flag/%Y/%m/%d/', verbose_name='Флаг')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country', kwargs={'country_slug': self.slug})

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
