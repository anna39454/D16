from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *
from .forms import PostForms, CommentForms

class PostList(ListView):

    model = Post # Указываем модель, объекты которой мы будем выводить
    ordering = '-created'     # Поле, которое будет использоваться для сортировки объектов
    template_name = 'post.html'  # Указываем имя шаблона,
    context_object_name = 'posts'  # имя списка, в котором будут лежать все объекты.чтобы обратиться к списку объектов в html-шаблоне
    #paginate_by = 10  # вот так мы можем указать количество записей на странице


class PostDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForms
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'create'


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForms
    model = Post
    template_name = 'post_edit.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')



class CommentCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = CommentForms
    model = Comment
    ordering = '-created'
    template_name = 'comment_create.html'
    context_object_name = 'comment'


class CommentDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Comment
    template_name = 'comment_detail.html'
    context_object_name = 'comments'


class CommentUpdate(LoginRequiredMixin, UpdateView):
    form_class = CommentForms
    model = Comment
    template_name = 'comment_edit.html'


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('post_list')


class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return  render(self.request,'users/invalid_code.html')
            return redirect('account_login')


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'