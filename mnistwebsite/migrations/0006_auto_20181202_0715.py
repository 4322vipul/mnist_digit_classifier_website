# Generated by Django 2.1.2 on 2018-12-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnistwebsite', '0005_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='given_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_given', models.ImageField(max_length=64, upload_to='')),
            ],
        ),
        migrations.RenameModel(
            old_name='salary',
            new_name='predicted_label',
        ),
        migrations.DeleteModel(
            name='positionLevel',
        ),
        migrations.RenameField(
            model_name='predicted_label',
            old_name='predictedSalary',
            new_name='label',
        ),
    ]
