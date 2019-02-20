from django.shortcuts import render, redirect
from events.models import Event, Booking
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from datetime import date

from .models import Event
from .forms import UserRegisterForm, UserLoginForm, EventForm


# Create your views here.
def event_list(request):
    events = Event.objects.filter(date__gte=date.today())
    query = request.GET.get('q')
    if query:
        events = events.filter(
            Q(name__contains=query) |
            Q(description__icontains=query) |
            Q(organizer__username__icontains=query)
        ).distinct()



    context = {
        "events": events,
    }
    return render(request, 'homepage.html', context)


def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    action = ""
    bookings = []
    if request.user.is_authenticated:
        bookings = event.booking_set.all()
        if event.booking_set.filter(user=request.user).count() > 0:
            action = "booked"
        elif event.booking_set.all().count() >= event.capacity:
            action = "full"
        else:
            action = "book"

    context = {
        "event": event,
        "action": action,
        "bookings": bookings,
    }
    return render(request, 'detail.html', context)


def event_dashboard(request):
    events = Event.objects.filter(organizer=request.user)
    bookings = Booking.objects.filter(user=request.user)

    if request.user.is_anonymous:
        return redirect('user-login')

    context = {
        "events": events,
        "bookings": bookings,
    }
    return render(request, 'dashboard.html', context)

  
def event_create(request):
    form = EventForm()
    if request.user.is_anonymous:
        return redirect('user-login')
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('homepage')
    context = {
        "form": form,
    }
    return render(request, 'create.html', context)


def event_update(request, event_id):
    event_obj = Event.objects.get(id=event_id)
    organizer = event_obj.organizer

    if request.user.id is not organizer.id:
        return redirect('no-access')

    form = EventForm(instance=event_obj)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event_obj)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {
        "event_obj": event_obj,
        "form": form,
    }
    return render(request, "update.html", context)


def event_delete(request, event_id):
    event_obj = Event.objects.get(id=event_id)
    if event_obj.organizer.id != request.user.id:
        return redirect('noaccess')
    event_obj.delete()
    return redirect('homepage')


def noaccess(request):
    return render(request, 'noaccess.html')


def user_register(request):
    register_form = UserRegisterForm()
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('homepage')
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
            authenticated_user = authenticate(
                username=username, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('homepage')
    context = {
        "login_form": login_form
    }
    return render(request, 'user_login.html', context)


def user_logout(request):
    logout(request)

    return redirect('homepage')


def booking(request, event_id):
    event_object = Event.objects.get(id=event_id)

    if request.user.is_anonymous:
        return redirect('user-login')

        # CHECK IF AT CAPACITY

    favorite, created = Booking.objects.get_or_create(
        user=request.user, event=event_object)

    if not created:
        favorite.delete()

    return redirect('event-detail', event_id)



