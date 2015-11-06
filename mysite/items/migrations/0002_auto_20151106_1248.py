# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('image_description', models.CharField(max_length=10)),
                ('link', models.URLField(verbose_name='link to item')),
                ('date', models.DateField(verbose_name='date of picture')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('map_name', models.CharField(max_length=20)),
                ('date', models.DateField(verbose_name='date of map')),
                ('link', models.URLField(verbose_name='link to item')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('site_name', models.CharField(max_length=30)),
                ('additional_text', models.CharField(max_length=30)),
                ('pub_date', models.DateField(verbose_name='data published')),
                ('location', models.CharField(max_length=10)),
                ('radius', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('song_name', models.CharField(max_length=10)),
                ('compositor_name', models.CharField(max_length=15)),
                ('singer_name', models.CharField(max_length=15)),
                ('link', models.URLField(verbose_name='link to item')),
                ('date', models.DateField(verbose_name='date of picture')),
                ('site', models.ForeignKey(to='items.Site')),
            ],
        ),
        migrations.CreateModel(
            name='Travelouge',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('traveler_name', models.CharField(max_length=20)),
                ('bib_info', models.URLField(verbose_name='link to bibliographic info')),
                ('description', models.CharField(max_length=100)),
                ('site', models.ForeignKey(to='items.Site')),
            ],
        ),
        migrations.RemoveField(
            model_name='type',
            name='item',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.AddField(
            model_name='map',
            name='site',
            field=models.ForeignKey(to='items.Site'),
        ),
        migrations.AddField(
            model_name='image',
            name='site',
            field=models.ForeignKey(to='items.Site'),
        ),
    ]
