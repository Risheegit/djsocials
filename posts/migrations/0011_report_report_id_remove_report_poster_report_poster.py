# Generated by Django 4.0.6 on 2022-07-13 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0010_remove_report_poster_report_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='report',
            name='poster',
        ),
        migrations.AddField(
            model_name='report',
            name='poster',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
