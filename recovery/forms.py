from django.forms import ModelForm
from django import forms
from .models import Post

class PostCreationForm(ModelForm):

    class Meta:
        model = Post
        exclude = [
            'created_at',
            'created_by',
            'published_at',
            ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Введите название'
                    }),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Добавьте краткое описание',
                    }),
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Введите статью',
                    }),
            }
