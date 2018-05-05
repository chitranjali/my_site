from django.shortcuts import render
from django.views import generic
from .models import Blog_post
# Create your views here.

class PostListView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return Blog_post.objects.all()

# class PostDetailView(generic.DetailView):
#     model = Blog_post
#     template_name = 'blog/detail.html'