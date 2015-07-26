# -*- coding: utf-8 -*-
from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField('blogAuthor')
    blog_name = serializers.SerializerMethodField('blogName')

    def blogAuthor(self, obj):
        return '{0} {1}'.format(obj.blog.author.first_name, obj.blog.author.last_name)

    def blogName(self, obj):
        return obj.blog.name

    class Meta:
        model = Post
        read_only_fields = ('blog',)
        #fields = ('id', 'title', 'url', 'resume', 'publication_date', 'blog_name', 'author')

class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ('id', 'title', 'url', 'resume', 'publication_date', 'author')
