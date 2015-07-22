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
from posts.views import HomeView, BlogsView
from users.views import LoginView, LogoutView, SignupView
from django.views.generic import RedirectView

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    #Blogs/Posts URLs
    url(r'^$', HomeView.as_view(), name='posts_home'),
    url(r'^blogs/$', BlogsView.as_view(), name='blogs'),
    #url(r'^blogs/(?P<pk>[-\w]+)/$', DetailBlogView.as_view(), name='blog_detail'),
    #url(r'^blogs/(?P<pk>[-\w]+)/(?P<idPost>[0-9]+)/$', DetailPostView.as_view(), name='post_detail'),

    #Users URLs
    url(r'^login', LoginView.as_view(), name='users_login'),
    url(r'^logout', LogoutView.as_view(), name='users_logout'),
    url(r'^signup', SignupView.as_view(), name='users_signup'),
    #url(r'^one', RedirectView.as_view(url='users_login')),
]
