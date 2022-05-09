# Generated by Django 4.0.4 on 2022-05-09 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_remove_zoommeeting_interviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoommeeting',
            name='interviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
