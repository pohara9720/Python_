import json # can do this to do json.loads or json.

from django.conf import settings 
from django.db import models
from django.core.serializers import serialize

#pillow lets you upload images

def upload_update_img(instance,file):
	return "updates/{user}/{file}".format(user=instance.user,file=file)
# Create your models here.


class UpdateQuerySet(models.QuerySet):
	def serialize(self):
		qs = self
		return serialize('json',qs)


class UpdateManager(models.Manager):
	def get_queryset(self):
		return UpdateQuerySet(self.model, using= self._db)



class Update(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	content = models.TextField(blank=True,null=True)
	image = models.ImageField(upload_to = upload_update_img,blank=True,null=True)
	timestamp = models.DateTimeField(auto_now=True)
	updated_time = models.DateTimeField(auto_now_add=True)
	# using the update manager makes it easier and cleaner to serialize the response via the model so that the views are nicer
	objects = UpdateManager()

	def __str__(self):
		return self.content or ""

	def serialize(self):
		return serialize('json',[self])
