from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    firm = models.CharField(max_length=255, verbose_name='Фирма', db_index=True)
    name = models.CharField(max_length=255, verbose_name='Название модели', db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to="images/product/", blank=True)
    stock = models.PositiveIntegerField(verbose_name='Количество')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True, verbose_name='Наличие')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='product')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['firm', 'name']
        index_together = (('id', 'slug'),)

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

