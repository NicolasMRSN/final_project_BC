# Generated by Django 2.2.5 on 2019-12-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FilePathField(path='/authentication/img/'),
        ),
    ]