# -*- coding: utf-8 -*-
from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.views import PostsQuerySet
from users.views import UserUtils
from posts.settings import PUBLICADO

# Listado de posts para la home (todos los post PUBLICADOS)
class PostListAPI(ListCreateAPIView, PostsQuerySet):

    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return PostSerializer if self.request.method == "POST" else PostListSerializer

    def get_queryset(self):
        return self.get_posts_queryset(self.request)

    # metodo que se ejecuta antes de llamar al metodo 'serializer.save()' de escritura en BB.DD.
    def perform_create(self, serializer):
        # forzamos a que el 'blog' del post creado tenga que ser el del usuario autenticado
        blog = UserUtils.getUserBlog(self.request.user.username)
        serializer.save(blog=blog, status=PUBLICADO)

class PostDetailAPI(RetrieveUpdateDestroyAPIView, PostsQuerySet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_posts_queryset(self.request)
