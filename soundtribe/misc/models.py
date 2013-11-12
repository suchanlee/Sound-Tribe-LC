from django.db import models

from redactor.fields import RedactorField
import soundcloud as sc

import pdb


class Talkbox(models.Model):
	date_added = models.DateTimeField(auto_now_add=True)
	url = models.URLField(max_length=500)
	current_url = models.URLField(max_length=500, blank=True)
	embed = models.TextField(max_length=500, blank=True)

	class Meta:
		ordering = ['-date_added']

	def __unicode__(self):
		return self.url

	def save(self, *args, **kwargs):
		'''
		Get and save the embed code
		'''
		if (self.current_url != self.url):
			try:
				vid_id = self.url.split('watch?v=')[1]
				self.embed = '<iframe class="talkbox-embed" src="//www.youtube.com/embed/{}" frameborder="0" allowfullscreen></iframe>'.format(vid_id)
			except:
				pass
			self.current_url = self.url

		super(Talkbox, self).save(*args, **kwargs)


class MonthlyPlaylist(models.Model):
	date_added = models.DateTimeField(auto_now_add=True)
	url = models.URLField(max_length=500)
	current_url = models.URLField(max_length=500, blank=True)
	embed = models.TextField(max_length=1000, blank=True)

	class Meta:
		ordering = ['-date_added']

	def __unicode__(self):
		return self.url

	def save(self, *args, **kwargs):
		'''
		Get and save the embed code
		'''
		if (self.current_url != self.url):
			client = sc.Client(client_id='7b049100ad8da6c3ef9767248ddf7c0a') # move client_id out later
			try:
				embed_info = client.get('/oembed', url=self.url, maxheight='300', color='6E6E6E')
				self.embed = embed_info.html
				self.current_url = self.url
			except:
				self.current_url = self.url

		super(MonthlyPlaylist, self).save(*args, **kwargs)


class Listen(models.Model):
	date_added = models.DateTimeField(auto_now_add=True)
	url = models.URLField(max_length=500)
	current_url = models.URLField(max_length=500, blank=True)
	embed = models.TextField(max_length=500, blank=True)

	class Meta:
		ordering = ['-date_added']

	def __unicode__(self):
		return self.url

	def save(self, *args, **kwargs):
		'''
		Get and save the embed code
		'''
		if (self.current_url != self.url):
			try:
				vid_id = self.url.split('watch?v=')[1]
				self.embed = '<iframe class="listen-embed" src="//www.youtube.com/embed/{}" frameborder="0" allowfullscreen></iframe>'.format(vid_id)
			except:
				pass
			self.current_url = self.url

		super(Listen, self).save(*args, **kwargs)


class Subscription(models.Model):
	date_added = models.DateTimeField(auto_now_add=True)
	email = models.EmailField()


class Facebook(models.Model):
	url = models.URLField(max_length=200)
	show = models.BooleanField(default=True)


class Twitter(models.Model):
	url = models.URLField(max_length=200)
	show = models.BooleanField(default=True)


class Tumblr(models.Model):
	url = models.URLField(max_length=200)
	show = models.BooleanField(default=True)


class About(models.Model):
	content = RedactorField(
		verbose_name = u'Content',
		redactor_options = {'lang': 'en', 'focus': 'true'},
		upload_to = 'about/',
		allow_file_upload = True,
		allow_image_upload = True,
	)


class Contact(models.Model):
	content = RedactorField(
		verbose_name = u'Content',
		redactor_options = {'lang': 'en', 'focus': 'true'},
		upload_to = 'about/',
		allow_file_upload = True,
		allow_image_upload = True,
	)