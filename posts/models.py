from django.db import models
from django.contrib.auth.models import User
from cathegories.models import Cathegory
from wordplease.settings import DEFAULT_IMAGE

BORRADOR = 'BOR'
TERMINADO = 'FIN'
PUBLICADO = 'PUB'

STATUS = (
    (BORRADOR, 'Borrador'),
    (TERMINADO, 'Terminado'),
    (PUBLICADO, 'Publicado')
)

class Post(models.Model):

    owner = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1500)
    # resume = models.CharField(max_length=500, blank=True, null=True, default="{0}".format(body[:200]))
    url = models.URLField(blank=True, null=True, default=DEFAULT_IMAGE)
    publication_data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUS, default=BORRADOR)
    cathegories = models.ManyToManyField(Cathegory)

    def __unicode__(self): #0 param method
        return self.title



