# Generated by Django 2.1.2 on 2018-12-01 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnistwebsite', '0003_auto_20181201_1216'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='inputImage',
            new_name='positionLevel',
        ),
        migrations.RenameField(
            model_name='positionlevel',
            old_name='image',
            new_name='position',
        ),
    ]
