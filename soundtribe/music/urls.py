from django.conf.urls import patterns, url

from music.views import ArtistListView, ArtistUpdateListView, ArtistDetailView, ArtistUpdateView, ArtistCreateView, music_contact_view, music_about_view, music_home, NoticeCreateView, NoticeUpdateListView, NoticeUpdateview, NoticeListView, NoticeDetailView

urlpatterns = patterns('',
    url(r'^$', music_home),
    url(r'^about/$', music_about_view),
    url(r'^contact/$', music_contact_view),
   
    # Notice urls
    url(r'^notice/create/$', NoticeCreateView.as_view(), name='notice_create_view'),
    url(r'^notice/update/$', NoticeUpdateListView.as_view(), name='notice_update_list_view'),
    url(r'^notice/update/(?P<pk>\d+)/$', NoticeUpdateview.as_view(), name='notice_update_view'),
    url(r'^notice/$', NoticeListView.as_view(), name='notice_list_view'),
    url(r'^notice/(?P<pk>\d+)/$', NoticeDetailView.as_view(), name='notice_detail_view'),

    # Artist urls
    url(r'^artist/$', ArtistListView.as_view(), name='artist_list_view'),
    url(r'^artist/(?P<pk>\d+)/$', ArtistDetailView.as_view(), name='artist_detail_view'),
    url(r'^artist/create/$', ArtistCreateView.as_view(), name='artist_create_view'),
    url(r'^artist/update/$', ArtistUpdateListView.as_view(), name='artist_update_list_view'),
    url(r'^artist/update/(?P<pk>\d+)/$', ArtistUpdateView.as_view(), name='artist_update_view'),
    
)