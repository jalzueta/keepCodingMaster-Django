# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import posts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20150717_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=1500, validators=[posts.validators.badwords_detector]),
        ),
        migrations.AlterField(
            model_name='post',
            name='resume',
            field=models.TextField(default=b'', max_length=500, null=True, blank=True, validators=[posts.validators.badwords_detector]),
        ),
    ]
