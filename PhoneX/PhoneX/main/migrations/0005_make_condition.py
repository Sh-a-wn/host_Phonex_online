# Generated by Django 5.0.2 on 2024-04-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_make_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='make',
            name='condition',
            field=models.BooleanField(default=True),
        ),
    ]
