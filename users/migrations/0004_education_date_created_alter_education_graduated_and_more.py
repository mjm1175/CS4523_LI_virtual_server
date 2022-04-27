# Generated by Django 4.0.4 on 2022-04-27 00:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_resume_date_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='education',
            name='graduated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='level',
            field=models.CharField(choices=[('Some High School Education', 'Some High School Education'), ('High School Certificate (G.E.D.)', 'High School Certificate (G.E.D.)'), ('High School Diploma', 'High School Diploma'), ('Some College Education', 'Some College Education'), ("Associate's Degree (AS/AA)", "Associate's Degree (AS/AA)"), ("Bachelor's Degree (BS/BA)", "Bachelor's Degree (BS/BA)"), ('Some Postgraduate School', 'Some Postgraduate School'), ('Professional School Graduate', 'Professional School Graduate'), ("Master's Degree (MS/MA)", "Master's Degree (MS/MA)"), ("Doctorate's Degree (PHD)", 'Doctorate Degree (PHD)')], default='Some High School Education', max_length=200),
        ),
        migrations.AlterField(
            model_name='education',
            name='major_subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='qualification',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
