from django.contrib import admin

# Register your models here.

from .models import PostsCollection

admin.site.register(PostsCollection)