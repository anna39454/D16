from allauth.account.forms import SignupForm
from string import hexdigits
import random

from django.conf import  settings
from django.core.mail import send_mail
from django.db import models
from django import forms
from .models import Post, Comment
class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = '__all__'
        fields = ['author', 'post', 'text']
        labels = {'author': 'Автор', 'post': 'Коментарий', 'text': 'Содержание коментария'}


class CommonSignupForms(SignupForm):
    def save(self, request):
        user = super(CommonSignupForms,self).save(request)
        user.is_active = False
        code = ''.join(random.sample(hexdigits, 5))
        user.code = code
        user.save()
        send_mail(
            subject= f'Код активации',
            message= f'Код активации аккаунта: {code}',
            from_email= settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return user