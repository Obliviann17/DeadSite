# Generated by Django 5.0 on 2024-01-09 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_productimage_options_productimage_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={},
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='date',
        ),
    ]
