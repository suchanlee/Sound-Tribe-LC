from django.conf.urls import patterns, url

from misc.views import FacebookUpdateView, TwitterUpdateView, TumblrUpdateView, ContactUpdateView, AboutUpdateView
from misc.views import CreateTalkboxView, CreateListenView, CreatePlaylistView

urlpatterns = patterns('',
    url(r'^update/facebook/(?P<pk>\d+)$', FacebookUpdateView.as_view(), name='fb_update_view'),
    url(r'^update/twitter/(?P<pk>\d+)$', TwitterUpdateView.as_view(), name='twitter_update_view'),
    url(r'^update/tumblr/(?P<pk>\d+)$', TumblrUpdateView.as_view(), name='tumblr_update_view'),
    url(r'^update/about/(?P<pk>\d+)$', AboutUpdateView.as_view(), name='about_update_view'),
    url(r'^update/contact/(?P<pk>\d+)$', ContactUpdateView.as_view(), name='contact_update_view'),
    url(r'^create/talkbox/$', CreateTalkboxView.as_view(), name='contact_update_view'),
    url(r'^create/listen/$', CreateListenView.as_view(), name='contact_update_view'),
    url(r'^create/mplaylist/$', CreatePlaylistView.as_view(), name='contact_update_view'),
)