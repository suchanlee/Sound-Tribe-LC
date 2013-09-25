from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from redactor.fields import RedactorField


class ThreadModel(models.Model):
	'''
	An abstract base class model that provides
	self-updating created and modified fields as well
	as the common fields required for all threads
	'''
	title = models.CharField(max_length=50)
	slug = models.SlugField(blank=True, db_index=True)
	subtitle = models.CharField(max_length=150, blank=True)
	author = models.ForeignKey(User)
	main_image = models.FileField(upload_to='thread_main_images')
	thumbnail_image = models.FileField(upload_to='thread_main_thumbnails', blank=True, null=True)
	content = RedactorField(
		verbose_name = u'Content',
		redactor_options = {'lang': 'en', 'focus': 'true'},
		upload_to = 'thread/images/',
		allow_file_upload = True,
		allow_image_upload = True,
	)
	tags = TaggableManager(blank=True)
	likes = models.IntegerField(default=0)
	views = models.IntegerField(default=0)
	published = models.BooleanField(default=True)
	slideshow = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


	class Meta:
		abstract = True
