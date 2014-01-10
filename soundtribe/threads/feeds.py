from django.contrib.syndication.views import Feed
from threads.models import Thread
from django.core.urlresolvers import reverse


URL = 'http://soundtribelc.com/'

class RssFeed(Feed):
	title = 'Sound Tribe LC RSS Feed'
	link = '/threads/'
	description = 'Latest News from Sound Tribe LC'

	def items(self):
		return Thread.objects.order_by('-created')[:10]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.content

	def item_link(self, item):
		return reverse('thread_detail_view', args=[item.pk, item.slug])
	
	def item_author_name(self, item):
		return item.author.get_full_name()

	def item_pubdate(self, item):
		return item.created

	def item_updateddate(self, item):
		return item.modified