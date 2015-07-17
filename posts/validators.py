# -*- coding: utf-8 -*-

from posts.settings import BADWORDS
from django.core.exceptions import ValidationError


def badwords_detector(value):
        """
        Valida si en el texto de entrada (value) se han puesto tacos definidos en settings.BADWORDS
        :return: Boolean
        """

        for badword in BADWORDS:
            if badword.lower() in value.lower():
                # Strings unicode para el tema de la codificación de caracteres especiales, tildes...
                raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

        # Si va OK (no hay tacos en value), devuelvo True
        return True
