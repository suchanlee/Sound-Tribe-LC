from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404

import pdb

from braces.views import LoginRequiredMixin

from misc.models import Facebook, Twitter, Tumblr, About, Contact, Subscription

def subscribe(request):
	if request.is_ajax():
		try:
			Subscription.objects.create(email=request.POST['email'])
			message = 'success'
		except:
			message = 'failure'
	return HttpResponse(message);

class FacebookUpdateView(LoginRequiredMixin, UpdateView):

	model = Facebook
	template_name = 'threads/admin/misc_form.html'
	success_url = '/admin/'

	def get_context_data(self, **kwargs):
		context = super(FacebookUpdateView, self).get_context_data(**kwargs)
		context['form_title'] = 'facebook'
		return context


class TwitterUpdateView(LoginRequiredMixin, UpdateView):

	model = Twitter
	template_name = 'threads/admin/misc_form.html'
	success_url = '/admin/'

	def get_context_data(self, **kwargs):
		context = super(TwitterUpdateView, self).get_context_data(**kwargs)
		context['form_title'] = 'twitter'
		return context


class TumblrUpdateView(LoginRequiredMixin, UpdateView):

	model = Tumblr
	template_name = 'threads/admin/misc_form.html'
	success_url = '/admin/'

	def get_context_data(self, **kwargs):
		context = super(TumblrUpdateView, self).get_context_data(**kwargs)
		context['form_title'] = 'tumblr'
		return context


class ContactUpdateView(LoginRequiredMixin, UpdateView):

	model = Contact
	template_name = 'threads/admin/misc_form.html'
	success_url = '/admin/'

	def get_context_data(self, **kwargs):
		context = super(ContactUpdateView, self).get_context_data(**kwargs)
		context['form_title'] = 'contact'
		return context


class AboutUpdateView(LoginRequiredMixin, UpdateView):

	model = About
	template_name = 'threads/admin/misc_form.html'
	success_url = '/admin/'

	def get_context_data(self, **kwargs):
		context = super(AboutUpdateView, self).get_context_data(**kwargs)
		context['form_title'] = 'about'
		return context
