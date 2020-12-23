from django.shortcuts import render
from django.http import HttpResponse
from .models import Post # use . if in the same directory

def home(request):
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'blog_posts/home.html', context) # this is still using a httpresponse

def about(request):
  return render(request, 'blog_posts/about.html', {'title': 'About Page'})
