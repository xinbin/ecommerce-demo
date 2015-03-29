# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('carousel', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=10)),
                ('small_image', models.CharField(max_length=255)),
                ('large_image', models.CharField(max_length=255)),
                ('special', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('status', models.CharField(default=b'active', max_length=10, choices=[(b'active', b'Active'), (b'inactive', b'Disabled'), (b'archived', b'Archived'), (b'deleted', b'Deleted')])),
                ('category', models.ForeignKey(to='ecommerce.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
