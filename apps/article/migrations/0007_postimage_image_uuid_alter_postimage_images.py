# Generated by Django 4.0 on 2022-02-15 08:03

import apps.article.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_postimage_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='image_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.ImageField(blank=True, upload_to=apps.article.models.images_path),
        ),
    ]
