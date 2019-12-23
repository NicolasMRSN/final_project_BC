# Generated by Django 2.2.5 on 2019-12-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaceAuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.BinaryField()),
                ('wallet_id', models.CharField(max_length=42)),
                ('encrypted_img_str', models.TextField(max_length=3000)),
                ('private_key', models.TextField(max_length=256)),
            ],
        ),
    ]
