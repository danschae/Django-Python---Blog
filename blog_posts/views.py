from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
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

class PostCreateView(LoginRequiredMixin,CreateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
  model = Post
  success_url = "/"

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False

def about(request):
  return render(request, 'blog_posts/about.html', {'title': 'About Page'})
