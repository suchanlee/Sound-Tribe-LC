import pdb

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from threads.models import Thread, ThreadType


def thread_likes_increment(request, pk, thread_slug):
	thread = get_object_or_404(Thread, id=pk)
	thread.likes += 1
	thread.save()
	return HttpResponse('Thanks! This thread now has {} likes!'.format(thread.likes))

def thread_fb_shared(request, pk, thread_slug):
	thread = get_object_or_404(Thread, id=pk)
	thread.fb_shared += 1
	thread.save()
	return HttpResponse('fb shared')

def thread_twtr_shared(request, pk, thread_slug):
	thread = get_object_or_404(Thread, id=pk)
	thread.twtr_shared += 1
	thread.save()
	return HttpResponse('twitter shared')