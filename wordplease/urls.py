# -*- coding: utf-8 -*-
"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from posts.views import HomeView, DetailPostView, CreatePostView, UpdatePostView
from blogs.views import BlogsView, DetailBlogView
from users.views import LoginView, LogoutView, SignupView
from users.api import UserListAPI, UserDetailAPI
from blogs.api import BlogsListAPI, BlogDetailAPI
from posts.api import PostListAPI, PostDetailAPI

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    #Posts URLs
    url(r'^$', HomeView.as_view(), name='posts_home'),
    url(r'^blogs/(?P<pk>[-\w]+)/(?P<idPost>[0-9]+)/$', DetailPostView.as_view(), name='post_detail'),
    url(r'^new-post$', CreatePostView.as_view(), name='create_post'),
    url(r'^update-post/(?P<pk>[-\w]+)/(?P<idPost>[0-9]+)/$', UpdatePostView.as_view(), name='update_post'),

    # Posts API URLs
    # Listado de posts para la home/Creacion de un post nuevo
    url(r'api/1.0/posts/$', PostListAPI.as_view(), name='post_list_api'),

    #Blogs URLs
    url(r'^blogs/$', BlogsView.as_view(), name='blogs'),
    url(r'^blogs/(?P<pk>[-\w]+)/$', DetailBlogView.as_view(), name='blog_detail'),

    # Blogs API URLs
    # Listado de blogs
    url(r'api/1.0/blogs/$', BlogsListAPI.as_view(), name='blog_list_api'),
    # Detalle de un blog: listado de posts del blog
    url(r'api/1.0/blogs/(?P<pk>[-\w]+)/$', BlogDetailAPI.as_view(), name='blog_detail_api'),
    # Detalle/Actualizacion/Borrado de un post
    url(r'api/1.0/blogs/(?P<pk>[-\w]+)/(?P<idPost>[0-9]+)/$', PostDetailAPI.as_view(), name='blog_detail_api'),

    #Users URLs
    url(r'^login', LoginView.as_view(), name='users_login'),
    url(r'^logout', LogoutView.as_view(), name='users_logout'),
    url(r'^signup', SignupView.as_view(), name='users_signup'),

    # Users API URLs
    #Listar usuarios/Crear un nuevo usuario
    url(r'api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),
    # Detalle/Actualizacion/Borrado de un usuario
    url(r'api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api')
]
