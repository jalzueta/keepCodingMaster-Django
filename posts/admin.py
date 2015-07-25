# -*- coding: utf-8 -*-
from django.contrib import admin
from posts.models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author_name', 'blog', 'status', 'publication_date')
    list_filter = ('status', 'cathegories')
    search_fields = ('title', 'resume', 'body')

    def author_name(self, obj): # 'obj' es un objeto 'post'
        return obj.blog.author.first_name + u' ' + obj.blog.author.last_name

    # definimos atributos a la funcion 'author_name'
    author_name.short_description = 'Post author' # nombre de la columna en el admin
    author_name.admin_order_field = 'blog.author' # le decimos que esa columna se ordene por el campo 'author' del modelo

    # Tuneamos el editor de posts del administrador
    fieldsets = (
        (None, {
            'fields': ('title', 'blog', 'status'),
            'classes': ('wide',)
        }),
        ('Resume & Body', {
            'fields': ('resume', 'body'),
            'classes': ('wide',)
        }),
        ('Extra info', {
            'fields': ('url', 'cathegories'),
            'classes': ('wide', 'collapse')
        })
    )

admin.site.register(Post, PostAdmin)
