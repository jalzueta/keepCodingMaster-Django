# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import posts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[posts.validators.badwords_detector]),
        ),
    ]
