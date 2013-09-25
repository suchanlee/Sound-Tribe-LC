from django.db import models


class Artist(models.Model):
	name = models.CharField(max_length=250, blank=True)
	image = models.FileField(upload_to='music/artist/profile_imgs/')
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
		ordering = ['name']
