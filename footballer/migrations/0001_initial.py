# Generated by Django 3.2.9 on 2021-12-04 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('foundation_year', models.PositiveSmallIntegerField(verbose_name='Год основания')),
                ('league', models.CharField(max_length=255, verbose_name='Лига')),
                ('content', models.TextField(verbose_name='Контент')),
                ('logo', models.ImageField(upload_to='logo/%Y/%m/%d/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Клуб',
                'verbose_name_plural': 'Клубы',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('flag', models.ImageField(upload_to='flag/%Y/%m/%d/', verbose_name='Флаг')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Позиция')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
            },
        ),
        migrations.CreateModel(
            name='Footballer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
                ('content', models.TextField(verbose_name='Контент')),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_upload', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='footballer.club', verbose_name='Клуб')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='footballer.country', verbose_name='Страна')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='footballer.position', verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Футболист',
                'verbose_name_plural': 'Футболисты',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='club',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='footballer.country', verbose_name='Страна'),
        ),
    ]