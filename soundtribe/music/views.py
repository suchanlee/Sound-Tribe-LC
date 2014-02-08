from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from music.image_processor import colors
from music.models import Artist, Notice


class ArtistListView(ListView):
	model = Artist
	template_name = 'music/public/artist_list.html'
	context_object_name = 'artists'


class ArtistDetailView(DetailView):
	model = Artist
	template_name = 'music/public/artist_detail.html'
	# context_object_name = 'artist'

	def get_context_data(self, **kwargs):
		context = super(ArtistDetailView, self).get_context_data(**kwargs)
		
		context['notices'] = Notice.objects.all()
		return context

class ArtistCreateView(CreateView):
	model = Artist
	template_name = 'music/admin/artist_form.html'
	success_url = '/admin/'

class ArtistUpdateView(UpdateView):
	model = Artist
	template_name = 'music/admin/artist_form.html'
	success_url = '/admin/'

class ArtistUpdateListView(ListView):
	model = Artist
	template_name = 'music/admin/artist_list.html'
	context_object_name = 'artists'

class ArtistDeleteView(DeleteView):
	model = Artist
	template_name = 'music/admin/artist_delete.html'
	success_url = '/admin/'

class ArtistDeleteListView(ListView):
	model = Artist
	template_name = 'music/admin/artist_list_delete.html'
	context_object_name = 'artists'



def music_about_view(request):
	return render(request, 'music/public/artist_about.html')

def music_contact_view(request):
	return render(request, 'music/public/artist_contact.html')

def music_home(request):
	notices = Notice.objects.all()
	artists = Artist.objects.all()[0:4]
	return render(request, 'music/public/music_home.html', {'notices': notices, 'artists': artists})

class NoticeCreateView(CreateView):
	model = Notice
	template_name = 'music/admin/notice_form.html'
	success_url = '/admin/'

class NoticeListView(ListView):
	model = Notice
	template_name = 'music/public/notice_list.html'
	context_object_name = 'notices'

class NoticeDetailView(DetailView):
	model = Notice
	template_name = 'music/public/notice_detail.html'
	context_object_name = 'notice'

class NoticeUpdateview(UpdateView):
	model = Notice
	template_name = 'music/admin/notice_form.html'
	success_url = '/admin/'

class NoticeUpdateListView(ListView):
	model = Notice
	template_name = 'music/admin/notice_list.html'
	context_object_name = 'notices'