# Generated by Django 5.0 on 2024-01-06 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='additional_images',
            field=models.ManyToManyField(blank=True, related_name='additional_images', to='main.productimage'),
        ),
    ]
