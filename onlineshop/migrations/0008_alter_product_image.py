# Generated by Django 4.0.3 on 2022-07-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0007_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/product/'),
        ),
    ]
