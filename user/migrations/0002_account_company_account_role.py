# Generated by Django 4.0.4 on 2022-05-04 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.company'),
        ),
        migrations.AddField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('Employer', 'Employer'), ('Applicant', 'Applicant')], default='Applicant', max_length=10),
        ),
    ]
