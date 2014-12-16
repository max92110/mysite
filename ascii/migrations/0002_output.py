# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ascii', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Output_text', models.CharField(max_length=200)),
                ('Output_index', models.ForeignKey(to='ascii.Input')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
