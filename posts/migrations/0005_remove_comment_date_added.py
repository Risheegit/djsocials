# Generated by Django 4.0.6 on 2022-07-13 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date_added',
        ),
    ]
