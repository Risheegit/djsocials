# Generated by Django 4.0.6 on 2022-07-10 17:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='India', max_length=100),
            preserve_default=False,
        ),
    ]
