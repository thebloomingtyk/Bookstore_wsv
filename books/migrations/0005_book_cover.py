# Generated by Django 2.2.7 on 2022-09-01 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
