# Generated by Django 3.2.5 on 2021-09-11 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0056_auto_20210910_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxon',
            name='accepted_name_id',
            field=models.IntegerField(default=0, null=True, verbose_name='accepted_name_id'),
        ),
    ]
