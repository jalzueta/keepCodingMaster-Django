# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as wordplease_logout, authenticate, login as wordplease_login #importo con un alias, para que no haya conflicto de nombres con mi funcion 'logout'
from users.forms import LoginForm, SignupForm
from django.views.generic import View
from django.contrib.auth.models import User
from blogs.models import Blog
from django.core.urlresolvers import reverse

class LoginView(View):

    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    wordplease_login(request, user)
                    url = request.GET.get('next', 'posts_home')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')

        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            wordplease_logout(request)
        return redirect('posts_home')

class SignupView(View):

    def get(self, request):
        error_messages = []
        form = SignupForm()
        context = {
            'errors': error_messages,
            'signup_form': form
        }
        return render(request, 'users/signup.html', context)

    def post(self, request):
        error_messages = []
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('usr')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('pwd')
            blog_name = form.cleaned_data.get('blog_name')
            users = User.objects.filter(username=username)
            if len(users) == 0:
                new_user = User()
                new_user.username = username
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.email = email
                new_user.set_password(password)
                new_user.save()
                blog = Blog()
                blog.name = blog_name
                blog.author = new_user
                blog.save()
                return redirect('posts_home')
            else:
                error_messages.append('El username {0} ya existe. Pruebe con otro'.format(username))

        context = {
            'errors': error_messages,
            'signup_form': form
        }
        return render(request, 'users/signup.html', context)