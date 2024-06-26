# Generated by Django 5.0.2 on 2024-04-16 18:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('condition', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('image', models.ImageField(default='', upload_to='phones/images')),
                ('description', models.TextField(default='')),
                ('price', models.IntegerField(default=0)),
                ('is_sold', models.BooleanField(default=False)),
                ('brands', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.brands')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('BUYER', 'buyer'), ('SELLER', 'seller')], default='BUYER', max_length=50)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
