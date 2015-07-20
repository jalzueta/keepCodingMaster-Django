from django.shortcuts import render
from django.views.generic import View, ListView
from posts.settings import PUBLICADO
from posts.models import Post


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

