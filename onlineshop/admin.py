from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'firm', 'name', 'time_create', 'get_html_image', 'available', 'stock', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('firm', 'name', 'description')
    list_editable = ('available',)
    list_filter = ('firm', 'time_create')
    prepopulated_fields = {"slug": ("firm", "name")}
    fields = ('firm', 'slug', 'name', 'cat', 'description', 'image', 'price','stock', 'get_html_image', 'available', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_image')

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
    get_html_image.short_description = "Миниатюра"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}




admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админка'
admin.site.site_header = 'Админ панель сайта'