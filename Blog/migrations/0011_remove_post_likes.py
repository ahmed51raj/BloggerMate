# Generated by Django 2.1.2 on 2019-03-01 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
