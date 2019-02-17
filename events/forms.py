from django import forms
from django.contrib.auth.models import User
from .models import Event

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [ 'username', 'first_name', 'last_name', 'password']
		widgets = {
			'password': forms.PasswordInput(),
		}

class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	fields = ['username', 'password']
	widgets = {
			'password': forms.PasswordInput(),
		}


class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ['owner',]
