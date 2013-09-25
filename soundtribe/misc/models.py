from django.db import models
from redactor.fields import RedactorField


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