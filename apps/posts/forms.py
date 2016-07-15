# coding: utf-8
from django import forms
from models import Posts
# from django.contrib.auth.models import User
from redactor.widgets import RedactorEditor


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        # Posts.title = forms.CharField(label='Your name')
        widgets = {
           'text': forms.Textarea(attrs={
                'class': 'form-control',
            }),
           # 'likes': forms.IntegerField(attrs={
           #      'class': 'fofm-control',
           #  })
           'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': u'Название',
            }),
           'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': u'Ссылка',
            }),
           'author': forms.Select(attrs={
                'class': 'form-control',
            }),
           'category': forms.Select(attrs={
                'class': 'form-control',
            }),
           'image': forms.FileInput(attrs={
                'class': 'btn btn-primary',
            }),
           # 'display': forms.CheckboxInput(attrs={
           #      'class': 'form-control',
           #  }),
           'likes': forms.TextInput(attrs={
                'class': 'form-control',
            }),
           'dislikes': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }
        exclude = ()


class PostsAdminForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
           'text': RedactorEditor(),
        }
        exclude = ()


# class UserAutorization(forms.ModelForm):
#     class Meta:
#         model = User
#         exclude = ()
