# -*- coding: utf-8 -*-
from django.db import models

class Cathegory(models.Model):

    name = models.CharField(max_length=50)

    def __unicode__(self): #0 param method
        return self.name
