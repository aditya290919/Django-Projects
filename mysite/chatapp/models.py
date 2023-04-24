from django.db import models

# Create your models here.
class ChatRoom(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	