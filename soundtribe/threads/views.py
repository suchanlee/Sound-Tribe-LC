from random import randint

from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.views.generic.detail import SingleObjectTemplateResponseMixin, BaseDetailView
from django.db.models import Q
from django import http
from django.utils import simplejson as json
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin
from endless_pagination.views import AjaxListView

from threads.models import Thread, ThreadType
from misc.models import Facebook, Twitter, Tumblr, About, Contact
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
		context['threads'] = Thread.objects.filter(published=True)
		context['slideshow'] = Thread.objects.filter(Q(slideshow=True)&Q(published=True))[:5]
		interviews = Thread.objects.filter(Q(published=True)&Q(thread_type__slug='interview'))
		context['feature_artist'] = interviews[randint(0, len(interviews)-1)]
		return context

	# def get_context_data(self):
		# thread_types = ThreadType.objects.all()
		# types = []
		# for t in thread_types:
		# 	threads = Thread.objects.filter(Q(published=True)&Q(thread_type=t))[:4]
		# 	types.append([t,threads])
		# context = {
		# 	# 'slideshow': Thread.objects.filter(Q(slideshow=True)&Q(published=True))[:5],
		# 	'threads': Thread.objects.filter(published=True)[:8],
		# 	# 'interviews': Thread.objects.filter(Q(published=True)&Q(thread_type__slug='interview'))[:3],
		# 	'types': thread_types,
		# 	'menu_threads': types,
		# 	'facebook': Facebook.objects.get(id=1),
		# 	'twitter': Twitter.objects.get(id=1),
		# 	'tumblr': Tumblr.objects.get(id=1),
		# 	'contact': Contact.objects.get(id=1),
		# 	'about': About.objects.get(id=1),
		# }
		# return context


class AdminView(LoginRequiredMixin, TemplateView):
	template_name = 'threads/admin/admin.html'


# DETAIL VIEWS

class ThreadView(ThreadMixin, AjaxListView):
	context_object_name = 'threads'
	template_name = 'threads/public/thread_detail.html'
	page_template = 'threads/public/thread_post.html'
	queryset = []

	def get_context_data(self, **kwargs):
		context = super(ThreadView, self).get_context_data(**kwargs)
		context['single_thread'] = get_object_or_404(Thread, id=self.kwargs['pk'])
		context['threads'] = Thread.objects.filter(Q(id__lte=self.kwargs['pk'])&Q(published=True))
		ThreadMixin.increment_view(self, context['threads'][0])
		return context


class CategoryView(ThreadMixin, AjaxListView):
	context_object_name = 'threads'
	template_name = 'threads/public/thread_list.html'
	page_template = 'threads/public/thread_list_post.html'
	queryset = []

	def get_context_data(self, **kwargs):
		context = super(CategoryView, self).get_context_data(**kwargs)
		context['threads'] = Thread.objects.filter(Q(thread_type__slug=self.kwargs['category'])&Q(published=True))
		context['title'] = ThreadType.objects.get(slug=self.kwargs['category']).title
		try:
			context['single_thread'] = threads[0]
		except:
			context['single_thread'] = None
		return context


# LIST VIEWS

class ThreadListView(TemplateView):

	template_name = 'threads/admin/thread_list.html'

	def get_context_data(self, **kwargs):
		context = super(ThreadListView, self).get_context_data(**kwargs)
		if is_interview_path(self.request):
			context['objects'] = Thread.objects.filter(Q(thread_type__title='interview')&Q(published=True))
			context['unpublished_objects'] = Thread.objects.filter(Q(thread_type__title='interview')&Q(published=False))
			context['obj_title'] = 'interview list'
		else:
			context['objects'] = Thread.objects.filter(~Q(thread_type__title='interview')&Q(published=True))
			context['unpublished_objects'] = Thread.objects.filter(~Q(thread_type__title='interview')&Q(published=False))
			context['obj_title'] = 'thread list'
		return context

class ThreadTypeListView(TemplateView):

	template_name = 'threads/admin/threadtype_list.html'

	def get_context_data(self, **kwargs):
		context = super(ThreadTypeListView, self).get_context_data(**kwargs)
		context['objects'] = ThreadType.objects.all()
		context['obj_title'] = 'thread types'
		return context


# class TagListView(TemplateView):

# 	template_name = 'threads/public/home.html'

# 	def get_context_data(self, **kwargs):
# 		context = super(TagListView, self).get_context_data(**kwargs)
# 		context['threads'] = Thread.objects.filter(Q(tags__name__in=[self.kwargs['tag']])&Q(published=True))
# 		return context


class TagListView(AjaxListView):
	template_name = 'threads/public/thread_list.html'
	page_template = 'threads/public/thread_list_post.html'
	queryset = []

	def get_context_data(self, **kwargs):
		context = super(TagListView, self).get_context_data(**kwargs)
		context['threads'] = Thread.objects.filter(Q(tags__name__in=[self.kwargs['tag']])&Q(published=True))
		context['title'] = self.kwargs['tag']
		return context


# CREATE VIEWS

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


class ThreadTypeCreateView(LoginRequiredMixin, CreateView):
	model = ThreadType
	template_name = 'threads/admin/threadtype_form.html'
	success_url = '/admin/'


# UPDATE VIEWS

class ThreadTypeUpdateView(LoginRequiredMixin, UpdateView):
	model = ThreadType
	template_name = 'threads/admin/threadtype_form.html'
	success_url = '/admin/'


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
	model = Thread
	success_url = '/admin/'

	def get_template_names(self, **kwargs):
		context = super(ThreadUpdateView, self).get_context_data(**kwargs)
		if context['thread'].thread_type.title == 'interview':
			return ['threads/admin/interview_form.html']
		else:
			return ['threads/admin/thread_form.html']



