# Generated by Django 4.0.4 on 2022-05-07 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_resume_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
