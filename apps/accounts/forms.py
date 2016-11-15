# coding: utf-8
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label='Password confirmation')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password', 'password_confirmation')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': u'Логин',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': u'Имя',
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': u'Пароль',
            }),
            'password_confirmation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': u'Подтвердите пароль',
            }),
        }

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError(u'Давай больше пиши')
        return password

        def clean(self):
            pass
        # exclude = ()
