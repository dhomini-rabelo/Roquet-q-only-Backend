# Generated by Django 3.2.7 on 2021-10-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asks', '0004_auto_20211018_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]