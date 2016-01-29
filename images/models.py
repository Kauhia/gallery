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
		"""from PIL import Image as PilImage

		print("image", self.image.url)
		filename = self.image.url.split('.')[0]
		self.thumbnail = PilImage.open(self.image.file)#.thumbnail(128, 128)#.save(filename + ".thumbnail", "JPEG")


		url = '%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION)
		self.thumbnail.save(, suf, save=False)
		#super(models.Model, self).save(*args, **kwargs)
		# models.Model.save(self, *args, **kwargs)"""

		self.create_thumbnail()
		super(Image, self).save()

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

		# Open original photo which we want to thumbnail using PIL's Image

		r = BytesIO(self.image.read())
		fullsize_image = Image.open(r)
		new_image = fullsize_image.copy()

		# Convert to RGB if necessary
		# Thanks to Limodou on DjangoSnippets.org
		# http://www.djangosnippets.org/snippets/20/
		#
		# I commented this part since it messes up my png files
		#
		#if image.mode not in ('L', 'RGB'):
		#    image = image.convert('RGB')

		# We use our PIL Image object to create the thumbnail, which already
		# has a thumbnail() convenience method that contrains proportions.
		# Additionally, we use Image.ANTIALIAS to make the image look better.
		# Without antialiasing the image pattern artifacts may result.
		
		new_image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
		#ImageOps.fit(new_image, THUMBNAIL_SIZE, Image.ANTIALIAS)

		# Save the thumbnail
		"""temp_handle = StringIO()
		image.save(temp_handle, PIL_TYPE)
		temp_handle.seek(0)"""

		temp_handle = BytesIO()
		new_image.save(temp_handle, PIL_TYPE)
		temp_handle.seek(0)

		# Save image to a SimpleUploadedFile which can be saved into
		# ImageField
		suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
		temp_handle.read(), content_type=DJANGO_TYPE)
		# Save SimpleUploadedFile into image field
		self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)
