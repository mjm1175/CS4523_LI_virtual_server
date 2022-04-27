# Generated by Django 4.0.4 on 2022-04-27 18:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_experience_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), default=list, size=None),
        ),
    ]
