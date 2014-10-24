# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productora',
            fields=[
                ('nombre', models.CharField(max_length=45, serialize=False, primary_key=True)),
                ('direccion', models.CharField(max_length=45)),
                ('foto', models.ImageField(upload_to=b'static')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
