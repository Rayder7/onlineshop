# Generated by Django 4.0.3 on 2022-04-12 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm', models.CharField(max_length=255, verbose_name='Фирма')),
                ('title', models.CharField(max_length=255, verbose_name='Название модели')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('Screen_size', models.FloatField(max_length=4, verbose_name='Размер экрана')),
                ('Screen_resolution', models.CharField(max_length=9, verbose_name='Разрешение экрана')),
                ('price', models.IntegerField(blank=True, default=0)),
                ('photo', models.ImageField(upload_to='photos/monitors/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='onlineshop.category')),
            ],
            options={
                'verbose_name': 'Мониторы',
                'verbose_name_plural': 'Мониторы',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
