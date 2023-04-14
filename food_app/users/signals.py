from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver
from .models import Profile

""" The post_save signal is typically used to update related models, such as updating a profile model
 when a user model is saved. It can also be used for sending notifications, updating caches, 
 or any other action that needs to be performed after a model is saved.

The post_save signal takes a sender argument, which is the model class that sends the signal, 
and a created argument, which is a boolean indicating whether the instance was created or updated.

To use the post_save signal, you need to import it from the django.db.models.signals module and 
connect it to a function that will be called when the signal is sent."""

@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	instance.profile.save()


