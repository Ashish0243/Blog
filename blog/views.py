from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import PostsCollection
from django.urls import reverse,reverse_lazy
# Create your views here.

class BlogPosts(ListView):
    model=PostsCollection
    template_name='home.html'
    context_object_name='posts_obj'
    
class BlogDetail(DetailView):
    model=PostsCollection
    template_name='detail.html'
    context_object_name='post'
    
class NewBlogPost(CreateView):
    model=PostsCollection
    template_name="new_post.html"
    fields="__all__"
    
class EditBlogPost(UpdateView):
    model=PostsCollection
    template_name="edit_post.html"
    fields=['title','body']
    
class DeletePost(DeleteView):
    model=PostsCollection
    template_name="delete.html"
    success_url=reverse_lazy('home')
    
