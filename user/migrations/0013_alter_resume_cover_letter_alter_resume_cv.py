# Generated by Django 4.0.4 on 2022-05-09 10:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_remove_resume_project_implicit_projectimplicit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='cover_letter',
            field=models.FileField(blank=True, null=True, upload_to='resumes', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='resume',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='resumes', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
