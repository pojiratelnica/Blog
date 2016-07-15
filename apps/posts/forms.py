from django import forms
from models import Posts
from redactor.widgets import RedactorEditor


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ()


class PostsAdminForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
           'text': RedactorEditor(),
        }
        exclude = ()
