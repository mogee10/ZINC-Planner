from django.shortcuts import render
from events.models import Event

# Create your views here.
def event_list(request):

	context = {
		"events":Event.objects.all()
	}
	return render(request, 'list.html', context)

def event_detail(request):

	event = Event.objects.get(id=event_id)
	context = {
		"event": event,
	}
	return render(request, 'detail.html', context)

def event_create(request):
	if request.user.is_anonymous:
		return redirect('signin')
	form = EventForm()
	if request.method == "POST":
		form = EventForm(request.POST, request.FILES)
		if form.is_valid():
			event = form.save(commit=False)
			event.owner = request.user
			event.save()
			return redirect('list')
	context = {
		"form":form,
	}
	return render(request, 'create.html', context)

def user_register(request):
    register_form = UserRegisterForm()
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('event-list')
    context = {
        "register_form": register_form
    }
    return render(request, 'user_register.html', context)

def user_login(request):
    login_form = UserLoginForm()
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('event-list')
    context = {
        "login_form": login_form
    }
    return render(request, 'user_login.html', context)

def user_logout(request):
    logout(request)

    return redirect('event-list')























