# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productora', '0001_initial'),
        ('actor', '0001_initial'),
        ('director', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pelicula',
            fields=[
                ('nombrePelicula', models.CharField(max_length=45, serialize=False, primary_key=True)),
                ('estreno', models.DateField()),
                ('foto', models.ImageField(upload_to=b'static')),
                ('precio', models.IntegerField(max_length=45)),
                ('nombreActor', models.ForeignKey(to='actor.actor')),
                ('nombreDirector', models.ForeignKey(to='director.director')),
                ('nombreProductora', models.ForeignKey(to='productora.productora')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
