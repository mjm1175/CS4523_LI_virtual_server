# Generated by Django 4.0.4 on 2022-05-09 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_category_job_city_job_skills_job_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
    ]
