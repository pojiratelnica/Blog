# coding: utf-8
from django import forms
from models import Posts
# from django.contrib.auth.models import User
from redactor.widgets import RedactorEditor
# from django.core import validators
from PIL import Image


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'slug', 'author', 'category', 'display', 'image', 'text')
        widgets = {
           'text': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': '3',
                'rows': '4',
            }),
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
        }
        exclude = ()

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError(u'Давай больше пиши')
        return title

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        img = Image.open(image)
        width, height = img.size
        if image:
            if height < 400 and width < 400:
                raise forms.ValidationError(u'Слишком маленькое изображение < 400px*400px')
            elif image._size < 1*1024*1024:
                raise forms.ValidationError(u'Слишком маленькое изображение < 1mb')
            elif image._size > 4*1024*1024:
                raise forms.ValidationError(u'Труба тяжелое изображение > 4mb')
            return image
        else:
            raise forms.ValidationError(u'Не могу загрузить изображение')

    def clean(self):
        pass


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
