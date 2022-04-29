# Generated by Django 4.0.4 on 2022-04-29 19:55

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_experience_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(choices=[('Employer', 'Employer'), ('Applicant', 'Applicant')], default='Applicant', max_length=10)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='employers',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='Applicants',
        ),
        migrations.DeleteModel(
            name='Employers',
        ),
    ]
