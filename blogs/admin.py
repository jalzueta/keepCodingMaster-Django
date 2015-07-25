from django.contrib import admin
from blogs.models import Blog

class BlogAdmin(admin.ModelAdmin):

    list_display = ('name', 'author_name')
    list_filter = ('author',)
    search_fields = ('name', 'author_name')

    def author_name(self, obj): # 'obj' es un objeto 'blog'
        return obj.author.first_name + u' ' + obj.author.last_name

    # definimos atributos a la funcion 'author_name'
    author_name.short_description = 'Blog author' # nombre de la columna en el admin
    author_name.admin_order_field = 'author' # le decimos que esa columna se ordene por el campo 'author' del modelo

    # Tuneamos el editor de posts del administrador
    fieldsets = (
        (None, {
            'fields': ('name', 'author'),
            'classes': ('wide',)
        }),
    )

admin.site.register(Blog, BlogAdmin)
