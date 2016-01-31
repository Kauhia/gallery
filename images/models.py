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
	thumbnail = models.ImageField(upload_to=get_image_path)

	def get_absolute_url(self):
		return reverse('image-comments', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):
		self.create_thumbnail()
		super(Image, self).save()

	# based on: https://gist.github.com/valberg/2429288
	def create_thumbnail(self):
		from PIL import Image, ImageOps
		from io import BytesIO
		from django.core.files.uploadedfile import SimpleUploadedFile
		import os

		THUMBNAIL_SIZE = (300,300)

		DJANGO_TYPE = self.image.file.content_type

		if DJANGO_TYPE == 'image/jpeg':
			PIL_TYPE = 'jpeg'
			FILE_EXTENSION = 'jpg'
		elif DJANGO_TYPE == 'image/png':
			PIL_TYPE = 'png'
			FILE_EXTENSION = 'png'

		r = BytesIO(self.image.read())
		fullsize_image = Image.open(r)
		new_image = fullsize_image.copy()

		
		new_image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)


		temp_handle = BytesIO()
		new_image.save(temp_handle, PIL_TYPE)
		temp_handle.seek(0)

		suf = SimpleUploadedFile(os.path.split(self.image.name)[-1], temp_handle.read(), content_type=DJANGO_TYPE)
		self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)
