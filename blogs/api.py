# -*- coding: utf-8 -*-
from blogs.models import Blog
from blogs.serializers import BlogSerializer
from posts.serializers import PostListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.views import PostsQuerySet
from users.views import UserUtils

class BlogsListAPI(APIView):

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


class BlogDetailAPI(APIView, PostsQuerySet):

    def get(self, request, pk):
        blog = UserUtils.getUserBlog(pk)
        posts = self.get_posts_queryset(request).filter(blog__name=blog.name).order_by('-publication_date')
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)



