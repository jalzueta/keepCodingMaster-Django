from django.db import models

class Cathegory(models.Model):

    name = models.CharField(max_length=50)
