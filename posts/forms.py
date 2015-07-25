# -*- coding: utf-8 -*-
from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    """
    Formulario para el modelo Photo
    """
    class Meta:
        model = Post
        exclude = ['author'] #campos de Post excluidos para el formulario

