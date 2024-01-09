from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo')
    list_display_links = ('name',)
    search_fields = ('name',)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'available', 'slug', 'cat')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price', 'cat', 'slug')

    inlines = [ProductImageAdmin]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)