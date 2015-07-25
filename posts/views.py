# -*- coding: utf-8 -*-
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import View, ListView
from posts.settings import PUBLICADO
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from wordplease.settings import NO_IMAGE

class PostsQuerySet(object):

    def get_posts_queryset(self, request):
        if not request.user.is_authenticated():
            post = Post.objects.filter(status=PUBLICADO)

        elif request.user.is_superuser:
            post = Post.objects.all()

        else:
            # Operacion "OR" para una query a la BB.DD -> 'Q'
            # '|' es un operador "OR" a nivel de bit
            post = Post.objects.filter(Q(author=request.user) | Q(status=PUBLICADO))

        """# devuelve un iterador de modelos: es un objeto con la query configurada, no una lista de photos en memoria.
        Se va a poder seguir configurando la query, por ejemplo en DetailView
        """
        return post

class HomeView(View):
    """
    Esta funcion devuelve el 'home' de mi pagina web
    """
    def get(self, request):
        posts = Post.objects.filter(status=PUBLICADO).order_by('-publication_data')
        context = {
            'posts_list': posts[:10]
        }
        return render(request, 'posts/home.html', context)

class BlogsView(ListView):

    model = User
    template_name = 'posts/blogs.html'

    """
    def get_queryset(self):
        queryset = super(BlogsView, self).get_queryset()
        return queryset.filter(owner=self.request.user)
    """

class DetailBlogView(ListView, PostsQuerySet):

    def get(self, request, pk):
        """
        Carga la página de detalle de un blog
        :param request: HttpRequest
        :param pk: username
        :return: HttpResponse
         """
        posts = self.get_posts_queryset(request).filter(author__username__exact=pk).order_by('-publication_data')
        users = User.objects.filter(username=pk)
        user = users[0].first_name + " " + users[0].last_name
        context = {
            'posts_list': posts,
            'pk': pk,
            'user': user
        }
        return render(request, 'posts/blog_detail.html', context)

class DetailPostView(View, PostsQuerySet):

    def get(self, request, pk, idPost):
        """
        Carga la página de detalle de un post
        :param request: HttpRequest
        :param pk: username, idPost: id del post
        :return: HttpResponse
         """
        possible_posts = self.get_posts_queryset(request).filter(author__username__exact=pk, pk=idPost)
        post = possible_posts[0] if len(possible_posts) >= 1 else None
        if post is not None:
            context = {
                'post': post,
                'url_no_image': NO_IMAGE
            }
            return render(request, 'posts/post_detail.html', context)
        else:
            return HttpResponseNotFound('No existe el post o no tiene acceso') # 404 not found

class CreatePostView(View):

    def render(self, request, context):
        return render(request, 'posts/create_post.html', context)

    # Se decora al decorador para que funcione con vistas basadas en clases.
    # @login_required() solo funciona para vistas basadas en funciones
    @method_decorator(login_required()) # Decorador que se encarga de comprobar si el usuario está autenticado. La redireccion en caso de no estar autenticado, al 'LOGIN_URL' de settings
    def get(self, request):
        """
        Muestra un formulario para crear un post
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = PostForm()

        context = {
            'form': form,
            'success_message': ''
        }
        return self.render(request, context)

    # Se decora al decorador para que funcione con vistas basadas en clases.
    # @login_required() solo funciona para vistas basadas en funciones
    @method_decorator(login_required()) # Decorador que se encarga de comprobar si el usuario está autenticado. La redireccion en caso de no estar autenticado, al 'LOGIN_URL' de settings
    def post(self, request):
        """
        Crea un post en base a la información POST
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''
        post_with_author = Post()
        post_with_author.author = request.user # asigno como propietario de la foto el usuario autenticado
        form = PostForm(request.POST, instance=post_with_author) # Coge los datos del formulario sobreescribe los campos que tiene el objeto 'photo_with_owner'
        if form.is_valid():
            new_post = form.save() # Guarda el objeto en BB.DD. y me lo devuelve
            form = PostForm() # Forzamos a que el formulario se vacie si la creacion de la foto ha sido satisfactoria
            success_message = 'Guardado con éxito!'
            success_message += '<a href = "{0}">'.format(
                reverse('post_detail', args=[new_post.author.username,new_post.pk])
            )
            success_message += 'Ver post'
            success_message += '</a>'
        context = {
            'form': form,
            'success_message': success_message
        }
        return self.render(request, context)