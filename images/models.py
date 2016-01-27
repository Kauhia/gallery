import uuid
import os
from django.db import models
from django.core.urlresolvers import reverse

# http://stackoverflow.com/questions/2673647/enforce-unique-upload-file-names-using-django
def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images', filename)

class Image(models.Model):
	text  =  models.CharField(max_length=200)
	image = models.ImageField(upload_to=get_image_path)

	def get_absolute_url(self):
		return reverse('image-comments', kwargs={'pk': self.pk})