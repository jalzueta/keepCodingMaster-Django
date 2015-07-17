# -*- coding: utf-8 -*-
from django.conf import settings

# Hago el campo NO_IMAGE parametrizable a nivel de App
BORRADOR = 'BOR'
TERMINADO = 'FIN'
PUBLICADO = 'PUB'

DEFAULT_POST_STATUS = (
    (BORRADOR, 'Borrador'),
    (TERMINADO, 'Terminado'),
    (PUBLICADO, 'Publicado')
)

POST_STATUS = getattr(settings, 'POST_STATUS', DEFAULT_POST_STATUS)
STATUS_FOR_NEW_POST = getattr(settings, 'STATUS_FOR_NEW_POST', BORRADOR)

# Hago el campo NO_IMAGE parametrizable a nivel de App
DEFAULT_NO_IMAGE = u'http://www.libreriaraimundo.com/frontend/images/no-photo.jpg'
NO_IMAGE = getattr(settings, 'NO_IMAGE', DEFAULT_NO_IMAGE)

BADWORDS = getattr(settings, 'BADWORDS', [])