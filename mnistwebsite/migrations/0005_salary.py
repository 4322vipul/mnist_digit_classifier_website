# Generated by Django 2.1.2 on 2018-12-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnistwebsite', '0004_auto_20181201_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predictedSalary', models.CharField(max_length=64)),
            ],
        ),
    ]