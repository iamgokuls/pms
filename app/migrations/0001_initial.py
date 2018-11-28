# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 15:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('compid', models.IntegerField(primary_key=True, serialize=False)),
                ('compname', models.TextField(max_length=100)),
                ('address', models.TextField()),
                ('contactno', models.IntegerField()),
                ('contactemail', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('jobid', models.IntegerField(primary_key=True, serialize=False)),
                ('jobtype', models.TextField(max_length=100)),
                ('course', models.TextField(max_length=50)),
                ('branch', models.TextField(max_length=50)),
                ('salary', models.IntegerField()),
                ('mincgpa', models.FloatField()),
                ('maxarrears', models.IntegerField()),
                ('compid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Company')),
            ],
            options={
                'db_table': 'job',
            },
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=20)),
                ('password', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('address', models.TextField()),
                ('mobno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('course', models.TextField(max_length=50)),
                ('branch', models.TextField(max_length=50)),
                ('cgpa', models.FloatField()),
                ('arrears', models.IntegerField()),
                ('sslc', models.FloatField()),
                ('plustwo', models.FloatField()),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]