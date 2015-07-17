# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150717_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resume',
            field=models.CharField(default=b'{0}', max_length=500, null=True, blank=True),
        ),
    ]
