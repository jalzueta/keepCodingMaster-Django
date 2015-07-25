# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from blogs.models import Blog
from django.db.models import Q
from django.views.generic import ListView
from posts.settings import PUBLICADO
from posts.models import Post
from blogs.models import Blog

class PostsQuerySet(object):

    def get_posts_queryset(self, request):

        if request.user.is_superuser:
            post = Post.objects.all()

        elif request.user.username == self.kwargs.get('pk'):
            post = Post.objects.all()

        else:
            post = Post.objects.filter(status=PUBLICADO)

        """# devuelve un iterador de modelos: es un objeto con la query configurada, no una lista de photos en memoria.
        Se va a poder seguir configurando la query, por ejemplo en DetailView
        """
        return post

class BlogsView(ListView):

    model = Blog
    template_name = 'blogs/blogs.html'


class DetailBlogView(ListView, PostsQuerySet):

    def get(self, request, pk):
        """
        Carga la página de detalle de un blog
        :param request: HttpRequest
        :param pk: username
        :return: HttpResponse
         """
        blogs = Blog.objects.filter(author__username__exact=pk)
        blog = blogs[0]
        posts = self.get_posts_queryset(request).filter(blog__name=blog.name).order_by('-publication_date')
        context = {
            'posts_list': posts,
            'pk': pk,
            'blog': blog
        }
        return render(request, 'blogs/blog_detail.html', context)
