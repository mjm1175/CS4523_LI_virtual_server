# Generated by Django 4.0.4 on 2022-04-23 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('Username', models.AutoField(primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=50)),
                ('FirstName', models.CharField(max_length=25)),
                ('LastName', models.CharField(max_length=25)),
                ('Degree', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employers',
            fields=[
                ('Username', models.AutoField(primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=50)),
                ('FirstName', models.CharField(max_length=25)),
                ('LastName', models.CharField(max_length=25)),
                ('CompanyName', models.CharField(max_length=50)),
                ('ImplicitBiasFile', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('Title', models.AutoField(primary_key=True, serialize=False)),
                ('JobType', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Part Time'), ('RT', 'Remote')], default='FT', max_length=10)),
                ('experience', models.CharField(choices=[('t1', 'Less than 2yrs'), ('t2', '2yrs - 5yrs'), ('t3', '5yrs - 10yrs'), ('t4', '10yrs - 15yrs'), ('t5', 'More than 15yrs')], default='t1', max_length=10)),
                ('summary', models.TextField()),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('logo', models.ImageField(default='default-job.png', upload_to='upload_images')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
