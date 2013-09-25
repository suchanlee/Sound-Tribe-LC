from django.conf.urls import patterns, url

from music.views import ArtistListView, ArtistUpdateListView, ArtistDetailView, ArtistUpdateView, ArtistCreateView

urlpatterns = patterns('',
    url(r'^artist/$', ArtistListView.as_view(), name='artist_list_view'),
    url(r'^artist/(?P<pk>\d+)/$', ArtistDetailView.as_view(), name='artist_detail_view'),
    url(r'^artist/create/$', ArtistCreateView.as_view(), name='artist_create_view'),
    url(r'^artist/update/$', ArtistUpdateListView.as_view(), name='artist_update_list_view'),
    url(r'^artist/update/(?P<pk>\d+)/$', ArtistUpdateView.as_view(), name='artist_update_view'),
)