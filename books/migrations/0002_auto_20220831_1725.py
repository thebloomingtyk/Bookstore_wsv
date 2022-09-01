# Generated by Django 2.2.7 on 2022-08-31 17:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AddField(
            model_name='book',
            name='uid',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=89, primary_key=True, serialize=False, unique=True),
        ),
    ]