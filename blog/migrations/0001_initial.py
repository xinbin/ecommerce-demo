# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('lead', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=512)),
                ('author', models.CharField(default=b'Anonymous', max_length=50, blank=True)),
                ('img', models.CharField(max_length=255, verbose_name=b'Image URL', blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default=b'active', max_length=10, choices=[(b'active', b'Active'), (b'inactive', b'Disabled'), (b'archived', b'Archived'), (b'deleted', b'Deleted')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
