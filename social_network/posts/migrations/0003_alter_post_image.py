# Generated by Django 5.0.2 on 2024-12-15 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_like_like_like_posts_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
