# -*- coding: utf-8 -*-
from cathegories.models import Cathegory
from django.contrib import admin

class CathegoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)

    # Tuneamos el editor de posts del administrador
    fieldsets = (
        ('Name', {
            'fields': ('name',),
            'classes': ('wide',)
        }),
    )

admin.site.register(Cathegory, CathegoryAdmin)
