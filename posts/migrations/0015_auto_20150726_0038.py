# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20150725_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cathegories',
            field=models.ManyToManyField(to='cathegories.Cathegory', null=True, blank=True),
        ),
    ]
