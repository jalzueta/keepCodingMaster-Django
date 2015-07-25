# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from posts.validators import badwords_detector

class Blog(models.Model):

    author = models.ForeignKey(User)
    name = models.CharField(max_length=200, validators=[badwords_detector], blank=True, null=True)

    def __unicode__(self):
        return self.name
