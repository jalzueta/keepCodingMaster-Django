# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20150717_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resume',
            field=models.TextField(default=b'', max_length=500, null=True, blank=True),
        ),
    ]
