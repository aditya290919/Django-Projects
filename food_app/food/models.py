from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
	user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	item_name = models.CharField(max_length=200)
	item_desc = models.CharField(max_length=200)
	item = models.IntegerField()
	item_image = models.CharField(max_length=500, default='https://tse3.mm.bing.net/th?id=OIP.N0JNvG4iu61u97rvu8FZWgHaFe&pid=Api&P=0')

	def get_absolute_url(self):
		return reverse("food:detail",kwargs={"pk":self.pk})
