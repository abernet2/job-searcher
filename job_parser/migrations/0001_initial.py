# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=150)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_parser.Company')),
            ],
        ),
        migrations.CreateModel(
            name='PostHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orig_header', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_parser.JobPost')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='post_header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_parser.PostHeader'),
        ),
    ]
