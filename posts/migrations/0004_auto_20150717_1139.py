# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resume',
            field=models.CharField(default=b'', max_length=500, null=True, blank=True),
        ),
    ]
