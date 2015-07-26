# -*- coding: utf-8 -*-
from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.views import PostsQuerySet
from users.views import UserUtils
from posts.settings import PUBLICADO
from posts.permissions import PostPermission
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView

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

"""
class PostDetailAPI(RetrieveUpdateDestroyAPIView, PostsQuerySet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_posts_queryset(self.request)
"""

class PostDetailAPI(GenericAPIView):

    permission_classes = (PostPermission,)

    def get(self, request, pk, idPost):
        blog = UserUtils.getUserBlog(pk)
        post = get_object_or_404(Post, blog=blog, pk=idPost) # devuelve el objeto o, si este no existe, un error 404

        # compruebo si el usuario autenticado puede hacer GET en este user.
        # Hay que hacerlo a mano porque estamos heredando de una GenericAPIView.
        # Al hacer la recuperación del objeto 'post' manualmente, la comprobacion tambien debe ser manual
        self.check_object_permissions(request, post)

        serializer = PostSerializer(post)
        serializer_post = serializer.data
        return Response(serializer_post)

    # Actualizacion de un usuario
    def put(self, request, pk, idPost):
        blog = UserUtils.getUserBlog(pk)
        post = get_object_or_404(Post, blog=blog, pk=idPost) # devuelve el objeto o, si este no existe, un error 404

        # compruebo si el usuario autenticado puede hacer PUT en este user
        # Hay que hacerlo a mano porque estamos heredando de una GenericAPIView
        # Al hacer la recuperación del objeto 'user' manualmente, la comprobacion tambien debe ser manual
        self.check_object_permissions(request, post)

        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Borrado de un usuario
    def delete(self, request, pk, idPost):
        blog = UserUtils.getUserBlog(pk)
        post = get_object_or_404(Post, blog=blog, pk=idPost) # devuelve el objeto o, si este no existe, un error 404

        # compruebo si el usuario autenticado puede hacer DELETE en este user
        # Hay que hacerlo a mano porque estamos heredando de una GenericAPIView
        # Al hacer la recuperación del objeto 'user' manualmente, la comprobacion tambien debe ser manual
        self.check_object_permissions(request, post)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
