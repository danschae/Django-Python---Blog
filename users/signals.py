from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#kwards just accepts any additonal keywords on the function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

def save_profile(sender, instance, **kwards):
  instance.profile.save()