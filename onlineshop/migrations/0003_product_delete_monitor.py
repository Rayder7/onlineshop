# Generated by Django 4.0.3 on 2022-05-18 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm', models.CharField(db_index=True, max_length=255, verbose_name='Фирма')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название модели')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='images/product/')),
                ('stock', models.PositiveIntegerField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='onlineshop.category')),
            ],
            options={
                'verbose_name': 'Мониторы',
                'verbose_name_plural': 'Мониторы',
                'ordering': ['firm', 'name'],
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.DeleteModel(
            name='Monitor',
        ),
    ]
