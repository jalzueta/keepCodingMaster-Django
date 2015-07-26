# -*- coding: utf-8 -*-
from django.db import models
from cathegories.models import Cathegory
from posts.settings import NO_IMAGE, POST_STATUS, STATUS_FOR_NEW_POST
from posts.validators import badwords_detector
from blogs.models import Blog
from posts.settings import PUBLICADO
from datetime import datetime

class Post(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1500, validators=[badwords_detector])
    resume = models.TextField(max_length=500, blank=True, null=True, default="", validators=[badwords_detector])
    url = models.URLField(blank=True, null=True, default=NO_IMAGE)
    publication_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=POST_STATUS, default=STATUS_FOR_NEW_POST)
    cathegories = models.ManyToManyField(Cathegory, blank=True, null=True)
    blog = models.ForeignKey(Blog)

    def save(self, *args, **kwargs):
        if self.resume == "":
            self.resume = self.body[:200]
        if self.status == PUBLICADO:
            self.publication_date = datetime.now()
        return super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title




