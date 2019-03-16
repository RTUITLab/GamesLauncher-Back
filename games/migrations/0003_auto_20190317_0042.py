# Generated by Django 2.1.7 on 2019-03-16 21:42

import django.core.validators
from django.db import migrations, models

import games.storage


class Migration(migrations.Migration):
    dependencies = [
        ('games', '0002_auto_20190317_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='file',
            field=models.FileField(null=True, storage=games.storage.OverwriteStorage(),
                                   upload_to=games.storage.upload_file, validators=[
                    django.core.validators.FileExtensionValidator(allowed_extensions=['zip'])]),
        ),
        migrations.AlterField(
            model_name='game',
            name='logo',
            field=models.ImageField(null=True, upload_to=games.storage.upload_file),
        ),
    ]