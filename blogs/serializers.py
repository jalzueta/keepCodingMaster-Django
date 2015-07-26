# -*- coding: utf-8 -*-
from rest_framework import serializers
from blogs.models import Blog
from django.core.urlresolvers import reverse
from posts.models import Post
from posts.views import PUBLICADO

class BlogSerializer(serializers.ModelSerializer):

    blog_name = serializers.SerializerMethodField('blogName')
    blog_url = serializers.SerializerMethodField('blogUrl')
    number_of_posts = serializers.SerializerMethodField('numberOfPosts')

    class Meta:
        model = Blog
        fields = ('id', 'blog_name', 'blog_url', 'number_of_posts')

    def blogName(self, obj):
        return obj.name

    def blogUrl(self, obj):
        return reverse('blog_detail', kwargs={'pk': obj.author.username})

    def numberOfPosts(self, obj):
        posts = Post.objects.filter(blog=obj, status=PUBLICADO)
        return len(posts)