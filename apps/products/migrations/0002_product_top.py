# Generated by Django 5.0.4 on 2024-05-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='top',
            field=models.BooleanField(default=False),
        ),
    ]