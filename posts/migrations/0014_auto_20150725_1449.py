# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_remove_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publication_data',
            new_name='publication_date',
        ),
    ]
