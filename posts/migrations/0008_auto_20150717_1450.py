# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20150717_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cathegories',
            field=models.ManyToManyField(to='cathegories.Cathegory', null=True, blank=True),
        ),
    ]
