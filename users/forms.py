from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField() # default is require is true

  class Meta: # meta is used to add configurations to the form, any information that is not a form field such as model, fields, exclude and widgets can be used
    model = User
    fields = ['username', 'email', 'password1', 'password2']