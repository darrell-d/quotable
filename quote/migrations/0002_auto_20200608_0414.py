# Generated by Django 3.0.7 on 2020-06-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_source',
            field=models.TextField(default='unknown', max_length=128),
        ),
    ]