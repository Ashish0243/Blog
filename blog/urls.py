from django.contrib import admin
from django.urls import path,include
from .views import BlogPosts,BlogDetail,NewBlogPost,EditBlogPost,DeletePost

urlpatterns = [
    path('home/',BlogPosts.as_view(),name="home"),
    path('post/<int:pk>/',BlogDetail.as_view(),name="post_detail"),
    path('post/new/',NewBlogPost.as_view(),name='new_post'),
    path('post/<int:pk>/edit',EditBlogPost.as_view(),name="edit_post"),
    path('post/<int:pk>/delete',DeletePost.as_view(),name="delete_post")
]
