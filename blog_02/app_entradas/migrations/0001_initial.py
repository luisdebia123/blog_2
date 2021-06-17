# Generated by Django 3.2.4 on 2021-06-09 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('contenido', models.TextField(default='DEFAULT VALUE')),
                ('img_destacada', models.ImageField(null=True, upload_to='fotos')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'entradas',
            },
        ),
    ]
