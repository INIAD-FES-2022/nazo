# Generated by Django 4.1.2 on 2022-10-27 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inya', '0002_alter_search_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='memo',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]