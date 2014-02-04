from django.db import models
from PIL import Image

from music.image_processor import colors

import time

class Artist(models.Model):
	name = models.CharField(max_length=250, blank=True)
	image = models.FileField(upload_to='music/artist/profile_imgs/')
	dominant_color = models.CharField(max_length=10, default="#000000")
	sub_color = models.CharField(max_length=10, default="#000000")
	isSquare = models.BooleanField(default=False, editable=True)
	description = models.TextField(blank=True)
	genre = models.CharField(max_length=100, blank=True)
	website = models.URLField(blank=True,null=True)
	facebook = models.URLField(blank=True, null=True)
	twitter = models.URLField(blank=True, null=True)
	tumblr = models.URLField(blank=True, null=True)
	bandcamp = models.URLField(blank=True, null=True)
	soundcloud = models.URLField(blank=True, null=True)
	youtube = models.URLField(blank=True, null=True)

	class Meta:
		ordering = ['?']

	def save(self, *args, **kwargs):
		if self.image:
			try:
				# Extracting colors
				image_colors = colors(self.image)
				self.dominant_color = image_colors[1]
				self.sub_color = image_colors[0]
			except IOError, e:
				pass
			
			try:
				# Checking image aspect ratio
				im = Image.open(self.image)
				size = im.size
				if(size[0] < size[1]*1.25):
					self.isSquare = True
			except IOError:
				pass

		super(Artist, self).save(*args, **kwargs)


class Notice(models.Model):
	date = models.DateField(default=time.strftime("%Y-%m-%d"))
	category = models.CharField(max_length=20, blank=False)
	content = models.CharField(max_length=200, blank=False)

	# Add relation to Artist model

	class Meta:
		ordering = ['date']