from django.contrib.syndication.views import Feed
from threads.models import Thread
from django.core.urlresolvers import reverse


URL = 'http://soundtribelc.com/'

class RssFeed(Feed):
	title = 'SoundTribe threads RSS feed'
	link = '/threads/'
	description = 'Latest news from SoundTribe'

	def items(self):
		return Thread.objects.order_by('-created')

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return '<p>' + item.content.split('<p>')[1].strip('\r\n')

	def item_link(self, item):
		# return URL + 'threads/' + item.pk + '/' + item.slug + '/'	
		return reverse('thread_detail_view', args=[item.pk, item.slug])
	
	def item_author_name(self, item):
		return item.author.get_full_name()

	def item_pubdate(self, item):
		return item.created

	def item_updateddate(self, item):
		return item.modified