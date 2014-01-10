from random import randint

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectTemplateResponseMixin, BaseDetailView
from django.db.models import Q
from django import http
from django.utils import simplejson as json
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin
from endless_pagination.views import AjaxListView
from taggit.models import Tag
from haystack.forms import ModelSearchForm


from threads.models import Thread, ThreadType
from misc.models import Facebook, Twitter, Tumblr, About, Contact
from misc.models import Talkbox, MonthlyPlaylist, Listen
from core.helpers import is_interview_path

import pdb

# MIX INS
class ThreadMixin(object):
	'''
	A mixin that has various useful methods for the views
	'''
	def increment_view(self, thread):
		thread.views += 1
		thread.save()
		return thread


# TEMPLATE VIEWS

class HomeView(AjaxListView):
	template_name = 'threads/public/home.html'
	page_template = 'threads/public/thread_list_post.html'
	queryset = []

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['searchform'] = ModelSearchForm
		context['threads'] = Thread.objects.filter(published=True)
		context['slideshow'] = Thread.objects.filter(Q(slideshow=True)&Q(published=True))[:5]
		interviews = Thread.objects.filter(Q(published=True)&Q(title__icontains='(interview'))

		try:
			context['feature_artist'] = interviews[randint(0, len(interviews)-1)]
		except:
			pass
		try:
			context['mplaylist'] = MonthlyPlaylist.objects.latest('date_added').embed
		except:
			pass
		try:
			context['talkbox'] = Talkbox.objects.latest('date_added').embed
		except:
			pass
		try:
			context['listen'] = Listen.objects.latest('date_added').embed
		except:
			pass

		return context


class ThreadView(ThreadMixin, AjaxListView):
	context_object_name = 'threads'
	template_name = 'threads/public/thread_detail.html'
	page_template = 'threads/public/thread_post.html'
	queryset = []

	def get_context_data(self, **kwargs):
		context = super(ThreadView, self).get_context_data(**kwargs)
		context['searchform'] = ModelSearchForm
		context['single_thread'] = get_object_or_404(Thread, id=self.kwargs['pk'])
		context['threads'] = Thread.objects.filter(Q(created__lte=context['single_thread'].created)&Q(published=True))
		ThreadMixin.increment_view(self, context['threads'][0])
		return context

class CategoryThreadView(ThreadMixin, AjaxListView):
	context_object_name = 'threads'
	template_name = 'threads/public/thread_detail.html'
	page_template = 'threads/public/thread_post.html'
	queryset = []

	def get_context_data(self, **kwargs):
		context = super(CategoryThreadView, self).get_context_data(**kwargs)
		context['searchform'] = ModelSearchForm
		context['single_thread'] = get_object_or_404(Thread, id=self.kwargs['pk'])
		context['threads'] = Thread.objects.filter(
			Q(created__lte=context['single_thread'].created)&
			Q(published=True)&
			Q(thread_type__slug=self.kwargs['category']))
		ThreadMixin.increment_view(self, context['threads'][0])
		return context

class CategoryView(ThreadMixin, AjaxListView):
	context_object_name = 'threads'
	template_name = 'threads/public/thread_list.html'
	page_template = 'threads/public/thread_list_post.html'
	queryset = []

	def get_context_data(self, **kwargs):
		context = super(CategoryView, self).get_context_data(**kwargs)
		context['searchform'] = ModelSearchForm
		context['threads'] = Thread.objects.filter(Q(thread_type__slug=self.kwargs['category'])&Q(published=True))
		context['title'] = ThreadType.objects.get(slug=self.kwargs['category']).title
		context['type'] = 'category'
		try:
			context['single_thread'] = threads[0]
		except:
			context['single_thread'] = None
		return context

class TagListView(AjaxListView):
	template_name = 'threads/public/thread_list.html'
	page_template = 'threads/public/thread_list_post.html'
	queryset = []

	def get_context_data(self, **kwargs):
		context = super(TagListView, self).get_context_data(**kwargs)
		context['searchform'] = ModelSearchForm
		context['threads'] = Thread.objects.filter(Q(tags__slug__in=[self.kwargs['tag']])&Q(published=True))
		tag = Tag.objects.get(slug=self.kwargs['tag'])
		context['title'] = tag.name
		context['type'] = 'tag'
		return context


# ADMIN

class AdminView(LoginRequiredMixin, TemplateView):
	template_name = 'threads/admin/admin.html'


class ThreadListView(TemplateView):

	template_name = 'threads/admin/thread_list.html'

	def get_context_data(self, **kwargs):
		context = super(ThreadListView, self).get_context_data(**kwargs)

		audio_type = ThreadType.objects.get(slug='audio')
		video_type = ThreadType.objects.get(slug='video')
		talk_type = ThreadType.objects.get(slug='talk')
		review_type = ThreadType.objects.get(slug='review')

		context['audio_threads'] = Thread.objects.filter(thread_type=audio_type)
		context['video_threads'] = Thread.objects.filter(thread_type=video_type)
		context['talk_threads'] = Thread.objects.filter(thread_type=talk_type)
		context['review_threads'] = Thread.objects.filter(thread_type=review_type)

		return context

class ThreadTypeListView(TemplateView):

	template_name = 'threads/admin/threadtype_list.html'

	def get_context_data(self, **kwargs):
		context = super(ThreadTypeListView, self).get_context_data(**kwargs)
		context['objects'] = ThreadType.objects.all()
		context['obj_title'] = 'thread types'
		return context

class ThreadCreateView(LoginRequiredMixin, CreateView):
	model = Thread
	template_name = 'threads/admin/thread_form.html'
	success_url = '/admin/'

	def get_initial(self):
		initial = super(ThreadCreateView, self).get_initial()
		initial = initial.copy()
		initial['views'] = 0
		initial['likes'] = 0
		return initial

	def get_template_names(self):
		if is_interview_path(self.request):
			return ['threads/admin/interview_form.html']
		else:
			return ['threads/admin/thread_form.html']

class ThreadUpdateView(LoginRequiredMixin, UpdateView):
	model = Thread
	success_url = '/admin/'
	template_name =  'threads/admin/thread_form.html'


class ThreadDeleteView(LoginRequiredMixin, DeleteView):
	model = Thread
	template_name = 'threads/admin/thread_delete_form.html'
	success_url = '/threads/list/thread/'


class ThreadTypeCreateView(LoginRequiredMixin, CreateView):
	model = ThreadType
	template_name = 'threads/admin/threadtype_form.html'
	success_url = '/admin/'


class ThreadTypeUpdateView(LoginRequiredMixin, UpdateView):
	model = ThreadType
	template_name = 'threads/admin/threadtype_form.html'
	success_url = '/admin/'


