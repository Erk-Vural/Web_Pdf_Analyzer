# Generated by Django 3.2.9 on 2021-12-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20211203_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='Main/Static/Main/documents/'),
        ),
    ]