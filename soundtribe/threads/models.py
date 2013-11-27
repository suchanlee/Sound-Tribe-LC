import datetime, pdb

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from redactor.fields import RedactorField


class ThreadModel(models.Model):
	'''
	An abstract base class model that provides
	self-updating created and modified fields as well
	as the common fields required for all threads
	'''
	thread_type = models.ForeignKey('ThreadType')
	title = models.CharField(max_length=200)
	slug = models.SlugField(blank=True, db_index=True)
	subtitle = models.CharField(max_length=200, blank=True)
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
	fb_shared = models.IntegerField(default=0, blank=True)
	twtr_shared = models.IntegerField(default=0, blank=True)
	views = models.IntegerField(default=0)
	published = models.BooleanField(default=True)
	slideshow = models.BooleanField(default=False)
	slideshow_image = models.FileField(upload_to='thread_slideshow_images', blank=True, null=True)
	created = models.DateTimeField(blank=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Thread(ThreadModel):
	artist_name = models.CharField(max_length=250, blank=True)
	artist_description = models.TextField(blank=True)
	artist_occupation = models.CharField(max_length=100, blank=True)
	artist_genre = models.CharField(max_length=100, blank=True)
	soundcloud_links = models.CharField(max_length=1500, blank=True, null=True)
	youtube_links = models.CharField(max_length=1500, blank=True, null=True)
	website = models.URLField(blank=True,null=True)
	facebook = models.URLField(blank=True, null=True)
	twitter = models.URLField(blank=True, null=True)
	tumblr = models.URLField(blank=True, null=True)
	bandcamp = models.URLField(blank=True, null=True)
	soundcloud = models.URLField(blank=True, null=True)
	youtube = models.URLField(blank=True, null=True)

	class Meta:
		ordering = ['-created']

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		'''
		If the post has not yet been saved
		create a slug from the title and save it
		'''
		if not self.id:
			self.created = datetime.datetime.now()
		if not self.slug:
			self.slug = slugify(self.title)

		super(Thread, self).save(*args, **kwargs)


class ThreadType(models.Model):

	title = models.CharField(max_length=100)
	slug = models.SlugField(blank=True, db_index=True)


	class Meta:
		ordering = ['slug']

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		'''
		If the post has not yet been saved
		create a slug from the title and save it
		'''
		self.slug = slugify(self.title)

		super(ThreadType, self).save(*args, **kwargs)



