from django.shortcuts import render
from events.models import Event

# Create your views here.
def event_list(request):

	context = {
	}
	return render(request, 'list.html', context)

def event_detail(request):

	context = {
	}
	return render(request, 'detail.html', context)


def user_register(request):

	context = {
		"register_form": register_form
	}
	return render(request, 'user_register.html', context)

def user_login(request):

	context = {
		"login_form": login_form
	}
	return render(request, 'user_login.html', context)

def user_logout(request):
	logout(request)

	return redirect('list')