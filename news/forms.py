from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()




class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()



    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class':'form-control'}),
            #'photo': forms.ImageField(upload_to='photos/%Y%m%d', height_field=None, width_field=None, max_length=100),
        }
    captcha = CaptchaField()


    # title = forms.CharField(max_length=150, label='название', widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label='текст', required=False, widget=forms.Textarea(attrs={
    #     "class": "form-control",
    #     "rows": 5
    # }))
    # is_published = forms.BooleanField(label='публикация', initial=True)
    # category = forms.ModelChoiceField(empty_label='выберите категорию', label='категория', queryset=Category.objects.all(),
    # widget=forms.Select(attrs={"class": "form-control"}))
    #
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if re.match(r'\d', title):
    #         raise ValidationError('название не должно содержать цифры')
    #     return title