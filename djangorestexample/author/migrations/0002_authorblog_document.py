# Generated by Django 3.1.7 on 2021-03-19 19:40

import author.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorblog',
            name='document',
            field=models.FileField(null=True, upload_to=author.models.directoy_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
