# -*- coding: utf-8 -*-
from django import forms
from posts.validators import badwords_detector
from wordplease.settings import DEFAULT_BLOG_NAME

class LoginForm(forms.Form):

    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput) #Campo con texto oculto


class SignupForm(forms.Form):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.CharField(label="Email")
    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    blog_name = forms.CharField(label="Nombre del blog", validators=[badwords_detector])