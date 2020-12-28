from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post # use . if in the same directory

# def home(request):
#   context = {
#     'posts': Post.objects.all()
#   }
#   return render(request, 'blog_posts/home.html', context) # this is still using a httpresponse

class PostListView(ListView):
  model = Post
  # looks for template at <app>/<model>_<viewtype>.html
  template_name = 'blog_posts/home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']

class PostDetailView(DetailView):
  model = Post

def about(request):
  return render(request, 'blog_posts/about.html', {'title': 'About Page'})
