from django.conf.urls import patterns, url

from threads.views import HomeView, ThreadCreateView, ThreadTypeCreateView, ThreadView, ThreadUpdateView, ThreadListView, TagListView, CategoryView, CategoryThreadView, ThreadTypeListView, ThreadTypeUpdateView
from threads.api import thread_likes_increment, thread_fb_shared, thread_twtr_shared

urlpatterns = patterns('',
    # url(r'i/(?P<pk>\d+)/$', InterviewView.as_view(), name='interview_detail_view'),
    url(r'^(?P<pk>\d+)/(?P<thread_slug>\w(?:[-\w]*\w))/$', ThreadView.as_view(), name='thread_detail_view'),
    url(r'^(?P<category>\w(?:[-\w]*\w))/(?P<pk>\d+)/(?P<thread_slug>\w(?:[-\w]*\w))/$', CategoryThreadView.as_view(), name='category_detail_view'),
    url(r'^create/types/$', ThreadTypeCreateView.as_view(), name='type_create_view'),
    url(r'^create/interview/$', ThreadCreateView.as_view(), name='interview_create_view'),
    url(r'^create/thread/$', ThreadCreateView.as_view(), name='thread_create_view'),
    url(r'^list/interview/$', ThreadListView.as_view(), name='interview_list_view'),
    url(r'^list/thread/$', ThreadListView.as_view(), name='thread_list_view'),
    url(r'^list/types/$', ThreadTypeListView.as_view(), name='type_list_view'),
    url(r'^update/(?P<pk>\d+)/$', ThreadUpdateView.as_view(), name='thread_create_view'),
    url(r'^update/types/(?P<pk>\d+)/$', ThreadTypeUpdateView.as_view(), name='type_create_view'),
    url(r'^tags/(?P<tag>\w(?:[-\w]*\w))/$', TagListView.as_view(), name='tag_list_view'),
    url(r'^category/(?P<category>\w(?:[-\w]*\w))/$', CategoryView.as_view(), name='thread_category_view'),
    # to API
    url(r'^(?P<pk>\d+)/(?P<thread_slug>\w(?:[-\w]*\w))/likes/$', thread_likes_increment, name='thread_like'),
    url(r'^(?P<pk>\d+)/(?P<thread_slug>\w(?:[-\w]*\w))/facebook/share/$', thread_fb_shared, name='thread_fb_shared'),
    url(r'^(?P<pk>\d+)/(?P<thread_slug>\w(?:[-\w]*\w))/twitter/share/$', thread_twtr_shared, name='thread_twtr_shared'),
)