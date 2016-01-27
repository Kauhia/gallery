from django.db import models
from django.core.urlresolvers import reverse
from images.models import Image

class Comment(models.Model):
	user = models.CharField(max_length=25)
	text  =  models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	image = models.ForeignKey('images.Image', on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('image-comments', kwargs={'pk': self.image.pk})