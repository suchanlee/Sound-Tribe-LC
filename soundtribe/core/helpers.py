

def is_interview_path(request):
	path_components = request.path.split('/')
	if path_components[len(path_components)-2] == 'interview':
		return True
	return False