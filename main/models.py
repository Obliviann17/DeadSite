from django.db import models
from autoslug import AutoSlugField
from PIL import Image

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    price = models.CharField(max_length=15)
    composition = models.TextField(max_length=100)
    description = models.TextField(max_length=250)
    main_image = models.ForeignKey('ProductImage', related_name='main_image', on_delete=models.SET_NULL, blank=True, null=True)
    available = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товари"
        verbose_name_plural = "Товари"
        ordering = ['name',]


class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='additional_images', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='product_images/')
    # date = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     ordering = ['-date',]
    #
    # def __str__(self):
    #     return str(self.date)



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(upload_to='category_images/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категоії"
        verbose_name_plural = "Категорії"




