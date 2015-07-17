# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cathegories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=1500)),
                ('url', models.URLField(default='http://www.libreriaraimundo.com/frontend/images/no-photo.jpg', null=True, blank=True)),
                ('publication_data', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default=b'BOR', max_length=3, choices=[(b'BOR', b'Borrador'), (b'FIN', b'Terminado'), (b'PUB', b'Publicado')])),
                ('cathegories', models.ManyToManyField(to='cathegories.Cathegory')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
