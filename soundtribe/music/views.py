from django.views.generic import DetailView, ListView, CreateView, UpdateView

from music.models import Artist


class ArtistListView(ListView):
	model = Artist
	template_name = 'music/public/artist_list.html'
	context_object_name = 'artists'


class ArtistDetailView(DetailView):
	model = Artist
	template_name = 'music/public/artist_detail.html'
	context_object_name = 'artist'


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