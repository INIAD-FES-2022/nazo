# Generated by Django 4.1.2 on 2022-10-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inya', '0004_search_limit_alter_search_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='memo',
            field=models.CharField(max_length=30, verbose_name='メモ'),
        ),
    ]
