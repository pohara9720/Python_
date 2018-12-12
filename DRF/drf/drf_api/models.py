from django.conf import settings
from django.db import models


def upload_status_img(instance,file):
	return "updates/{user}/{file}".format(user=instance.user,file=file)


# Create your models here.
class StatusQuerySet(models.QuerySet):
	pass

class StatusManager(models.Manager):
	def get_queryset(self):
		return StatusQuerySet(self.model,using=self._db)
class Status(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	content = models.TextField(null=True,blank=True)
	image = models.ImageField(upload_to=upload_status_img,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = StatusManager()

	def __str__(self):
		return str(self.content)[:50]

	class Meta:
		verbose_name = 'Status Post'
		verbose_name_plural = 'Status Posts'
