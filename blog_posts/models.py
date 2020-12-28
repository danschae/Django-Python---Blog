from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model): # each model inherits from the database
  title = models.CharField(max_length=100) # charfield is varchar
  content = models.TextField() # text field is unrestricted text
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE) 

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})
