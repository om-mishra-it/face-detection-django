# Generated by Django 2.1.8 on 2021-09-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facedetection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='img',
            field=models.ImageField(upload_to='facedetection/dataset/'),
        ),
    ]