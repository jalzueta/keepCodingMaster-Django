# -*- coding: utf-8 -*-
from django.contrib import admin
from posts.models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author_name', 'status')
    list_filter = ('status', 'cathegories')
    search_fields = ('title', 'resume', 'body')

    def author_name(self, obj): # 'obj' es un objeto 'photo'
        return obj.author.first_name + u' ' + obj.author.last_name

    # definimos atributos a la funcion 'owner_name'
    author_name.short_description = 'Post author' # nombre de la columna en el admin
    author_name.admin_order_field = 'author' # le decimos que esa columna se ordene por el campo 'author' del modelo

    # Tuneamos el editor de posts del administrador
    fieldsets = (
        (None, {
            'fields': ('title',),
            'classes': ('wide',)
        }),
        ('Resume & Body', {
            'fields': ('resume', 'body'),
            'classes': ('wide',)
        }),
        ('Extra info', {
            'fields': ('url', 'status', 'cathegories'),
            'classes': ('wide', 'collapse') # 'collapse', hace la seccion plegable/desplegable
        })
    )

admin.site.register(Post, PostAdmin)
