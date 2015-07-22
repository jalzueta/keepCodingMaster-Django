# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View, ListView
from posts.settings import PUBLICADO
from posts.models import Post
from django.contrib.auth.models import User


class HomeView(View):
    """
    Esta funcion devuelve el 'home' de mi pagina web
    """
    def get(self, request):
        posts = Post.objects.filter(status=PUBLICADO).order_by('-publication_data')
        context = {
            'posts_list': posts[:5]
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