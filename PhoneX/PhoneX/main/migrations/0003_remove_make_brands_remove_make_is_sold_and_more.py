# Generated by Django 5.0.2 on 2024-04-21 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_make_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='make',
            name='brands',
        ),
        migrations.RemoveField(
            model_name='make',
            name='is_sold',
        ),
        migrations.AlterField(
            model_name='make',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='phones/images'),
        ),
    ]
