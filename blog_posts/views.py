from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {
    'author': 'DanielS',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'December 23rd, 2020'
  },
  {
    'author': 'Dude',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'December 24th, 2020'
  }
]
# Create your views here.
def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog_posts/home.html', context) # this is still using a httpresponse

def about(request):
  return render(request, 'blog_posts/about.html')
