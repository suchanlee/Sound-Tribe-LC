from django.conf.urls import patterns, include, url
from django.conf import settings

from threads.views import AdminView, HomeView, SubscribedUsersView
from misc.views import subscribe, AboutView, ContactView

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login_view'),
	url(r'^admin/$', AdminView.as_view(), name='admin_view'),
    url(r'^admin/subscribed_users/$', SubscribedUsersView.as_view(), name='subscribed_users_view'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^threads/', include('threads.urls'), name='thread_views'),
    url(r'^misc/', include('misc.urls'), name='misc_views'),
    url(r'^music/', include('music.urls'), name='music_views'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^contact/', ContactView.as_view(), name='contact'),
    url(r'^subscribe/submit/$', subscribe, name='subscribe')
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))