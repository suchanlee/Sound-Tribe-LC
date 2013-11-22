import pdb

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from threads.models import Thread, ThreadType


def thread_likes_increment(request, pk, thread_slug):
	thread = get_object_or_404(Thread, id=pk)
	thread.likes += 1
	thread.save()
	print thread.likes
	return HttpResponse('Thanks! This article now has {} likes!'.format(thread.likes))