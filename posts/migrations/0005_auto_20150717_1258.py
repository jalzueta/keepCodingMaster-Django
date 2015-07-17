# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20150717_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resume',
            field=models.CharField(default=models.TextField(max_length=1500), max_length=500, null=True, blank=True),
        ),
    ]
